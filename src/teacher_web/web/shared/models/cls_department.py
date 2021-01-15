# -*- coding: utf-8 -*-
from .core.basemodel import BaseModel
from .core.db_helper import ExecHelper, sql_safe
from .core.log import handle_log_info
from shared.models.core.basemodel import BaseModel


class DepartmentModel(BaseModel):

    name = ""
    
    def __init__(self, id_, name, created = "", created_by = ""):
        self.id = id_
        self.name = name
        self.created = created
        self.created_by = created_by


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
