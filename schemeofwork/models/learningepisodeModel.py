# -*- coding: utf-8 -*-
from datetime import datetime
from gluon.contrib.appconfig import AppConfig
from basemodel import BaseModel

configuration = AppConfig(reload=True)

db = DAL(configuration.get('db.uri'),
     pool_size=configuration.get('db.pool_size'),
     migrate_enabled=configuration.get('db.migrate'),
     check_reserved=['all'])


class LearningEpisodeModel (BaseModel):

    order_of_delivery_id = 0
    scheme_of_work_id = 0
    scheme_of_work_name = ""
    topic_id = 0
    topic_name = ""
    parent_topic_id = 0
    parent_topic_name = ""
    key_stage_id = None

    def __init__(this, id_, order_of_delivery_id = 1, scheme_of_work_id = 0, scheme_of_work_name = "", topic_id = 0, topic_name = "", parent_topic_id = 0, parent_topic_name = "", key_stage_id = 0, created = "", created_by = ""):
        this.id = int(id_)
        this.order_of_delivery_id = int(order_of_delivery_id)
        this.scheme_of_work_id = int(scheme_of_work_id)
        this.scheme_of_work_name = scheme_of_work_name if scheme_of_work_id > 0 else ""
        this.topic_id = int(topic_id)
        this.topic_name = topic_name
        this.parent_topic_id = parent_topic_id
        this.parent_topic_name = parent_topic_name,
        this.key_stage_id = key_stage_id
        this.created = created
        this.created_by = created_by

    def validate(this):
        this.is_valid = True
        return True


    def _update(this):
        str_update = "UPDATE sow_learning_episode SET order_of_delivery_id = {}, scheme_of_work_id = {}, topic_id = {} WHERE id =  {};"
        str_update = str_update.format(this.order_of_delivery_id, this.scheme_of_work_id, this.topic_id, this.id)

        db.executesql(str_update)

        return True


    def _insert(this):
        str_insert = "INSERT INTO sow_learning_episode (order_of_delivery_id, scheme_of_work_id, topic_id, created, created_by) VALUES ({}, {}, {}, '{}', {});"
        str_insert = str_insert.format(this.order_of_delivery_id, this.scheme_of_work_id, this.topic_id, this.created, this.created_by)

        db.executesql(str_insert)

        return this.get_last_insert_row_id(db)


    def _delete(this):
        str_delete = "DELETE FROM sow_learning_episode WHERE id = {};"
        str_delete = str_delete.format(this.id)

        rval = db.executesql(str_delete)

        return rval


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
                 "  CONCAT_WS(' ', user.first_name, user.last_name) as created_by " + #10
                 " FROM sow_learning_episode as le " +
                 "  INNER JOIN sow_scheme_of_work as sow ON sow.id = le.scheme_of_work_id " +
                 "  LEFT JOIN sow_topic as top ON top.id = le.topic_id " +
                 "  LEFT JOIN sow_topic as pnt_top ON pnt_top.id = top.parent_id " +
                 "  LEFT JOIN auth_user as user ON user.id = sow.created_by " +
                 "  WHERE le.scheme_of_work_id = {} ORDER BY le.order_of_delivery_id;".format(scheme_of_work_id))

    rows = db.executesql(select_sql)

    data = [];

    for row in rows:
        model = LearningEpisodeModel(id_=row[0], order_of_delivery_id=row[1], scheme_of_work_id=row[2], scheme_of_work_name=row[3], topic_id=row[4], topic_name=row[5], parent_topic_id=row[6], parent_topic_name=row[7], key_stage_id=row[8], created=row[9], created_by=row[10])
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
                 "  CONCAT_WS(' ', user.first_name, user.last_name) as created_by " + #10
                 " FROM sow_learning_episode as le " +
                 "  INNER JOIN sow_scheme_of_work as sow ON sow.id = le.scheme_of_work_id " +
                 "  INNER JOIN sow_topic as top ON top.id = le.topic_id " +
                 "  LEFT JOIN sow_topic as pnt_top ON pnt_top.id = top.parent_id " +
                 "  LEFT JOIN auth_user as user ON user.id = sow.created_by " +
                  "  WHERE le.id = {};".format(id_))
    #raise Exception(select_sql)
    rows = db.executesql(select_sql)

    for row in rows:
        model = LearningEpisodeModel(id_=row[0], order_of_delivery_id=row[1], scheme_of_work_id=row[2], scheme_of_work_name=row[3], topic_id=row[4], topic_name=row[5], parent_topic_id=row[6], parent_topic_name=row[7], key_stage_id=row[8], created=row[9], created_by=row[10])

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
        created_by = auth_user_id
    )

    rval = model.validate()
    if model.is_valid == True:
        if model.is_new() == True:
            newId = model._insert()
            model.id = newId
        else:
            rval = model._update()

    return model


def delete(auth_user_id, id_):

    model = LearningEpisodeModel(id_)
    model._delete();
