# -*- coding: utf-8 -*-
from datetime import datetime
from gluon.contrib.appconfig import AppConfig
from basemodel import BaseModel

configuration = AppConfig(reload=True)

db = DAL(configuration.get('db.uri'),
     pool_size=configuration.get('db.pool_size'),
     migrate_enabled=configuration.get('db.migrate'),
     check_reserved=['all'])


class SchemeOfWorkModel(BaseModel):
    name = ""
    description = ""
    exam_board_id = 0
    exam_board_name = ""
    key_stage_id = 0
    key_stage_name = ""


    def __init__(this, id_, name = "", description = "", exam_board_id = 0, exam_board_name = "", key_stage_id = 0, key_stage_name = "", created = "", created_by = ""):
        this.id = int(id_)
        this.name = name
        this.description = description
        this.exam_board_id = exam_board_id
        this.exam_board_name = exam_board_name if exam_board_id > 0 else ""
        this.key_stage_id = key_stage_id 
        this.key_stage_name = key_stage_name if key_stage_id > 0 else ""
        this.created = created
        this.created_by = created_by


    def validate(this):
        this.is_valid = True
        return True


    def _update(this):
        str_update = "UPDATE sow_scheme_of_work SET name = '{}', description = '{}', exam_board_id = {}, key_stage_id = {} WHERE id =  {};"
        str_update = str_update.format(this.name, this.description, this.exam_board_id, this.key_stage_id, this.id)

        db.executesql(str_update)

        return True

    def _insert(this):
        str_insert = "INSERT INTO sow_scheme_of_work (name, description, exam_board_id, key_stage_id, created, created_by) VALUES ('{}', '{}', {}, {}, '{}', {});"
        str_insert = str_insert.format(this.name, this.description, this.exam_board_id, this.key_stage_id, this.created, this.created_by)

        db.executesql(str_insert)

        return this.get_last_insert_row_id(db)


    def _delete(this):
        str_delete = "DELETE FROM sow_scheme_of_work WHERE id = {};"
        str_delete = str_delete.format(this.id)

        rval = db.executesql(str_delete)

        return rval


def save(auth_user_id, id_, name = "", description = "", exam_board_id = 0, key_stage_id = 0):
    # refresh model for validation
    model = SchemeOfWorkModel(
        id_=id_,
        name=name,
        description=description,
        exam_board_id=exam_board_id,
        key_stage_id=key_stage_id,
        created=datetime.now(),
        created_by=auth_user_id
    )

    model.validate()
    if model.is_valid == True:
        if model.is_new() == True:
            retId = model._insert()
            model.id = retId
        else:
            model._update()

    return model;


def delete(auth_user_id, id_):
    model = SchemeOfWorkModel(id_)
    model._delete();


def get_options():

    rows = db.executesql("SELECT id, name FROM sow_scheme_of_work;")

    data = [];

    for row in rows:
        model = SchemeOfWorkModel(row[0], row[1])
        data.append(model)

    return data


def get_all():
    select_sql = ("SELECT " +
                 "  sow.id as id, " + #0
                 "  sow.name as name, " + #1
                 "  sow.description as description, " + #2
                 "  sow.exam_board_id as exam_board_id, " + #3
                 "  exam.name as exam_board_name, " + #4
                 "  sow.key_stage_id as key_stage_id, " + #5
                 "  kys.name as key_stage_name, " + #6
                 "  sow.created as created, " + #7
                 "  CONCAT_WS(' ', user.first_name, user.last_name) as created_by " + #8
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
                  " sow.id as id, " + #0
                  " sow.name as name, " + #1
                  " sow.description as description, " + #2
                  " sow.exam_board_id as exam_board_id, " + #3
                  " exam.name as exam_board_name, " + #4
                  " sow.key_stage_id as key_stage_id, " + #5
                  " kys.name as key_stage_name, " + #6
                  " sow.created as created, " + #7
                  " CONCAT_WS(' ', user.first_name, user.last_name) as created_by " + #8
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
                 "  sow.name as name " #0
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
                 "  sow.key_stage_id as key_stage_id " #0
                 " FROM sow_scheme_of_work as sow " +
                 " LEFT JOIN auth_user as user ON user.id = sow.created_by " +
                 " WHERE sow.id = {};".format(scheme_of_work_id))

    rows = db.executesql(select_sql)

    key_stage_id = 0
    for row in rows:
        key_stage_id = row[0]

    return key_stage_id
