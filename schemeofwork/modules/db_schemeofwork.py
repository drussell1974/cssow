# -*- coding: utf-8 -*-
from cls_schemeofwork import SchemeOfWorkModel
from db_helper import to_db_null

def get_options(db, auth_user = 0):
    str_select = "SELECT sow.id, sow.name, ks.name as key_stage_name FROM sow_scheme_of_work as sow LEFT JOIN sow_key_stage as ks ON ks.id = sow.key_stage_id WHERE sow.published = 1 OR sow.created_by = {auth_user} ORDER BY sow.key_stage_id;"
    str_select = str_select.format(auth_user=to_db_null(auth_user))
    rows = db.executesql(str_select)

    data = [];

    for row in rows:
        model = SchemeOfWorkModel(id_ = row[0], name = row[1], key_stage_name = row[2])
        data.append(model)

    return data


def get_all(db, key_stage_id=0, auth_user = 0):
    select_sql = "SELECT "\
                  "  sow.id as id, "\
                  "  sow.name as name, "\
                  "  sow.description as description, "\
                  "  sow.exam_board_id as exam_board_id, "\
                  "  exam.name as exam_board_name, "\
                  "  sow.key_stage_id as key_stage_id, "\
                  "  kys.name as key_stage_name, "\
                  "  sow.created as created, "\
                  "  sow.created_by as created_by_id,"\
                  "  CONCAT_WS(' ', user.first_name, user.last_name) as created_by_name, "\
                  "  sow.published as published"\
                  " FROM sow_scheme_of_work as sow "\
                  "  LEFT JOIN sow_exam_board as exam ON exam.id = sow.exam_board_id "\
                  "  INNER JOIN sow_key_stage as kys ON kys.id = sow.key_stage_id "\
                  "  LEFT JOIN auth_user as user ON user.id = sow.created_by "\
                  " WHERE (sow.key_stage_id = {key_stage_id} or {key_stage_id} = 0) AND (sow.published = 1 OR sow.created_by = {auth_user});"
    select_sql = select_sql.format(key_stage_id=key_stage_id, auth_user=to_db_null(auth_user))

    rows = db.executesql(select_sql)

    data = [];

    for row in rows:

        model = SchemeOfWorkModel(id_=row[0],
                                  name=row[1],
                                  description=row[2],
                                  exam_board_id=row[3],
                                  exam_board_name=row[4],
                                  key_stage_id=row[5],
                                  key_stage_name=row[6],
                                  created=row[7],
                                  created_by_id=row[8],
                                  created_by_name=row[9],
                                  published=row[10])

        model.set_is_recent()

        data.append(model)

    return data

def get_latest_schemes_of_work(db, top = 5, auth_user = 0):
    """
    Gets the latest schemes of work with learning objectives
    :param db: the database context
    :param top: number of records to return
    :return: list of schemes of work models
    """
    select_sql = "SELECT DISTINCT "\
                 " sow.id as id," \
                 " sow.name as name," \
                 " sow.description as description," \
                 " sow.exam_board_id as exam_board_id," \
                 " exam.name as exam_board_name," \
                 " sow.key_stage_id as key_stage_id," \
                 " kys.name as key_stage_name," \
                 " sow.created as created," \
                 " sow.created_by as created_by_id," \
                 " CONCAT_WS(' ', user.first_name, user.last_name) as created_by_name," \
                 " sow.published as published"\
                 " FROM sow_scheme_of_work as sow" \
                 " LEFT JOIN sow_learning_episode as le ON le.scheme_of_work_id = sow.id"\
                 " LEFT JOIN sow_learning_objective__has__learning_episode as lo_le ON lo_le.learning_episode_id = le.id"\
                 " LEFT JOIN sow_exam_board as exam ON exam.id = sow.exam_board_id" \
                 " LEFT JOIN sow_key_stage as kys ON kys.id = sow.key_stage_id "\
                 " LEFT JOIN auth_user as user ON user.id = sow.created_by" \
                 " WHERE sow.published = 1 OR sow.created_by = {auth_user}"\
                 " ORDER BY sow.created DESC LIMIT {top};"
    select_sql = select_sql.format(auth_user=to_db_null(auth_user), top=top)

    rows = db.executesql(select_sql)

    data = [];

    for row in rows:

        model = SchemeOfWorkModel(id_=row[0],
                                  name=row[1],
                                  description=row[2],
                                  exam_board_id=row[3],
                                  exam_board_name=row[4],
                                  key_stage_id=row[5],
                                  key_stage_name=row[6],
                                  created=row[7],
                                  created_by_id=row[8],
                                  created_by_name=row[9],
                                  published=row[10])
        data.append(model)

    return data

def get_model(db, id_, auth_user):
    model = SchemeOfWorkModel(0);

    select_sql = "SELECT "\
                  " sow.id as id, "\
                  " sow.name as name, "\
                  " sow.description as description, "\
                  " sow.exam_board_id as exam_board_id, "\
                  " exam.name as exam_board_name, "\
                  " sow.key_stage_id as key_stage_id, "\
                  " kys.name as key_stage_name, "\
                  " sow.created as created, "\
                  " sow.created_by as created_by_id, "\
                  " CONCAT_WS(' ', user.first_name, user.last_name) as created_by_name, "\
                  " sow.published as published"\
                  " FROM sow_scheme_of_work as sow "\
                  " LEFT JOIN sow_exam_board as exam ON exam.id = sow.exam_board_id "\
                  " INNER JOIN sow_key_stage as kys ON kys.id = sow.key_stage_id "\
                  " INNER JOIN auth_user as user ON user.id = sow.created_by "\
                  "  WHERE sow.id = {scheme_of_work_id} AND (sow.published = 1 OR sow.created_by = {auth_user});"

    select_sql = select_sql.format(scheme_of_work_id=id_, auth_user=to_db_null(auth_user))

    rows = db.executesql(select_sql)

    for row in rows:
        model = SchemeOfWorkModel(id_=row[0],
                                  name=row[1],
                                  description=row[2],
                                  exam_board_id=row[3],
                                  exam_board_name=row[4],
                                  key_stage_id=row[5],
                                  key_stage_name=row[6],
                                  created=row[7],
                                  created_by_id=row[8],
                                  created_by_name=row[9],
                                  published=row[10])

    return model


def get_schemeofwork_name_only(db, scheme_of_work_id):
    select_sql = ("SELECT " +
                  "  sow.name as name "  # 0
                  " FROM sow_scheme_of_work as sow " +
                  " LEFT JOIN auth_user as user ON user.id = sow.created_by " +
                  " WHERE sow.id = {scheme_of_work_id};".format(scheme_of_work_id=scheme_of_work_id))

    rows = db.executesql(select_sql)

    scheme_of_work_name = ""
    for row in rows:
        scheme_of_work_name = row[0]

    return scheme_of_work_name


def get_key_stage_id_only(db, scheme_of_work_id):
    select_sql = ("SELECT " +
                  "  sow.key_stage_id as key_stage_id "  # 0
                  " FROM sow_scheme_of_work as sow " +
                  " LEFT JOIN auth_user as user ON user.id = sow.created_by " +
                  " WHERE sow.id = {scheme_of_work_id};".format(scheme_of_work_id=scheme_of_work_id))

    rows = db.executesql(select_sql)

    key_stage_id = 0
    for row in rows:
        key_stage_id = row[0]

    return key_stage_id

"""
Private CRUD functions
"""

def save(db, model, published=1):
    if model.is_new() == True:
        _insert(db, model, published)
    else:
        _update(db, model, published)

    return model;


def delete(db, auth_user_id, id_):
    model = SchemeOfWorkModel(id_)
    _delete(db, model);


def publish(db, auth_user_id, id_):
    model = SchemeOfWorkModel(id_)
    model.publish = True
    _publish(db, model);


def _update(db, model, published):
    str_update = "UPDATE sow_scheme_of_work SET name = '{name}', description = '{description}', exam_board_id = {exam_board_id}, key_stage_id = {key_stage_id}, published = {published} WHERE id =  {scheme_of_work_id};"
    str_update = str_update.format(
        name=to_db_null(model.name),
        description = to_db_null(model.description),
        exam_board_id = to_db_null(model.exam_board_id),
        key_stage_id=to_db_null(model.key_stage_id),
        scheme_of_work_id = to_db_null(model.id),
        published=published)

    db.executesql(str_update)

    return True


def _insert(db, model, published):
    str_insert = "INSERT INTO sow_scheme_of_work (name, description, exam_board_id, key_stage_id, created, created_by, published) VALUES ('{name}', '{description}', {exam_board_id}, {key_stage_id}, '{created}', {created_by}, {published});"
    str_insert = str_insert.format(
        name=to_db_null(model.name),
        description=to_db_null(model.description),
        exam_board_id=to_db_null(model.exam_board_id),
        key_stage_id=to_db_null(model.key_stage_id),
        created=to_db_null(model.created),
        created_by=to_db_null(model.created_by_id),
        published=published)

    db.executesql(str_insert)

    # get last inserted row id
    rows = db.executesql("SELECT LAST_INSERT_ID();")

    for row in rows:
        model.id = int(row[0])

    return model.id


def _delete(db, model):
    str_delete = "DELETE FROM sow_scheme_of_work WHERE id = {scheme_of_work_id};"
    str_delete = str_delete.format(scheme_of_work_id=model.id)

    rval = db.executesql(str_delete)

    return rval


def _publish(db, model):
    str_delete = "UPDATE sow_scheme_of_work SET published = {published} WHERE id = {scheme_of_work_id};"
    str_delete = str_delete.format(published=1 if model.published else 0, scheme_of_work_id=model.id)

    rval = db.executesql(str_delete)

    return rval
