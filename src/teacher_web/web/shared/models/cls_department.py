# -*- coding: utf-8 -*-
from .core.basemodel import BaseModel
from .core.db_helper import ExecHelper, sql_safe
from .core.log import handle_log_info
from shared.models.core.basemodel import BaseModel
from shared.models.cls_teacher_permission import TeacherPermissionModel

class DepartmentModel(BaseModel):

    name = ""
    
    def __init__(self, id_, name, school_id = 0, created = "", created_by_id = 0, created_by_name = "", published=1, is_from_db=False):
        super().__init__(id_, name, created, created_by_id, created_by_name, published, is_from_db)
        #self.id = id_
        self.name = name
        self.school_id = school_id


    def validate(self, skip_validation = []):
        """ clean up and validate model """
        super().validate(skip_validation)

        # Validate name
        self._validate_required_string("name", self.name, 1, 70)


    def _clean_up(self):
        """ clean up properties by removing by casting and ensuring safe for inserting etc """

        # id
        self.id = int(self.id)

        # name
        if self.name is not None:
            self.name = sql_safe(self.name)


    @staticmethod
    def get_options(db, auth_user):
        rows = DepartmentDataAccess.get_options(db, auth_user)
        data = []
        
        for row in rows:
            model = DepartmentModel(row[0], row[1])
            data.append(model)
        return data


    @staticmethod
    def save(db, model, teacher_id, auth_user):
        """ save model """
        if model.published == 2:
            data = DepartmentDataAccess._delete(db, model.id, auth_user)
        else:
            if model.is_new():
                data = DepartmentDataAccess._insert(db, model, teacher_id, auth_user)
                model.id = data[0]
            else:
                data = DepartmentDataAccess._update(db, model, teacher_id, auth_user)
    
        return model


class DepartmentDataAccess:
    
    @staticmethod
    def get_options(db, user_auth):
        
        execHelper = ExecHelper()

        str_select = "department__get_options"
        params = (user_auth,)

        try:
            rows = []
            rows = execHelper.select(db, str_select, params, rows, handle_log_info)
            
            return rows

        except Exception as e:
            raise Exception("Error getting departments", e)
        

    @staticmethod
    def _insert(db, model, teacher_id, auth_user):
        """ inserts the sow_department """
        execHelper = ExecHelper()

        sql_insert_statement = "department__insert"
        params = (
            model.id,
            model.name,
            teacher_id,
            model.school_id,
            model.created,
            auth_user,
        )
               
        result = execHelper.insert(db, sql_insert_statement, params, handle_log_info)

        return result


    @staticmethod
    def _update(db, model, teacher_id, auth_user):
        """ updates the sow_department """
        
        execHelper = ExecHelper()
        
        str_update = "department__update"
        params = (
            model.id,
            model.name,
            teacher_id,
            auth_user
        )
        
        result = execHelper.update(db, str_update, params, handle_log_info)

        return result


    @staticmethod
    def _delete(db, model, auth_user):

        execHelper = ExecHelper()

        sql = "lesson_resource__delete"
        params = (model.id, auth_user)
    
        #271 Stored procedure
        rows = execHelper.delete(db, sql, params, handle_log_info)
        
        return rows
