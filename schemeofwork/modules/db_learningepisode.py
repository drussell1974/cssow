# -*- coding: utf-8 -*-
from cls_learningepisode import LearningEpisodeModel

def get_options(db, scheme_of_work_id):

    str_select = ("SELECT id, order_of_delivery_id FROM sow_learning_episode WHERE scheme_of_work_id = {} ORDER BY order_of_delivery_id;".format(scheme_of_work_id))
    rows = db.executesql(str_select)

    data = [];

    for row in rows:
        model = LearningEpisodeModel(row[0], row[1])
        data.append(model)

    return data


def get_all(db, scheme_of_work_id):

    select_sql = ("SELECT " +
                 "  le.id as id, " + #0
                 "  le.order_of_delivery_id as order_of_delivery_id, " #1
                 "  le.scheme_of_work_id as scheme_of_work_id, " + #2
                 "  sow.name as scheme_of_work_name, " + #3
                 "  top.id as topic_id, " + #4
                 "  top.name as topic_name, " + #5
                 "  pnt_top.id as parent_topic_id, " + #6
                 "  pnt_top.name as parent_topic_name, " + #7
                 "  sow.key_stage_id as key_stage_id, " + #8
                 "  le.created as created, " + #9
                 "  le.created_by as created_by_id, " + #10
                 "  CONCAT_WS(' ', user.first_name, user.last_name) as created_by_name " + #11
                 " FROM sow_learning_episode as le " +
                 "  INNER JOIN sow_scheme_of_work as sow ON sow.id = le.scheme_of_work_id " +
                 "  LEFT JOIN sow_topic as top ON top.id = le.topic_id " +
                 "  LEFT JOIN sow_topic as pnt_top ON pnt_top.id = top.parent_id " +
                 "  LEFT JOIN auth_user as user ON user.id = sow.created_by " +
                 "  WHERE le.scheme_of_work_id = {} ORDER BY le.order_of_delivery_id;".format(scheme_of_work_id))

    rows = db.executesql(select_sql)

    data = [];

    for row in rows:
        model = LearningEpisodeModel(id_=row[0], order_of_delivery_id=row[1], scheme_of_work_id=row[2], scheme_of_work_name=row[3], topic_id=row[4], topic_name=row[5], parent_topic_id=row[6], parent_topic_name=row[7], key_stage_id=row[8], created=row[9], created_by_id=row[10], created_by_name=row[11])
        data.append(model)

    return data


def get_model(db, id_):
    model = LearningEpisodeModel(id_);

    select_sql = ("SELECT " +
                  "  le.id as id, " + #0
                 "  le.order_of_delivery_id as order_of_delivery_id, " #1
                 "  le.scheme_of_work_id as scheme_of_work_id, " + #2
                 "  sow.name as scheme_of_work_name, " + #3
                 "  top.id as topic_id, " + #4
                 "  top.name as topic_name, " + #5
                 "  pnt_top.id as parent_topic_id, " + #6
                 "  pnt_top.name as parent_topic_name, " + #7
                 "  sow.key_stage_id as key_stage_id, " + #8
                 "  le.created as created, " + #9
                 "  le.created_by as created_by_id, " + #10
                 "  CONCAT_WS(' ', user.first_name, user.last_name) as created_by_name " + #11
                 " FROM sow_learning_episode as le " +
                 "  INNER JOIN sow_scheme_of_work as sow ON sow.id = le.scheme_of_work_id " +
                 "  INNER JOIN sow_topic as top ON top.id = le.topic_id " +
                 "  LEFT JOIN sow_topic as pnt_top ON pnt_top.id = top.parent_id " +
                 "  LEFT JOIN auth_user as user ON user.id = sow.created_by " +
                  "  WHERE le.id = {};".format(id_))

    rows = db.executesql(select_sql)

    for row in rows:
        model = LearningEpisodeModel(id_=row[0], order_of_delivery_id=row[1], scheme_of_work_id=row[2], scheme_of_work_name=row[3], topic_id=row[4], topic_name=row[5], parent_topic_id=row[6], parent_topic_name=row[7], key_stage_id=row[8], created=row[9], created_by_id=row[10], created_by_name=row[11])

    return model


def save(db, model):
    if model.is_new() == True:
        model.id = _insert(db, model)
    else:
        _update(db, model)

    return model


def delete(db, auth_user_id, id_):

    model = LearningEpisodeModel(id_)
    _delete(db, model);

"""
Private CRUD functions 
"""

def _update(db, model):
    str_update = "UPDATE sow_learning_episode SET order_of_delivery_id = {}, scheme_of_work_id = {}, topic_id = {} WHERE id =  {};"
    str_update = str_update.format(model.order_of_delivery_id, model.scheme_of_work_id, model.topic_id, model.id)

    db.executesql(str_update)

    return True


def _insert(db, model):
    str_insert = "INSERT INTO sow_learning_episode (order_of_delivery_id, scheme_of_work_id, topic_id, created, created_by) VALUES ({}, {}, {}, '{}', {});"
    str_insert = str_insert.format(model.order_of_delivery_id, model.scheme_of_work_id, model.topic_id, model.created, model.created_by_id)

    db.executesql(str_insert)

    # get last inserted row id

    rows = db.executesql("SELECT LAST_INSERT_ID();")

    for row in rows:
        model.id = int(row[0])

    return model.id


def _delete(db, model):
    str_delete = "DELETE FROM sow_learning_episode WHERE id = {};"
    str_delete = str_delete.format(model.id)

    rval = db.executesql(str_delete)

    return rval

