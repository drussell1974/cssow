# -*- coding: utf-8 -*-
from .core.basemodel import BaseModel
from .core.db_helper import ExecHelper, sql_safe
from shared.models.core.log_handlers import handle_log_info


class SoloTaxonomyModel(BaseModel):

    learning_objectives = []

    def __init__(self, id_, name, lvl):
        self.id = id_
        self.name = name
        self.lvl = lvl
        self.learning_objectives = []


    def _clean_up(self):
        """ clean up properties by removing by casting and ensuring safe for inserting etc """

        # id
        self.id = int(self.id)

        # name
        if self.name is not None:
            self.name = sql_safe(self.name)

        # lvl
        if self.lvl is not None:
            self.lvl = sql_safe(self.lvl)


    @staticmethod
    def get_options(db, auth_user):
        rows = SoloTaxonomyDataAccess.get_options(db, auth_user)
        data = []
        for row in rows:
            model = SoloTaxonomyModel(row[0], row[1], row[2])
            data.append(model)
        return data


class SoloTaxonomyDataAccess:

    @staticmethod
    def get_options(db, auth_user):
    
        execHelper = ExecHelper()
        
        rows = []
        #271 Stored procedure (get_options)
        rows = execHelper.select(db, "solotaxonomy__get_options", (auth_user,), rows, handle_log_info)
        return rows
