# -*- coding: utf-8 -*-
from basemodel import BaseModel
from db_helper import sql_safe

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
