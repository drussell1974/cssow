# -*- coding: utf-8 -*-
from cls_keystage import KeyStageModel

def get_options(db):

    rows = db.executesql("SELECT id, name FROM sow_key_stage;")

    data = [];

    for row in rows:
        model = KeyStageModel(row[0], row[1])
        data.append(model)

    return data
