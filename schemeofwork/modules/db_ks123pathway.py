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


def get_linked_pathway_ks123(db, learning_episode_id):

    select_sql = "SELECT"\
                 " pw.id as id,"\
                 " pw.objective as objective "\
                 "FROM sow_learning_episode__has__ks123_pathway as le_pw" \
                 " INNER JOIN sow_ks123_pathway AS pw ON pw.id = le_pw.ks123_pathway_id"\
                 " WHERE le_pw.learning_episode_id = {learning_episode_id};"

    select_sql = select_sql.format(learning_episode_id=learning_episode_id)

    rows = db.executesql(select_sql)

    data = [];

    for row in rows:
        data.append([int(row[0]), row[1]])

    return data
