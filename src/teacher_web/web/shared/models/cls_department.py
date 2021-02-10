from .core.basemodel import BaseModel
from .core.db_helper import ExecHelper, sql_safe
from shared.models.core.log_handlers import handle_log_info
from shared.models.core.basemodel import BaseModel

class DepartmentModel(BaseModel):

    name = ""
    
    def __init__(self, id_, name, institute_id = 0, created = "", created_by_id = 0, created_by_name = "", published=1, is_from_db=False):
        super().__init__(id_, name, created, created_by_id, created_by_name, published, is_from_db)
        #self.id = id_
        self.name = name
        self.institute_id = institute_id


    def validate(self, skip_validation = []):
        """ clean up and validate model """
        super().validate(skip_validation)

        # Validate name
        self._validate_required_string("name", self.name, 1, 70)

        self.on_after_validate()


    def _clean_up(self):
        """ clean up properties by removing by casting and ensuring safe for inserting etc """

        # id
        self.id = int(self.id)

        # name
        if self.name is not None:
            self.name = sql_safe(self.name)


    @staticmethod
    def get_options(db, auth_user):
        rows = DepartmentDataAccess.get_options(db, auth_user_id=auth_user.id)
        data = []
        
        for row in rows:
            model = DepartmentModel(row[0], row[1])
            data.append(model)
        return data


    @staticmethod
    def save(db, model, teacher_id, auth_user):
        """ save model """
        if model.published == 2:
            data = DepartmentDataAccess._delete(db, model, auth_user.id)
        elif model.is_valid == True:
            if model.is_new():
                data = DepartmentDataAccess._insert(db, model, teacher_id, auth_user_id=auth_user.id)
                model.id = data[0]
            else:
                data = DepartmentDataAccess._update(db, model, teacher_id, auth_user_id=auth_user.id)

        return model


class DepartmentDataAccess:
    
    @staticmethod
    def get_options(db, auth_user_id):
        
        execHelper = ExecHelper()

        str_select = "department__get_options"
        params = (auth_user_id,)

        try:
            rows = []
            rows = execHelper.select(db, str_select, params, rows, handle_log_info)
            
            return rows

        except Exception as e:
            raise Exception("Error getting departments", e)
        

    @staticmethod
    def _insert(db, model, teacher_id, auth_user_id):
        """ inserts the sow_department """
        execHelper = ExecHelper()

        sql_insert_statement = "department__insert"
        params = (
            model.id,
            model.name,
            teacher_id,
            model.institute_id,
            model.created,
            auth_user_id,
        )
               
        result = execHelper.insert(db, sql_insert_statement, params, handle_log_info)

        return result


    @staticmethod
    def _update(db, model, teacher_id, auth_user_id):
        """ updates the sow_department """
        
        execHelper = ExecHelper()
        
        str_update = "department__update"
        params = (
            model.id,
            model.name,
            teacher_id,
            auth_user_id
        )
        
        result = execHelper.update(db, str_update, params, handle_log_info)

        return result


    @staticmethod
    def _delete(db, model, auth_user_id):

        execHelper = ExecHelper()

        sql = "department__delete"
        params = (model.id, auth_user_id)
    
        #271 Stored procedure
        rows = execHelper.delete(db, sql, params, handle_log_info)
        
        return rows
