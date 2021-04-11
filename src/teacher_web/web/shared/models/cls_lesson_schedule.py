from django.db import models
from django.conf import settings
from shared.models.core.basemodel import BaseModel, try_int
from shared.models.core.db_helper import ExecHelper, sql_safe, to_empty, TRANSACTION_STATE
from shared.models.core.log_handlers import handle_log_info, handle_log_error
from shared.models.core.helper_string import date_to_string
from shared.models.enums.publlished import STATE

from datetime import datetime, timedelta

class LessonScheduleModel(BaseModel):
    
    title = ""
    class_name = ""
    class_code = ""
    period = 0
    start_date = ""
    start_date_ui_date = ""
    start_date_ui_time = ""
    edit_url = ""
    whiteboard_url = ""
    lesson_id = 0
    scheme_of_work_id = 0
    department_id = 0
    institute_id = 0
    is_from_db = False

    def __init__(self, id_, title, class_name, class_code, start_date, lesson_id, scheme_of_work_id, created = "", created_by_id = 0, created_by_name = "", published=STATE.PUBLISH, is_from_db=False, auth_user=None, fn_resolve_url=None):
        super().__init__(id_, f"{title} - {class_name} ({class_code})", created, created_by_id, created_by_name, published, is_from_db, ctx=auth_user)
        self.title = title
        self.class_name = class_name
        self.class_code = class_code
        self.whiteboard_url = "" # default
        self.edit_url = "" # default
        self.start_date = start_date # date_to_string(start_date) if start_date is datetime else start_date
        if type(start_date) is datetime:
            start_date = start_date.strftime(settings.ISOFORMAT)
        if "T" in start_date:
            self.start_date_ui_date = start_date.split("T")[0]
            self.start_date_ui_time = start_date.split("T")[1]
        self.lesson_id = try_int(lesson_id)
        self.scheme_of_work_id = try_int(scheme_of_work_id)

        if fn_resolve_url is not None:
            self.whiteboard_url  = fn_resolve_url(self)["lesson_schedule.whiteboard_view"]
            self.edit_url = fn_resolve_url(self)["lesson_schedule.edit"]


    @property
    def is_today(self):
        return True if self.start_date.date() == datetime.today().date() else False


    @property
    def input_date(self):
        # format as "2021-04-03T11:23" for datetime-local input field
        if self.start_date is None:
            return ""
        return self.start_date.strftime(settings.ISOFORMAT)

    @property
    def display_date(self):
        if self.start_date is None:
            return ""
        elif self.is_today:
            return "Today"
        else:
            return date_to_string(self.start_date)
        

    @classmethod
    def new(cls, lesson_id, scheme_of_work_id, auth_ctx, fn_generate_class_code):
        start_date = date_to_string(datetime.now())
        new_class_code = fn_generate_class_code(length=6)
        return LessonScheduleModel(0, title="", class_name="", class_code=new_class_code, start_date=start_date, lesson_id=lesson_id, scheme_of_work_id=scheme_of_work_id, auth_user=auth_ctx)


    def validate(self, skip_validation = []):
        """ clean up and validate model """
        super().validate(skip_validation)

        # Validate class code
        self._validate_required_string("class_code", self.class_code, 6, 6)
        
        # Validate class name
        self._validate_required_string("class_name", self.class_name, 1, 10)
        
        return self.is_valid


    def _clean_up(self):
        """ clean up properties by casting and ensuring safe for inserting etc """

        self.id = int(self.id)
    
        if self.class_code is not None:
            self.class_code = sql_safe(self.class_code)

        if self.class_name is not None:
            self.class_name = sql_safe(self.class_name)


    @staticmethod
    def get_all(db, lesson_id, scheme_of_work_id, auth_user, show_next_days=0, fn_resolve_url=None):
        
        #432 use academic year start and end by default 
        from_date = auth_user.academic_year.start_date if show_next_days == 0 and auth_user.institute_id > 0 else datetime.today().date()
        to_date = auth_user.academic_year.end_date if show_next_days == 0 and auth_user.institute_id > 0 else datetime.today().date() + timedelta(show_next_days)
        
        rows = LessonScheduleDataAccess.get_all(db, lesson_id=lesson_id, scheme_of_work_id=scheme_of_work_id, department_id=auth_user.department_id, institute_id=auth_user.institute_id, auth_user_id=auth_user.auth_user_id, from_date=from_date, to_date=to_date, show_published_state=auth_user.can_view)
        
        result = []
        for row in rows:
            model = LessonScheduleModel(
                id_=row[0],
                title=row[1],
                class_name=row[2],
                class_code = row[3],
                start_date=row[4],
                lesson_id = row[5],
                scheme_of_work_id=row[6],
                published=row[9],
                created_by_id=row[10],
                auth_user=auth_user,
                fn_resolve_url=fn_resolve_url)

            model.department_id=row[7]
            model.institute_id=row[8]

            model.on_fetched_from_db()
            
            result.append(model)

        return result


    @staticmethod
    def get_model(db, schedule_id, lesson_id, scheme_of_work_id, auth_user):
        rows = LessonScheduleDataAccess.get_model(db, schedule_id, lesson_id, scheme_of_work_id, auth_user_id=auth_user.auth_user_id, show_published_state=auth_user.can_view)
        model = None
        for row in rows:
            model = LessonScheduleModel(
                id_=schedule_id,
                title=row[0],
                class_name=row[1],
                class_code = row[2],
                start_date=row[3],
                lesson_id = row[4],
                scheme_of_work_id=row[5],
                published=row[6],
                created_by_id=row[7],
                auth_user=auth_user)
            model.on_fetched_from_db()
        return model


    @staticmethod
    def get_model_by_class_code(db, class_code, auth_user):
        rows = LessonScheduleDataAccess.get_model_by_class_code(db, class_code, auth_user_id=auth_user.auth_user_id, show_published_state=auth_user.can_view)
        model = None
        
        for row in rows:
            if auth_user.department_id == 0 and auth_user.institute_id == 0:
                # handle empty context
                auth_user.department_id = row[6]
                auth_user.institute_id = row[7]
                
            model = LessonScheduleModel(
                id_=row[0],
                title=row[1],
        		class_name = row[2],
                class_code = class_code,
                start_date = row[3],
                lesson_id = row[4],
                scheme_of_work_id=row[5],
                published=row[8],
                created_by_id=row[9],
                auth_user=auth_user)
            model.on_fetched_from_db()
        return model


    @staticmethod
    def save(db, model, auth_user, published):
        """ Save Lesson """
        try:     
            if model.is_new() == True:
                model = LessonScheduleDataAccess._insert(db, model, published, auth_ctx=auth_user)
            elif published == STATE.DELETE:
                model = LessonScheduleDataAccess._delete(db, model=model, auth_user_id=auth_user.auth_user_id)
                model.published = published
            else:
                model = LessonScheduleDataAccess._update(db, model, published, auth_ctx=auth_user)
            return model
        except:
            handle_log_error(db, 0, "error saving lesson schedule")
            raise
    

    @staticmethod
    def delete_unpublished(db, lesson_id, scheme_of_work_id, auth_user):
        return LessonScheduleDataAccess.delete_unpublished(db, lesson_id, scheme_of_work_id, auth_user_id=auth_user.auth_user_id)

    
    @staticmethod
    def delete(db, model, auth_user):
        LessonScheduleDataAccess._delete(db, model=model, auth_user_id=auth_user.auth_user_id)
        return model
    

class LessonScheduleDataAccess:

    @staticmethod
    def get_all(db, institute_id, department_id, scheme_of_work_id, lesson_id, auth_user_id, from_date, to_date, show_published_state=STATE.PUBLISH):
        """
        get lesson schedule

        :param db:database context
        :param id_: the schedule identifier
        :param lesson_id: the lesson identifie
        :param scheme_of_work_id: the scheme of work identifier
        :param auth_user_id: the user executing the command
        :return: the lesson
        """
        
        execHelper = ExecHelper()
        select_sql = "lesson_schedule__get_all$2"
        params = (lesson_id, scheme_of_work_id, department_id, institute_id, from_date, to_date, int(show_published_state), auth_user_id)
        
        rows = []
        rows = execHelper.select(db, select_sql, params, rows, handle_log_info)
        
        return rows


    @staticmethod
    def get_model(db, id_, lesson_id, scheme_of_work_id, auth_user_id, show_published_state=STATE.PUBLISH):
        """
        get all lesson schedules for the lesson

        :param db:database context
        :param lesson_id: the lesson identifie
        :param scheme_of_work_id: the scheme of work identifier
        :param auth_user_id: the user executing the command
        :return: the lesson
        """
        
        execHelper = ExecHelper()
        select_sql = "lesson_schedule__get$3"
        params = (id_, int(show_published_state), auth_user_id)
        
        rows = []
        rows = execHelper.select(db, select_sql, params, rows, handle_log_info)
        
        return rows


    @staticmethod
    def get_model_by_class_code(db, class_code, auth_user_id, show_published_state=STATE.PUBLISH):
        """
        get lesson schedule

        :param db:database context
        :param id_: the lesson identifier
        :param class_code: class_code
        :return: the lesson schedule
        """
        
        execHelper = ExecHelper()
        select_sql = "lesson_schedule__get_by_class_code$3"
        params = (class_code, int(show_published_state), auth_user_id)
        
        rows = []
        rows = execHelper.select(db, select_sql, params, rows, handle_log_info)
        
        return rows


    @staticmethod
    def _update(db, model, published, auth_ctx):
        """ 
        updates the sow_lesson_schedule

        :param db: the database context
        :param model: the lesson schedule model
        :param published: the published status id
        :param auth_ctx: the context and user executing the command
        :return: the updated model
        """

        execHelper = ExecHelper()
        
        str_update = "lesson_schedule__update$2"
        params = (
            model.id,
            model.start_date,
            model.class_code,
            model.class_name,
            auth_ctx.institute_id,
            auth_ctx.department_id,
            model.scheme_of_work_id,
            model.lesson_id,
            int(published),
            auth_ctx.auth_user_id
        )

        rows = []
        rows = execHelper.update(db, str_update, params, handle_log_info)

        return model


    @staticmethod
    def _insert(db, model, published, auth_ctx):
        """ 
        inserts the sow_lesson_schedule

        :param db: the database context
        :param model: the lesson schedule model
        :param published: the published status id
        :param auth_ctx: the context and user executing the command
        :return: the model with new identifier
        """

        execHelper = ExecHelper()

        str_insert = "lesson_schedule__insert$2"
        params = (
            model.id,
            model.start_date,
            model.class_code,
            model.class_name,
            auth_ctx.institute_id,
            auth_ctx.department_id,
            model.scheme_of_work_id,
            model.lesson_id,
            int(published),
            auth_ctx.auth_user_id
        )
    

        result = execHelper.insert(db, str_insert, params, handle_log_info)
    
        model.id = result[0]

        return model


    @staticmethod
    def _delete(db, model, auth_user_id):
        """ 
        Delete desson schedule 

        :param db: the database context
        :param model: the lesson schedule model
        :param auth_ctx: the context and user executing the command
        :return: the deleted model
        """
        
        execHelper = ExecHelper()
        
        str_delete = "lesson_schedule__delete"
        params = (model.id, auth_user_id)
        
        rval = execHelper.delete(db, str_delete, params, handle_log_info)

        return model


    @staticmethod
    def delete_unpublished(db, lesson_id, scheme_of_work_id, auth_user_id):
        """ 
        Delete all unpublished lessons schedules 

        :param db: the database context
        :param lesson_id: the lesson identifier
        :param scheme_of_work_id: the lesson identifier
        :param auth_user_id: the user executing the command
        :return: the rows
        """

        execHelper = ExecHelper()
        
        str_delete = "lesson_schedule__delete_unpublished"
        params = (lesson_id, scheme_of_work_id, auth_user_id)
        
        rows = []
        rows = execHelper.delete(db, str_delete, params, handle_log_info)
        
        return rows
