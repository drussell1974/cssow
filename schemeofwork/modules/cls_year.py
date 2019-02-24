# -*- coding: utf-8 -*-
from basemodel import BaseModel
from db_helper import sql_safe


class YearModel(BaseModel):
    def __init__(this, id_, name):
        this.id = id_
        this.name = name


    def _clean_up(self):
        """ clean up properties by removing by casting and ensuring safe for inserting etc """

        # id
        self.id = int(self.id)

        # name
        if self.name is not None:
            self.name = sql_safe(self.name)
