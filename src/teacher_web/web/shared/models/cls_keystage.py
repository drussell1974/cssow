# -*- coding: utf-8 -*-
from .core.basemodel import BaseModel
from .core.db_helper import ExecHelper, sql_safe
from shared.models.core.log_handlers import handle_log_info


class KeyStageModel(BaseModel):
    def __init__(self, id_, name):
        self.id = id_
        self.name = name


    def _clean_up(self):
        """ clean up properties by removing by casting and ensuring safe for inserting etc """

        # id
        self.id = int(self.id)

        # name
        if self.name is not None:
            self.name = sql_safe(self.name)


    @staticmethod
    def get_options(db, auth_user):
        
        rows = KeyStageDataAccess.get_options(db, auth_user)
        data = []

        for row in rows:
            model = KeyStageModel(row[0], row[1])
            data.append(model)

        return data


class KeyStageDataAccess:

    @staticmethod
    def get_options(db, auth_user):

        execHelper = ExecHelper()

        rows = []
        #271 Stored procedure (get_options)
        rows = execHelper.select(db, "keystage__get_options", (auth_user,), rows, handle_log_info)
        return rows
