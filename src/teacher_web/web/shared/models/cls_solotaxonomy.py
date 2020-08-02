# -*- coding: utf-8 -*-
from .core.basemodel import BaseModel
from .core.db_helper import ExecHelper, sql_safe
from .core.log import handle_log_info


class SoloTaxonomyModel(BaseModel):
    def __init__(self, id_, name, lvl):
        self.id = id_
        self.name = name
        self.lvl = lvl


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


class SoloTaxonomyDataAccess:

    @staticmethod
    def get_options(db):
    
        #TODO: #230 Move to DataAccess
        BaseModel.depreciation_notice("use SoloTaxonomyDataAccess.get_options()")

        execHelper = ExecHelper()
        
        rows = []
        rows = execHelper.execSql(db, "SELECT id, name, lvl FROM sow_solo_taxonomy;", rows, log_info=handle_log_info)

        data = []

        for row in rows:
            model = SoloTaxonomyModel(row[0], row[1], row[2])
            data.append(model)

        return data
