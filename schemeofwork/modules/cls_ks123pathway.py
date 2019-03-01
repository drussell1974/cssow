# -*- coding: utf-8 -*-
from basemodel import BaseModel
from db_helper import sql_safe

class KS123PathwayModel(BaseModel):
    def __init__(self, id_, objective):
        self.id = id_
        self.objective = objective
        self.is_checked = False


    def _clean_up(self):
        """ clean up properties by removing by casting and ensuring safe for inserting etc """

        # id
        self.id = int(self.id)

        # objective
        if self.objective is not None:
            self.objective = sql_safe(self.objective)

"""
DAL
"""

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

    select_sql = select_sql.format(learning_episode_id=int(learning_episode_id))

    rows = db.executesql(select_sql)

    data = [];

    for row in rows:
        data.append([int(row[0]), row[1]])

    return data
