# -*- coding: utf-8 -*-
from .core.basemodel import BaseModel
from .core.db_helper import ExecHelper, sql_safe
from .core.log import handle_log_info


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
    def get_options(db):
        return KeyStageDataAccess.get_options(db)
        

class KeyStageDataAccess:

    @staticmethod
    def get_options(db):
        
        #TODO: #230 Move to DataAccess
        BaseModel.depreciation_notice("use KeyStage.get_options()")

        execHelper = ExecHelper()

        rows = []
        rows = execHelper.execSql(db, "SELECT id, name FROM sow_key_stage;", rows, log_info=handle_log_info)

        data = []

        for row in rows:
            model = KeyStageModel(row[0], row[1])
            data.append(model)

        return data
