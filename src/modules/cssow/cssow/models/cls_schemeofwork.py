# -*- coding: utf-8 -*-
from django.db import models
from .core.basemodel import BaseModel, try_int
from .core.db_helper import sql_safe, execSql, execCRUDSql

class SchemeOfWorkListModel(models.Model):
    schemesofwork = []
    def __init__(self, data):
        self.schemesofwork = get_all(None, 11, None).__dict__

class SchemeOfWorkModel(BaseModel):

    def __init__(self, id_, name="", description="", exam_board_id=0, exam_board_name="", key_stage_id=0, key_stage_name="", created="", created_by_id=0, created_by_name="", is_recent = False, published = 1):
        self.id = int(id_)
        self.name = name
        self.description = description
        self.exam_board_id = try_int(exam_board_id)
        self.exam_board_name = exam_board_name
        self.key_stage_id = try_int(key_stage_id)
        self.key_stage_name = key_stage_name
        self.is_recent = is_recent
        self.created=created
        self.created_by_id=try_int(created_by_id)
        self.created_by_name=created_by_name
        self.published=published
        self.url = '/schemeofwork/{}/lessons'.format(self.id)

    def validate(self):

        """ clean up and validate model """

        self._on_before_validate()

        # clean properties before validation
        self._clean_up()

        # Validate name
        self._validate_required_string("name", self.name, 1, 40)
        # Validate description
        self._validate_optional_string("description", self.description, 1500)
        # Validate exam board
        self._validate_optional_integer("exam_board_id", self.exam_board_id, 1, 9999)
        # Validate key stage
        self._validate_required_integer("key_stage_id", self.key_stage_id, 1, 9999)


    def _clean_up(self):
        """ clean up properties by casting and ensuring safe for inserting etc """

        self.id = int(self.id)

        if self.name is not None:
            self.name = sql_safe(self.name)

        if self.description is not None:
            self.description = sql_safe(self.description)

        if self.key_stage_name is not None:
            self.key_stage_name = sql_safe(self.key_stage_name)

        if self.exam_board_name is not None:
            self.exam_board_name = sql_safe(self.exam_board_name)

"""
DAL
"""

#from cls_schemeofwork import SchemeOfWorkModel
from .core.db_helper import to_db_null

def get_options(db, auth_user = 0):
    str_select = "SELECT sow.id, sow.name, ks.name as key_stage_name FROM sow_scheme_of_work as sow LEFT JOIN sow_key_stage as ks ON ks.id = sow.key_stage_id WHERE sow.published = 1 OR sow.created_by = {auth_user} ORDER BY sow.key_stage_id;"
    str_select = str_select.format(auth_user=to_db_null(auth_user))
    rows = []
    execSql(db, str_select, rows)

    data = []

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
                  " WHERE (sow.key_stage_id = {key_stage_id} or {key_stage_id} = 0) AND (sow.published = 1 OR sow.created_by = {auth_user})" \
                  " ORDER BY sow.key_stage_id;"
    select_sql = select_sql.format(key_stage_id=int(key_stage_id), auth_user=to_db_null(auth_user))

    rows = []
    execSql(db, select_sql, rows)

    data = []

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

        data.append(model.__dict__)

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

    rows = []
    execSql(db, select_sql, rows)

    data = []

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
    model = SchemeOfWorkModel(0)

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

    rows = []
    execSql(db, select_sql, rows)

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
    select_sql = "SELECT "\
                  "  sow.name as name "\
                  " FROM sow_scheme_of_work as sow "\
                  " LEFT JOIN auth_user as user ON user.id = sow.created_by "\
                  " WHERE sow.id = {scheme_of_work_id};"
    select_sql = select_sql.format(scheme_of_work_id=scheme_of_work_id)

    rows = []
    execSql(db, select_sql, rows)

    scheme_of_work_name = ""
    for row in rows:
        scheme_of_work_name = row[0]

    return scheme_of_work_name


def get_key_stage_id_only(db, scheme_of_work_id):
    select_sql = ("SELECT "\
                  "  sow.key_stage_id as key_stage_id "\
                  " FROM sow_scheme_of_work as sow "\
                  " LEFT JOIN auth_user as user ON user.id = sow.created_by "\
                  " WHERE sow.id = {scheme_of_work_id};".format(scheme_of_work_id=scheme_of_work_id))
    rows = []
    execSql(db, select_sql, rows)

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

    return model


def delete(db, auth_user_id, id_):
    model = SchemeOfWorkModel(id_)
    _delete(db, model)


def publish(db, auth_user_id, id_):
    model = SchemeOfWorkModel(id_)
    model.publish = True
    _publish(db, model)


def _update(db, model, published):
    str_update = "UPDATE sow_scheme_of_work SET name = '{name}', description = '{description}', exam_board_id = {exam_board_id}, key_stage_id = {key_stage_id}, published = {published} WHERE id =  {scheme_of_work_id};"
    str_update = str_update.format(
        name=to_db_null(model.name),
        description = to_db_null(model.description),
        exam_board_id = to_db_null(model.exam_board_id),
        key_stage_id=to_db_null(model.key_stage_id),
        scheme_of_work_id = to_db_null(model.id),
        published=published)

    execCRUDSql(db, str_update)

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

    execCRUDSql(db, str_insert)

    # get last inserted row id
    rows = []
    execCRUDSql(db, "SELECT LAST_INSERT_ID();", rows)

    for row in rows:
        model.id = int(row[0])

    return model.id


def _delete(db, model):
    str_delete = "DELETE FROM sow_scheme_of_work WHERE id = {scheme_of_work_id};"
    str_delete = str_delete.format(scheme_of_work_id=model.id)

    rval = []
    execCRUDSql(db, str_delete, rval)

    return rval


def _publish(db, model):
    str_delete = "UPDATE sow_scheme_of_work SET published = {published} WHERE id = {scheme_of_work_id};"
    str_delete = str_delete.format(published=1 if model.published else 0, scheme_of_work_id=model.id)

    rval = []
    execCRUDSql(db, str_delete, rval)

    return rval
