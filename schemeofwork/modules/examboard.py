# -*- coding: utf-8 -*-
from datetime import datetime
from gluon.contrib.appconfig import AppConfig

class ExamBoardModel:
    def __init__(this, id_, name):
        this.id = id_
        this.name = name
    id = 0
    name = ""


def get_options(db):

    rows = db.executesql("SELECT id, name FROM sow_exam_board;")

    data = [];

    for row in rows:
        model = ExamBoardModel(row[0], row[1])
        data.append(model)

    return data
