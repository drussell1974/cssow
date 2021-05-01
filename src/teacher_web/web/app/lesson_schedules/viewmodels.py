from datetime import datetime, timedelta
from django.conf import settings
from django.http import Http404
from django.urls import reverse
from shared.models.core.helper_string import date_to_string
from shared.models.core.log_type import LOG_TYPE
from shared.models.core.log_handlers import handle_log_warning, handle_log_exception, handle_log_info
from shared.models.cls_academic_year import AcademicYearModel
from shared.models.cls_lesson import LessonModel, try_int
from shared.models.cls_lesson_schedule import LessonScheduleModel
from shared.models.cls_notification import NotifyModel
from shared.models.cls_schemeofwork import SchemeOfWorkModel
from shared.models.enums.publlished import STATE
from shared.models.utils.class_code_generator import ClassCodeGenerator 
from shared.viewmodels.baseviewmodel import BaseViewModel
from shared.view_model import ViewModel


class LessonScheduleIndexViewModel(BaseViewModel):
    
    
    def __init__(self, db, request, lesson_id, scheme_of_work_id, auth_user):
        
        self.model = []
        self.db = db
        self.request = request
        self.scheme_of_work_id = scheme_of_work_id
        self.lesson_id = lesson_id
        self.auth_user = auth_user
        self.lesson_options = []
        
        try:
            # get model
            # TODO: #323 call read only model
            self.lesson = LessonModel.get_model(self.db, self.lesson_id, self.scheme_of_work_id, self.auth_user)
            # TODO: #323 call read only model
            self.scheme_of_work = SchemeOfWorkModel.get_model(self.db, self.scheme_of_work_id, self.auth_user)
            
            # if not found then raise error
            if self.lesson_id > 0:
                if self.lesson is None or self.lesson.is_from_db == False:
                    self.on_not_found(self.lesson, self.lesson_id, self.scheme_of_work_id)

            self.lesson_options = LessonModel.get_options(self.db, self.scheme_of_work_id, self.auth_user)  

            # get default from settings
            self.show_next_days = request.session.get("lesson_schedule.show_next_days", settings.PAGER["schedule"]["pagesize"])

            if request.method == "POST":
                # get show_next_days from POST or use default set above
                self.show_next_days = try_int(request.POST.get("show_next_days", self.show_next_days))
                request.session["lesson_schedule.show_next_days"] = self.show_next_days

            # get model
            data = LessonScheduleModel.get_all(db, lesson_id=lesson_id, scheme_of_work_id=scheme_of_work_id, show_next_days=self.show_next_days, auth_user=auth_user)
            self.model = data

        except Http404 as e:
            raise e

        except Exception as e:
            handle_log_exception(self.db, self.scheme_of_work_id, "An error occured viewing resources", e)
            self.error_message = repr(e)
            raise e

    def view(self, request):

        data = {
            "scheme_of_work_id": self.scheme_of_work_id,
            "lesson_id":self.lesson_id,
            "scheme_of_work": self.scheme_of_work,
            "lesson": self.lesson,
            "schedules": self.model,
            "lesson_options": self.lesson_options,
            "show_next_days": self.show_next_days,
            "days_to_show__options": settings.PAGER["schedule"]["pagesize_options"],
        }
        
        return ViewModel(request, self.lesson.title, self.lesson.title, "Scheduled lessons", ctx=self.auth_user, data=data, active_model=self.lesson, error_message=self.error_message)


class LessonScheduleEditViewModel(BaseViewModel):

    def __init__(self, db, request, schedule_id, lesson_id, scheme_of_work_id, auth_ctx, action_url = "", start_date = None):
        self.db = db
        self.request = request
        self.schedule_id = schedule_id
        self.lesson_id = lesson_id
        self.scheme_of_work_id = scheme_of_work_id
        self.auth_ctx = auth_ctx
        self.action_url = action_url
        self.return_url = ""
        
        self.lesson = LessonModel.get_model(db, lesson_id=lesson_id, scheme_of_work_id=scheme_of_work_id, auth_user=auth_ctx)
        # Http404
        if self.lesson_id > 0:
            if self.lesson is None or self.lesson.is_from_db == False:
                self.on_not_found(self.lesson, self.lesson_id)
                return
                
        if schedule_id > 0:
            self.model = LessonScheduleModel.get_model(db, schedule_id=schedule_id, lesson_id=lesson_id, scheme_of_work_id=schedule_id, auth_user=auth_ctx)
        else:
            self.model = LessonScheduleModel.new(lesson_id=lesson_id, scheme_of_work_id=scheme_of_work_id, start_date=start_date, auth_ctx=auth_ctx, fn_generate_class_code=ClassCodeGenerator.generate_class_code)
            self.model.created_by_id = auth_ctx.auth_user_id
        
        
    def execute(self):
        try:
            published_state = STATE.parse(self.request.POST["published"] if self.request.POST["published"] is not None else "PUBLISH")
            
            # join selected date and time
            self.model.start_date = f"{self.request.POST['start_date']}T{self.request.POST['period']}"

            create_new_class_code = self.request.POST.get("generate_class_code", False)
            if create_new_class_code:
                self.model.class_code = ClassCodeGenerator.generate_class_code(6)
            else:
                self.model.class_code = self.request.POST.get("class_code")
            self.model.class_name = self.request.POST.get('class_name')
            self.model.published = published_state
                
            self.model.validate()

            if self.model.is_valid:
                LessonScheduleModel.save(self.db, self.model, self.auth_ctx, published_state)
                
                #432 set reminder n minutes before start_date (string to date)
                offset_min = self.request.POST.get('reminder_minutes_before', 0) # TODO: get reminder_minutes_before value from form
                reminder = self.model.start_date - timedelta(minutes=try_int(offset_min))
                # back to string
                reminder = reminder.strftime(settings.ISOFORMAT)

                NotifyModel.create(
                        db=self.db,
                        title="Create scheduled lesson",
                        message=f"lesson {self.model.start_date_ui_date} {self.model.start_date_ui_time} for {self.model.class_name}",
                        action_url=self.action_url,
                        auth_ctx=self.auth_ctx,
                        notify_dt=reminder,
                        handle_log_info=handle_log_info
                    )

                self.on_post_complete(saved=True)
            
            else:
                self.error_message = self.model.validation_errors
                handle_log_warning(self.db, self.model.id, "saving scheduled lesson", " scheduled lesson is not valid (id:{}, name:{}, start_date:{}, validation_errors (count:{}).".format(self.model.id, self.model.class_name, self.model.start_date, len(self.model.validation_errors)))

        except Exception as ex: 
            self.error_message = ex
            self.on_exception(ex)
            raise Exception(ex)


    def view(self, request):

        data = {
            "scheme_of_work_id": self.scheme_of_work_id,
            "lesson_id": self.lesson_id,
            "model": self.model,
            "period_options": self.auth_ctx.periods,
            "reminder_options": { 5:"5 minutes", 10:"10 minutes", 15:"15 minutes", 30:"30 minutes", 60:"1 hour"},
            "return_url": self.return_url
        }
        
        return ViewModel(request, self.model.class_name, self.lesson.title if self.lesson is not None else "", "Edit scheduled lesson {} for {}".format(self.lesson.title, self.model.class_name) if self.model.id > 0 else "Create schedule for {}".format(self.lesson.title), ctx=self.auth_ctx, data=data, active_model=self.model, alert_message="", error_message=self.error_message)


class LessonScheduleDeleteViewModel(BaseViewModel):

    def __init__(self, db, schedule_id, lesson_id, scheme_of_work_id, auth_ctx):
        self.db = db
        self.schedule_id = schedule_id
        self.auth_ctx = auth_ctx
        self.model = LessonScheduleModel.get_model(db, schedule_id, lesson_id, scheme_of_work_id, auth_user=auth_ctx)
        # Http404
        if self.schedule_id > 0:
            if self.model is None or self.model.is_from_db == False:
                self.on_not_found(self.model, schedule_id, lesson_id)


    def execute(self):
        if self.model is not None:
            # can now delete
            self.model = LessonScheduleModel.delete(self.db, self.model, auth_user=self.auth_ctx)


class LessonScheduleWhiteboardViewModel(BaseViewModel):
    
    def __init__(self, db, schedule_id, lesson_id, scheme_of_work_id, auth_user, resource_type_id = 0):
        self.db = db
        # get model
        model = LessonModel.get_model(self.db, lesson_id, scheme_of_work_id, auth_user, resource_type_id)
        self.lesson_schedule = LessonScheduleModel.get_model(self.db, schedule_id, lesson_id, scheme_of_work_id, auth_user)
        self.STUDENT_WEB__WEB_SERVER_WWW = settings.STUDENT_WEB__WEB_SERVER_WWW

        # if not found then raise error
        if lesson_id > 0:
            if model is None or model.is_from_db == False:
                self.on_not_found(model, lesson_id, scheme_of_work_id)

        self.model = model
