# -*- coding: utf-8 -*-
from gluon.contrib.appconfig import AppConfig
configuration = AppConfig(reload=True)
db = DAL(configuration.get('db.uri'),
     pool_size=configuration.get('db.pool_size'),
     migrate_enabled=configuration.get('db.migrate'),
     check_reserved=['all'])


from datetime import datetime
from cls_learningepisode import LearningEpisodeModel


def get_options(scheme_of_work_id):

    str_select = ("SELECT id, order_of_delivery_id FROM sow_learning_episode WHERE scheme_of_work_id = {};".format(scheme_of_work_id))
    rows = db.executesql(str_select)

    data = [];

    for row in rows:
        model = LearningEpisodeModel(row[0], row[1])
        data.append(model)

    return data


def get_all(scheme_of_work_id):

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


def get_model(id_):
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


def save(auth_user_id, id_, order_of_delivery_id, scheme_of_work_id, topic_id):

    # refresh model for validation
    model = LearningEpisodeModel(
        id_ = id_,
        order_of_delivery_id = order_of_delivery_id,
        scheme_of_work_id = scheme_of_work_id,
        scheme_of_work_name = "",
        topic_id = topic_id,
        topic_name = "",
        created = datetime.now(),
        created_by_id = auth_user_id
    )

    rval = model.validate()
    if model.is_valid == True:
        if model.is_new() == True:
            newId = _insert(model)
            model.id = newId
        else:
            rval = _update(model)

    return model


def delete(auth_user_id, id_):

    model = LearningEpisodeModel(id_)
    _delete(model);

"""
Private CRUD functions 
"""

def _update(model):
    str_update = "UPDATE sow_learning_episode SET order_of_delivery_id = {}, scheme_of_work_id = {}, topic_id = {} WHERE id =  {};"
    str_update = str_update.format(model.order_of_delivery_id, model.scheme_of_work_id, model.topic_id, model.id)

    db.executesql(str_update)

    return True


def _insert(model):
    str_insert = "INSERT INTO sow_learning_episode (order_of_delivery_id, scheme_of_work_id, topic_id, created, created_by) VALUES ({}, {}, {}, '{}', {});"
    str_insert = str_insert.format(model.order_of_delivery_id, model.scheme_of_work_id, model.topic_id, model.created, model.created_by)

    db.executesql(str_insert)

    return _get_last_insert_row_id(model)


def _delete(model, db):
    str_delete = "DELETE FROM sow_learning_episode WHERE id = {};"
    str_delete = str_delete.format(model.id)

    rval = db.executesql(str_delete)

    return rval


def _get_last_insert_row_id(model):
        # get last inserted row id
        rows = db.executesql("SELECT LAST_INSERT_ID();")

        rval = None # Should not be zero (handle has necessary)
        for row in rows:
            model.id = int(row[0])

        return model.id
