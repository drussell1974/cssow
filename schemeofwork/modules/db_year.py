# -*- coding: utf-8 -*-
from cls_year import YearModel

def get_options(db, key_stage_id):

    str_select = "SELECT id, name FROM sow_year WHERE key_stage_id = {key_stage_id};".format(key_stage_id=int(key_stage_id))
    rows = db.executesql(str_select)

    data = [];

    for row in rows:
        model = YearModel(row[0], row[1])
        data.append(model)

    return data
