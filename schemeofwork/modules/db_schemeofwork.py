# -*- coding: utf-8 -*-
from cls_schemeofwork import SchemeOfWorkModel
from db_helper import to_db_null

def get_options(db):
    rows = db.executesql("SELECT id, name FROM sow_scheme_of_work;")

    data = [];

    for row in rows:
        model = SchemeOfWorkModel(row[0], row[1])
        data.append(model)

    return data


def get_all(db, key_stage_id=0):
    select_sql = ("SELECT " +
                  "  sow.id as id, " +  # 0
                  "  sow.name as name, " + # 1
                  "  sow.description as description, " +  # 2
                  "  sow.exam_board_id as exam_board_id, " +  # 3
                  "  exam.name as exam_board_name, " +  # 4
                  "  sow.key_stage_id as key_stage_id, " +  # 5
                  "  kys.name as key_stage_name, " +  # 6
                  "  sow.created as created, " +  # 7
                  "  sow.created_by as created_by_id, " + #8
                  "  CONCAT_WS(' ', user.first_name, user.last_name) as created_by_name " +  # 9
                  " FROM sow_scheme_of_work as sow " +
                  "  LEFT JOIN sow_exam_board as exam ON exam.id = sow.exam_board_id " +
                  "  INNER JOIN sow_key_stage as kys ON kys.id = sow.key_stage_id " +
                  "  LEFT JOIN auth_user as user ON user.id = sow.created_by " +
                  " WHERE sow.key_stage_id = {} or {} = 0;".format(key_stage_id, key_stage_id))

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
                                  created_by_name=row[9])

        model.set_is_recent()

        data.append(model)

    return data



def get_model(db, id_):
    model = SchemeOfWorkModel(0);

    select_sql = ("SELECT " +
                  " sow.id as id, " +  # 0
                  " sow.name as name, " +  # 1
                  " sow.description as description, " +  # 2
                  " sow.exam_board_id as exam_board_id, " +  # 3
                  " exam.name as exam_board_name, " +  # 4
                  " sow.key_stage_id as key_stage_id, " +  # 5
                  " kys.name as key_stage_name, " +  # 6
                  " sow.created as created, " +  # 7
                  " sow.created_by as created_by_id, " + #8
                  " CONCAT_WS(' ', user.first_name, user.last_name) as created_by_name " +  # 9
                  "FROM sow_scheme_of_work as sow " +
                  " LEFT JOIN sow_exam_board as exam ON exam.id = sow.exam_board_id " +
                  " INNER JOIN sow_key_stage as kys ON kys.id = sow.key_stage_id " +
                  " INNER JOIN auth_user as user ON user.id = sow.created_by " +
                  "  WHERE sow.id = {};".format(id_))

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
                                  created_by_name=row[9])

    return model


def get_schemeofwork_name_only(db, scheme_of_work_id):
    select_sql = ("SELECT " +
                  "  sow.name as name "  # 0
                  " FROM sow_scheme_of_work as sow " +
                  " LEFT JOIN auth_user as user ON user.id = sow.created_by " +
                  " WHERE sow.id = {};".format(scheme_of_work_id))

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
                  " WHERE sow.id = {};".format(scheme_of_work_id))

    rows = db.executesql(select_sql)

    key_stage_id = 0
    for row in rows:
        key_stage_id = row[0]

    return key_stage_id

"""
Private CRUD functions
"""

def save(db, model):
    if model.is_new() == True:
        _insert(db, model)
    else:
        _update(db, model)

    return model;


def delete(db, auth_user_id, id_):
    model = SchemeOfWorkModel(id_)
    _delete(db, model);


def _update(db, model):
    str_update = "UPDATE sow_scheme_of_work SET name = '{}', description = '{}', exam_board_id = {}, key_stage_id = {} WHERE id =  {};"
    str_update = str_update.format(to_db_null(model.name), to_db_null(model.description), to_db_null(model.exam_board_id), to_db_null(model.key_stage_id), to_db_null(model.id))

    db.executesql(str_update)

    return True


def _insert(db, model):
    str_insert = "INSERT INTO sow_scheme_of_work (name, description, exam_board_id, key_stage_id, created, created_by) VALUES ('{}', '{}', {}, {}, '{}', {});"
    str_insert = str_insert.format(to_db_null(model.name), to_db_null(model.description), to_db_null(model.exam_board_id), to_db_null(model.key_stage_id), to_db_null(model.created), to_db_null(model.created_by_id))

    db.executesql(str_insert)

    # get last inserted row id
    rows = db.executesql("SELECT LAST_INSERT_ID();")

    for row in rows:
        model.id = int(row[0])

    return model.id


def _delete(db, model):
    str_delete = "DELETE FROM sow_scheme_of_work WHERE id = {};"
    str_delete = str_delete.format(model.id)

    rval = db.executesql(str_delete)

    return rval
