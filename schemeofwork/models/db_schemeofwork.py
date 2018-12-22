# -*- coding: utf-8 -*-
# from gluon.debug import dbg

from gluon.contrib.appconfig import AppConfig

configuration = AppConfig(reload=True)
db = DAL(configuration.get('db.uri'),
         pool_size=configuration.get('db.pool_size'),
         migrate_enabled=configuration.get('db.migrate'),
         check_reserved=['all'])

from datetime import datetime
from cls_schemeofwork import SchemeOfWorkModel


def save(auth_user_id, id_, name, desc, exam_board_id, key_stage_id):
    # dbg.set_trace() # stop here!
    # refresh model for validation
    model = SchemeOfWorkModel(
        id_=id_,
        name=name,
        description=desc,
        exam_board_id=exam_board_id,
        key_stage_id=key_stage_id,
        created=datetime.now(),
        created_by=auth_user_id
    )

    model.validate()
    if model.is_valid == True:
        if model.is_new() == True:
            retId = _insert(model)
            model.id = retId
        else:
            _update(model)

    return model;


def delete(auth_user_id, id_):
    model = SchemeOfWorkModel(id_)
    _delete(model);


def get_options():
    rows = db.executesql("SELECT id, name FROM sow_scheme_of_work;")

    data = [];

    for row in rows:
        model = SchemeOfWorkModel(row[0], row[1])
        data.append(model)

    return data


def get_all():
    select_sql = ("SELECT " +
                  "  sow.id as id, " +  # 0
                  "  sow.name as name, " +  # 1
                  "  sow.description as description, " +  # 2
                  "  sow.exam_board_id as exam_board_id, " +  # 3
                  "  exam.name as exam_board_name, " +  # 4
                  "  sow.key_stage_id as key_stage_id, " +  # 5
                  "  kys.name as key_stage_name, " +  # 6
                  "  sow.created as created, " +  # 7
                  "  CONCAT_WS(' ', user.first_name, user.last_name) as created_by " +  # 8
                  " FROM sow_scheme_of_work as sow " +
                  "  INNER JOIN sow_exam_board as exam ON exam.id = sow.exam_board_id " +
                  "  INNER JOIN sow_key_stage as kys ON kys.id = sow.key_stage_id " +
                  "  LEFT JOIN auth_user as user ON user.id = sow.created_by; ")

    rows = db.executesql(select_sql)

    data = [];

    for row in rows:
        model = SchemeOfWorkModel(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
        data.append(model)

    return data


def get_model(id_):
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
                  " CONCAT_WS(' ', user.first_name, user.last_name) as created_by " +  # 8
                  "FROM sow_scheme_of_work as sow " +
                  " INNER JOIN sow_exam_board as exam ON exam.id = sow.exam_board_id " +
                  " INNER JOIN sow_key_stage as kys ON kys.id = sow.key_stage_id " +
                  " INNER JOIN auth_user as user ON user.id = sow.created_by " +
                  "  WHERE sow.id = {};".format(id_))

    rows = db.executesql(select_sql)

    for row in rows:
        model = SchemeOfWorkModel(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])

    return model


def get_schemeofwork_name_only(scheme_of_work_id):
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


def get_key_stage_id_only(scheme_of_work_id):
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

def _update(model):
    str_update = "UPDATE sow_scheme_of_work SET name = '{}', description = '{}', exam_board_id = {}, key_stage_id = {} WHERE id =  {};"
    str_update = str_update.format(model.name, model.description, model.exam_board_id, model.key_stage_id, model.id)

    db.executesql(str_update)

    return True


def _insert(model):
    str_insert = "INSERT INTO sow_scheme_of_work (name, description, exam_board_id, key_stage_id, created, created_by) VALUES ('{}', '{}', {}, {}, '{}', {});"
    str_insert = str_insert.format(model.name, model.description, model.exam_board_id, model.key_stage_id, model.created,
                                   model.created_by)

    db.executesql(str_insert)

    return _get_last_insert_row_id(model)


def _delete(model):
    str_delete = "DELETE FROM sow_scheme_of_work WHERE id = {};"
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
