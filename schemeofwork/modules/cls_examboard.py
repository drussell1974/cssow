# -*- coding: utf-8 -*-
from basemodel import BaseModel
from db_helper import sql_safe

class ExamBoardModel(BaseModel):
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

"""
DAL
"""

def get_options(db):

    rows = db.executesql("SELECT id, name FROM sow_exam_board;")

    data = [];

    for row in rows:
        model = ExamBoardModel(row[0], row[1])
        data.append(model)

    return data
