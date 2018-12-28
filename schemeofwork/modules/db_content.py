# -*- coding: utf-8 -*-

""" National Curriculum content """

from cls_content import ContentModel
import db_helper

def get_options(db, key_stage_id):

    str_select = "SELECT cnt.id as id, cnt.description as description FROM sow_content as cnt WHERE key_stage_id = %s;" % (key_stage_id)

    data = [];

    try:
        rows = db.executesql(str_select)


        for row in rows:
            model = ContentModel(row[0], row[1])
            data.append(model)
    except Exception as e:
        db_helper.last_sql = (str_select, "FAILED")
        raise Exception("Error getting content", e)

    db_helper.last_sql = (str_select, "SUCCESS")

    return data
