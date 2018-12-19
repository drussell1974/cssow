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

    scheme_of_work_id = 0
    order_of_delivery_id = 0

    def __init__(this, id_, order_of_delivery_id = 1, scheme_of_work_id = 0, scheme_of_work_name = "", created = "", created_by = ""):
        this.id = int(id_)
        this.order_of_delivery_id = int(order_of_delivery_id)
        this.scheme_of_work_id = int(scheme_of_work_id)
        this.scheme_of_work_name = scheme_of_work_name if scheme_of_work_id > 0 else ""
        this.created = created
        this.created_by = created_by

    def validate(this):
        this.is_valid = True
        return True


    def _update(this):
        str_update = "UPDATE sow_learning_episode SET order_of_delivery_id = {}, scheme_of_work_id = {} WHERE id =  {};"
        str_update = str_update.format(this.order_of_delivery_id, this.scheme_of_work_id, this.id)

        db.executesql(str_update)

        return True


    def _insert(this):
        str_insert = "INSERT INTO sow_learning_episode (order_of_delivery_id, scheme_of_work_id, created, created_by) VALUES ({}, {}, '{}', {});"
        str_insert = str_insert.format(this.order_of_delivery_id, this.scheme_of_work_id, this.created, this.created_by)

        return get_last_insert_id(db)


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


def get_order_of_delivery_name_only(learning_episode_id):

    select_sql = ("SELECT le.order_of_delivery_id as order_of_delivery_name FROM sow_learning_episode as le WHERE le.id = {};".format(learning_episode_id))

    rows = db.executesql(select_sql)

    order_of_delivery_name = "";

    for row in rows:
        order_of_delivery_name = row[0]

    return order_of_delivery_name


def get_all():

    scheme_of_work_id = int(request.vars.scheme_of_work_id)

    select_sql = ("SELECT " +
                 "  le.id as id, " + #0
                 "  le.order_of_delivery_id as order_of_delivery_id, " #1
                 "  le.scheme_of_work_id as scheme_of_work_id, " + #2
                 "  sow.name as scheme_of_work_name, " + #3
                 "  le.created as created, " + #4
                 "  CONCAT_WS(' ', user.first_name, user.last_name) as created_by " + #5
                 " FROM sow_learning_episode as le " +
                 "  INNER JOIN sow_scheme_of_work as sow ON sow.id = le.scheme_of_work_id " +
                 "  LEFT JOIN auth_user as user ON user.id = sow.created_by " +
                 "  WHERE le.scheme_of_work_id = {} ORDER BY le.order_of_delivery_id;".format(scheme_of_work_id))

    rows = db.executesql(select_sql)

    data = [];

    for row in rows:
        model = LearningEpisodeModel(row[0], row[1], row[2], row[3], row[4], row[5])
        data.append(model)

    return data


def get_model():
    id_ = int(request.vars.id if request.vars.id is not None else 0)
    model = LearningEpisodeModel(id_);

    select_sql = ("SELECT " +
                 "  le.id as id, " + #0
                 "  le.order_of_delivery_id as order_of_delivery_id, " #1
                 "  le.scheme_of_work_id as scheme_of_work_id, " + #2
                 "  sow.name as scheme_of_work_name, " + #3
                 "  le.created as created, " + #4
                 "  CONCAT_WS(' ', user.first_name, user.last_name) as created_by " + #5
                 " FROM sow_learning_episode as le " +
                 "  INNER JOIN sow_scheme_of_work as sow ON sow.id = le.scheme_of_work_id " +
                 "  LEFT JOIN auth_user as user ON user.id = sow.created_by " +
                  "  WHERE le.id = {};".format(id_))

    rows = db.executesql(select_sql)

    for row in rows:
        model = LearningEpisodeModel(row[0], row[1], row[2], row[3], row[4], row[5])

    return model


def save(auth_user_id):

    # refresh model for validation
    model = LearningEpisodeModel(
        id_ = request.vars.id,
        order_of_delivery_id = request.vars.order_of_delivery_id,
        scheme_of_work_id = request.vars.scheme_of_work_id,
        scheme_of_work_name = request.vars.scheme_of_work_name,
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


def delete(auth_user_id):

    id_ = int(request.vars.id)

    model = LearningEpisodeModel(id_)
    model._delete();
