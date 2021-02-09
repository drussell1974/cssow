# -*- coding: utf-8 -*-
from .core.basemodel import BaseModel
from .core.db_helper import ExecHelper, sql_safe
from shared.models.core.log_handlers import handle_log_info


class KS123PathwayModel(BaseModel):
    def __init__(self, id_, objective):
        self.id = id_
        self.objective = objective
        self.is_checked = False


    def _clean_up(self):
        """ clean up properties by removing by casting and ensuring safe for inserting etc """

        # id
        self.id = int(self.id)

        # objective
        if self.objective is not None:
            self.objective = sql_safe(self.objective)
    
    
    @staticmethod
    def get_options(db, year_id, topic_id, auth_user):
        rows = KS123PathwayDataAccess.get_options(db, year_id, topic_id, auth_user_id=auth_user.id)
        data = []
        for row in rows:
            model = KS123PathwayModel(row[0], row[1])
            data.append(model)
        return data


    @staticmethod
    def get_linked_pathway_ks123(db, lesson_id, auth_user):
        rows = KS123PathwayDataAccess.get_linked_pathway_ks123(db, lesson_id, auth_user_id=auth_user.id)
        data = []
        for row in rows:
            data.append([int(row[0]), row[1]])
        return data


class KS123PathwayDataAccess:

    @staticmethod
    def get_options(db, year_id, topic_id, auth_user_id):

        execHelper = ExecHelper()

        str_select = "ks123_pathway__get_options"
        params = (year_id, topic_id, auth_user_id)

        rows = []

        #271 Stored procedure (get_options)
        rows = execHelper.select(db, str_select, params, rows, handle_log_info)

        return rows


    @staticmethod
    def get_linked_pathway_ks123(db, lesson_id, auth_user_id):

        execHelper = ExecHelper()
        

        select_sql = "ks123_pathway__get_linked_pathway"

        params = (lesson_id, auth_user_id)

        rows = []
        #271 Stored procedure
        rows = execHelper.select(db, select_sql, params, rows, handle_log_info)
        return rows
