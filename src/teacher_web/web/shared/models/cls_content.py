# -*- coding: utf-8 -*-
from .core.basemodel import BaseModel
from .core.db_helper import ExecHelper, sql_safe
from .core.log import handle_log_info


class ContentModel(BaseModel):
    def __init__(self, id_, description):
        self.id = id_
        self.description = description


    def _clean_up(self):
        """ clean up properties by removing by casting and ensuring safe for inserting etc """

        # id
        self.id = int(self.id)

        # trim description
        if self.description is not None:
            self.description = sql_safe(self.description)


class ContentDataAccess:

    @staticmethod
    def get_options(db, key_stage_id):

        #TODO: #230 Move to DataAccess
        BaseModel.depreciation_notice("use ContentDataAccess.get_options()")
        execHelper = ExecHelper()

        str_select = "SELECT cnt.id as id, cnt.description as description FROM sow_content as cnt WHERE key_stage_id = {};".format(int(key_stage_id))

        data = []

        try:
            rows = []
            rows = execHelper.execSql(db, str_select, rows, handle_log_info)

            for row in rows:
                model = ContentModel(row[0], row[1])
                data.append(model)
        except Exception as e:
            last_sql = (str_select, "FAILED")
            raise Exception("Error getting content", e)

        last_sql = (str_select, "SUCCESS")

        return data
