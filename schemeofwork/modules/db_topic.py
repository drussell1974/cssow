# -*- coding: utf-8 -*-
from cls_topic import TopicModel
from db_helper import to_db_null


def get_options(db, topic_id, lvl):

    str_select = "SELECT DISTINCT id, name, created, created_by FROM view_child_parent_topics WHERE lvl = {lvl} AND (id  = {topic_id} or parent_id = {topic_id} or related_topic_id = {topic_id});"
    str_select = str_select.format(lvl=lvl, topic_id=to_db_null(topic_id))

    data = [];

    try:

        rows = db.executesql(str_select)

        for row in rows:
            model = TopicModel(row[0], row[1], row[2], row[3])
            data.append(model)

    except Exception as e:
        #db_helper.last_sql = (str_select, "FAILED")
        raise Exception("Error getting topics", e)

    #db_helper.last_sql = (str_select, "SUCCESS")

    return data
