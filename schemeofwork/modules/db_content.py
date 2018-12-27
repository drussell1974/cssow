# -*- coding: utf-8 -*-

""" National Curriculum content """

from cls_content import ContentModel

def get_options(db, key_stage_id):

    str_select = " SELECT cnt.id as id, cnt.description as description FROM sow_content as cnt WHERE key_stage_id = %s " % (key_stage_id)

    rows = db.executesql(str_select)

    data = [];

    for row in rows:
        model = ContentModel(row[0], row[1])
        data.append(model)

    return data
