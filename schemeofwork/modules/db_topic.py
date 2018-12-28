# -*- coding: utf-8 -*-
from cls_topic import TopicModel
import db_helper


def get_options(db, topic_id='null', parent_topic_id='null', str_select = ""):

    str_select = "SELECT DISTINCT id, name, created, created_by FROM view_child_parent_topics WHERE id  = %s or parent_id = %s;" % (db_helper.to_db_null(topic_id), db_helper.to_db_null(parent_topic_id))

    data = [];

    try:

        rows = db.executesql(str_select)

        for row in rows:
            model = TopicModel(row[0], row[1], row[2], row[3])
            data.append(model)

    except Exception as e:
        db_helper.last_sql = (str_select, "FAILED")
        raise Exception("Error getting topics", e)

    db_helper.last_sql = (str_select, "SUCCESS")

    return data
