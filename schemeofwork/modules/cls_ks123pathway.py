# -*- coding: utf-8 -*-
from basemodel import BaseModel
from db_helper import sql_safe

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
