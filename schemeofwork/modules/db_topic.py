# -*- coding: utf-8 -*-
from cls_topic import TopicModel
from db_helper import last_sql, sql_safe

def get_options(db, lvl, topic_id = 0):

    str_select = "SELECT id, name, created, created_by FROM sow_topic WHERE lvl = {lvl} and parent_id = {topic_id};"
    str_select = str_select.format(lvl=sql_safe(lvl), topic_id=int(topic_id))

    data = [];

    try:

        rows = db.executesql(str_select)

        for row in rows:
            model = TopicModel(row[0], row[1], row[2], row[3])
            data.append(model)

    except Exception as e:
        raise Exception("Error getting topics", e)


    return data
