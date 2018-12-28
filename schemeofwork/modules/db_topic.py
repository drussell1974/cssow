# -*- coding: utf-8 -*-
from cls_topic import TopicModel

def get_options(db, topic_id = 0, parent_topic_id = 0):

    str_select = "SELECT DISTINCT id, name, created, created_by FROM view_child_parent_topics WHERE id  = %s or parent_id = %s" % (topic_id, parent_topic_id)

    rows = db.executesql(str_select)

    data = [];

    for row in rows:
        model = TopicModel(row[0], row[1], row[2], row[3])
        data.append(model)

    return data
