# -*- coding: utf-8 -*-
from basemodel import BaseModel
from db_helper import sql_safe

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

"""
DAL
"""

def get_options(db):

    rows = db.executesql("SELECT id, name, lvl FROM sow_solo_taxonomy;")

    data = []

    for row in rows:
        model = SoloTaxonomyModel(row[0], row[1], row[2])
        data.append(model)

    return data
