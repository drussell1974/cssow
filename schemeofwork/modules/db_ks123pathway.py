# -*- coding: utf-8 -*-
from cls_ks123pathway import KS123PathwayModel

def get_options(db, year_id, topic_id):

    str_select = "SELECT id, objective FROM sow_ks123_pathway WHERE year_id = {year_id} and topic_id = {topic_id};"\
        .format(year_id=year_id, topic_id=topic_id)

    rows = db.executesql(str_select)

    data = [];

    for row in rows:
        model = KS123PathwayModel(row[0], row[1])
        data.append(model)

    return data


def get_pathway_ks123_ids(db, learning_episode_id):

    select_sql = "SELECT"\
                 " pw.ks123_pathway_id as ks123_pathway_id"\
                 " FROM sow_learning_episode__has__ks123_pathway as pw"\
                 " WHERE pw.learning_episode_id = {learning_episode_id};"

    select_sql = select_sql.format(learning_episode_id=learning_episode_id)

    rows = db.executesql(select_sql)

    data = [];

    for row in rows:
        data.append(int(row[0]))

    return data
