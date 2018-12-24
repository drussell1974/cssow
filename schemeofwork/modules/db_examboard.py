# -*- coding: utf-8 -*-
from cls_examboard import ExamBoardModel

def get_options(db):

    rows = db.executesql("SELECT id, name FROM sow_exam_board;")

    data = [];

    for row in rows:
        model = ExamBoardModel(row[0], row[1])
        data.append(model)

    return data
