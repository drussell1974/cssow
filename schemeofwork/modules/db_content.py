# -*- coding: utf-8 -*-
from cls_content import ContentModel

def get_options(db, key_stage_id):

    rows = db.executesql("SELECT id, description FROM sow_content WHERE key_stage_id = {};".format(key_stage_id))

    data = [];

    for row in rows:
        model = ContentModel(row[0], row[1])
        data.append(model)

    return data
