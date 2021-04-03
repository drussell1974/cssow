from shared.models.core.log_handlers import handle_log_warning
from shared.models.cls_lesson import LessonModel, try_int
from shared.models.cls_lesson_schedule import LessonScheduleModel
from shared.models.enums.publlished import STATE
from shared.models.utils.class_code_generator import ClassCodeGenerator 
from shared.viewmodels.baseviewmodel import BaseViewModel
from shared.view_model import ViewModel

class LessonScheduleEditViewModel(BaseViewModel):

    def __init__(self, db, request, schedule_id, lesson_id, scheme_of_work_id, auth_ctx):
        self.db = db
        self.request = request
        self.schedule_id = schedule_id
        self.lesson_id = lesson_id
        self.scheme_of_work_id = scheme_of_work_id
        self.auth_ctx = auth_ctx
        self.lesson = LessonModel.get_model(db, lesson_id=lesson_id, scheme_of_work_id=scheme_of_work_id, auth_user=auth_ctx)
        # Http404
        if self.lesson_id > 0:
            if self.lesson is None or self.lesson.is_from_db == False:
                self.on_not_found(self.lesson, self.lesson_id)
                return
                
        if schedule_id > 0:
            self.model = LessonScheduleModel.get_model(db, schedule_id=schedule_id, lesson_id=lesson_id, scheme_of_work_id=schedule_id, auth_user=auth_ctx)
        else:
            self.model = LessonScheduleModel.new(lesson_id=lesson_id, scheme_of_work_id=scheme_of_work_id, auth_ctx=auth_ctx, fn_generate_class_code=ClassCodeGenerator.generate_class_code)
            self.model.created_by_id = auth_ctx.auth_user_id
        
        
    def execute(self):
        try:
            published_state = STATE.parse(self.request.POST["published"] if self.request.POST["published"] is not None else "PUBLISH")
            
            self.model.start_date = self.request.POST['start_date']
            create_new_class_code = self.request.POST.get("generate_class_code", False)
            if create_new_class_code:
                self.model.class_code = ClassCodeGenerator.generate_class_code(6)
            else:
                self.model.class_code = self.request.POST.get("class_code")
            self.model.class_name = self.request.POST.get('class_name')
            self.model.published = published_state

            self.model.validate()

            # TODO: save
            if self.model.is_valid:
                LessonScheduleModel.save(self.db, self.model, self.auth_ctx, published_state)
                self.on_post_complete(saved=True)
            else:
                self.error_message = self.model.validation_errors
                handle_log_warning(self.db, self.model.id, "saving scheduled lesson", " scheduled lesson is not valid (id:{}, name:{}, start_date:{}, validation_errors (count:{}).".format(self.model.id, self.model.class_name, self.model.start_date, len(self.model.validation_errors)))

        except Exception as ex: 
            self.error_message = ex
            self.on_exception(ex)
            raise Exception(ex)


    def view(self):

        data = {
            "scheme_of_work_id": self.scheme_of_work_id,
            "lesson_id": self.lesson_id,
            "model": self.model
        }
        
        return ViewModel(self.model.class_name, self.lesson.title if self.lesson is not None else "", "Edit: {} {}".format(self.model.class_name, self.model.start_date) if self.model.id > 0 else "Create new schedule for {} {}".format(self.model.class_name, self.model.start_date), ctx=self.auth_ctx, data=data, active_model=self.model, alert_message="", error_message=self.error_message)
