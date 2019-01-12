# -*- coding: utf-8 -*-
from cls_learningepisode import LearningEpisodeModel
from db_helper import to_db_null

def get_options(db, scheme_of_work_id, auth_user):

    str_select = "SELECT id, order_of_delivery_id FROM sow_learning_episode WHERE scheme_of_work_id = {scheme_of_work_id} AND (published = 1 OR created_by = {auth_user}) ORDER BY order_of_delivery_id;"
    str_select = str_select.format(scheme_of_work_id=scheme_of_work_id, auth_user=to_db_null(auth_user))

    rows = db.executesql(str_select)

    data = [];

    for row in rows:
        model = LearningEpisodeModel(row[0], row[1])
        data.append(model)

    return data


def get_all(db, scheme_of_work_id, auth_user):

    select_sql = "SELECT "\
                 " le.id as id,"\
                 " le.order_of_delivery_id as order_of_delivery_id,"\
                 " le.scheme_of_work_id as scheme_of_work_id,"\
                 " sow.name as scheme_of_work_name,"\
                 " top.id as topic_id," \
                 " top.name as topic_name," \
                 " pnt_top.id as parent_topic_id,"\
                 " pnt_top.name as parent_topic_name,"\
                 " sow.key_stage_id as key_stage_id,"\
                 " le.key_words as key_words,"\
                 " le.summary as summary,"\
                 " le.created as created,"\
                 " le.created_by as created_by_id,"\
                 " CONCAT_WS(' ', user.first_name, user.last_name) as created_by_name"\
                 " FROM sow_learning_episode as le "\
                 " INNER JOIN sow_scheme_of_work as sow ON sow.id = le.scheme_of_work_id "\
                 " LEFT JOIN sow_topic as top ON top.id = le.topic_id "\
                 " LEFT JOIN sow_topic as pnt_top ON pnt_top.id = top.parent_id "\
                 " LEFT JOIN auth_user as user ON user.id = sow.created_by "\
                 " WHERE le.scheme_of_work_id = {scheme_of_work_id} AND (le.published = 1 OR le.created_by = {auth_user}) ORDER BY le.order_of_delivery_id;"
    select_sql = select_sql.format(scheme_of_work_id=scheme_of_work_id, auth_user=to_db_null(auth_user))

    rows = db.executesql(select_sql)

    data = [];

    for row in rows:
        model = LearningEpisodeModel(id_=row[0], order_of_delivery_id=row[1], scheme_of_work_id=row[2], scheme_of_work_name=row[3], topic_id=row[4], topic_name=row[5], parent_topic_id=row[6], parent_topic_name=row[7], key_stage_id=row[8], key_words = row[9], summary = row[10], created=row[11], created_by_id=row[12], created_by_name=row[13])
        data.append(model)

    return data


def get_model(db, id_, auth_user):
    model = LearningEpisodeModel(id_);

    select_sql = "SELECT "\
                  " le.id as id,"\
                 " le.order_of_delivery_id as order_of_delivery_id,"\
                 " le.scheme_of_work_id as scheme_of_work_id,"\
                 " sow.name as scheme_of_work_name,"\
                 " top.id as topic_id,"\
                 " top.name as topic_name,"\
                 " pnt_top.id as parent_topic_id,"\
                 " pnt_top.name as parent_topic_name,"\
                 " sow.key_stage_id as key_stage_id,"\
                 " le.key_words as key_words,"\
                 " le.summary as summary,"\
                 " le.created as created,"\
                 " le.created_by as created_by_id,"\
                 " CONCAT_WS(' ', user.first_name, user.last_name) as created_by_name"\
                 " FROM sow_learning_episode as le"\
                 " INNER JOIN sow_scheme_of_work as sow ON sow.id = le.scheme_of_work_id"\
                 " INNER JOIN sow_topic as top ON top.id = le.topic_id"\
                 " LEFT JOIN sow_topic as pnt_top ON pnt_top.id = top.parent_id"\
                 " LEFT JOIN auth_user as user ON user.id = sow.created_by"\
                  " WHERE le.id = {learning_episode_id} AND (le.published = 1 OR le.created_by = {auth_user});"
    select_sql = select_sql.format(learning_episode_id=id_, auth_user=to_db_null(auth_user))

    rows = db.executesql(select_sql)

    for row in rows:
        model = LearningEpisodeModel(id_=row[0], order_of_delivery_id=row[1], scheme_of_work_id=row[2], scheme_of_work_name=row[3], topic_id=row[4], topic_name=row[5], parent_topic_id=row[6], parent_topic_name=row[7], key_stage_id=row[8], key_words = row[9], summary = row[10], created=row[11], created_by_id=row[12], created_by_name=row[13])

    return model


def save(db, model, published=1):
    if model.is_new() == True:
        model.id = _insert(db, model, published)
    else:
        _update(db, model, published)

    return model


def delete(db, auth_user_id, id_):

    model = LearningEpisodeModel(id_)
    _delete(db, model);

"""
Private CRUD functions 
"""

def _update(db, model, published):
    str_update = "UPDATE sow_learning_episode SET order_of_delivery_id = {order_of_delivery_id}, scheme_of_work_id = {scheme_of_work_id}, topic_id = {topic_id}, key_words = '{key_words}', summary = '{summary}', published = {published} WHERE id =  {learning_episode_id};"
    str_update = str_update.format(
        order_of_delivery_id=model.order_of_delivery_id,
        scheme_of_work_id=model.scheme_of_work_id,
        topic_id=model.topic_id,
        key_words=to_db_null(model.key_words),
        summary=to_db_null(model.summary),
        published=published,
        learning_episode_id=model.id)

    db.executesql(str_update)

    return True


def _insert(db, model, published):
    str_insert = "INSERT INTO sow_learning_episode (order_of_delivery_id, scheme_of_work_id, topic_id, key_words, summary, created, created_by, published) VALUES ({order_of_delivery_id}, {scheme_of_work_id}, {topic_id}, '{key_words}', '{summary}', '{created}', {created_by}, {published});"
    str_insert = str_insert.format(
        order_of_delivery_id=model.order_of_delivery_id,
        scheme_of_work_id=model.scheme_of_work_id,
        topic_id=model.topic_id,
        key_words=to_db_null(model.key_words),
        summary=to_db_null(model.summary),
        created=model.created,
        created_by=model.created_by_id,
        published=published)

    db.executesql(str_insert)

    # get last inserted row id

    rows = db.executesql("SELECT LAST_INSERT_ID();")

    for row in rows:
        model.id = int(row[0])

    return model.id


def _delete(db, model):
    str_delete = "DELETE FROM sow_learning_episode WHERE id = {learning_episode_id};"
    str_delete = str_delete.format(learning_episode_id=model.id)

    rval = db.executesql(str_delete)

    return rval

