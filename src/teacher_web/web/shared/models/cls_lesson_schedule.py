from django.db import models
from shared.models.core.basemodel import BaseModel, try_int
from shared.models.core.db_helper import ExecHelper, sql_safe, to_empty, TRANSACTION_STATE
from shared.models.core.log_handlers import handle_log_info, handle_log_error
from shared.models.enums.publlished import STATE

class LessonScheduleModel(BaseModel):
        
    lesson_id = 0
    scheme_of_work_id = 0
    department_id = 0
    institute_id = 0

    def __init__(self, id_, class_code, lesson_id, scheme_of_work_id, department_id, institute_id, created = "", created_by_id = 0, created_by_name = "", published=STATE.PUBLISH, is_from_db=False, auth_user=None):
        #231: implement across all classes
        super().__init__(id_, class_code, created, created_by_id, created_by_name, published, is_from_db, ctx=auth_user)
        self.class_code = class_code
        self.lesson_id = int(lesson_id)
        self.scheme_of_work_id = int(scheme_of_work_id)
        self.department_id = department_id
        self.institute_id = institute_id
        

    @staticmethod
    def new(lesson_id, scheme_of_work_id, auth_ctx, fn_generate_class_code):
        new_class_code = fn_generate_class_code(length=6)
        return LessonScheduleModel(0, new_class_code, lesson_id=lesson_id, scheme_of_work_id=scheme_of_work_id, department_id=auth_ctx.department_id, institute_id=auth_ctx.institute_id, auth_user=auth_ctx)


    def validate(self, skip_validation = []):
        """ clean up and validate model """
        super().validate(skip_validation)

        # Validate class code
        self._validate_required_string("class_code", self.class_code, 6, 6)
        
        return self.is_valid


    def _clean_up(self):
        """ clean up properties by casting and ensuring safe for inserting etc """

        self.id = int(self.id)
    
        if self.class_code is not None:
            self.class_code = sql_safe(self.class_code)


    @staticmethod
    def get_model(db, lesson_id, scheme_of_work_id, auth_user):
        rows = LessonScheduleDataAccess.get_model(db, lesson_id, scheme_of_work_id, auth_user_id=auth_user.auth_user_id, show_published_state=auth_user.can_view)
        model = None
        for row in rows:
            model = LessonScheduleModel(
                id_=row[0],
                class_code = row[1],
                lesson_id = row[5],
                scheme_of_work_id=row[4],
                department_id=row[3],
                institute_id=row[2],
                published=row[6],
                auth_user=auth_user)
            model.on_fetched_from_db()
        return model


    @staticmethod
    def get_model_by_class_code(db, class_code, auth_user):
        rows = LessonScheduleDataAccess.get_model_by_class_code(db, class_code, auth_user_id=auth_user.auth_user_id, show_published_state=auth_user.can_view)
        model = None
        for row in rows:
            model = LessonScheduleModel(
                id_=row[0],
                class_code = row[1],
                lesson_id = row[5],
                scheme_of_work_id=row[4],
                department_id=row[3],
                institute_id=row[2],
                published=row[6],
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
    def delete(db, id_, lesson_id, scheme_of_work_id, auth_user):
        model = LessonScheduleModel(id_, "", lesson_id=lesson_id, scheme_of_work_id=scheme_of_work_id, department_id=auth_user.department_id, institute_id=auth_user.institute_id)
        LessonScheduleDataAccess._delete(db, auth_user_id=auth_user.auth_user_id, model=model)
        return model


class LessonScheduleDataAccess:

    @staticmethod
    def get_model(db, lesson_id, scheme_of_work_id, auth_user_id, show_published_state=STATE.PUBLISH):
        """
        get lesson schedule

        :param db:database context
        :param id_: the lesson identifier
        :param scheme_of_work_id: the scheme of work identifier
        :param auth_user_id: the user executing the command
        :return: the lesson
        """
        
        execHelper = ExecHelper()
        select_sql = "lesson_schedule__get"
        params = (lesson_id, int(show_published_state), auth_user_id)
        
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
        select_sql = "lesson_schedule__get_by_class_code"
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
        
        str_update = "lesson_schedule__update"
        params = (
            model.id,
            model.class_code,
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

        str_insert = "lesson_schedule__insert"
        params = (
            
            model.id,
            model.class_code,
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
    def _delete(db, auth_user_id, model):
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
