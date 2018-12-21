# -*- coding: utf-8 -*-
from datetime import datetime
from gluon.contrib.appconfig import AppConfig
from basemodel import BaseModel

configuration = AppConfig(reload=True)

db = DAL(configuration.get('db.uri'),
     pool_size=configuration.get('db.pool_size'),
     migrate_enabled=configuration.get('db.migrate'),
     check_reserved=['all'])


class LearningObjectiveModel (BaseModel):

    description = ""
    solo_taxonomy_id = 0
    solo_taxonomy_name = ""
    solo_taxonomy_level = ""
    topic_id = 0
    topic_name = ""
    parent_topic_id = 0
    parent_topic_name = ""
    content_id = 0
    content_description = ""
    exam_board_id = 0
    exam_board_name = ""
    learning_episode_id = 0
    learning_episode_name = ""
    key_stage_id = 0
    key_stage_name = ""
    parent_id = None

    def __init__(this, id_, description = "", solo_taxonomy_id = 0, solo_taxonomy_name = "", solo_taxonomy_level = "", topic_id = 0, topic_name = "", parent_topic_id = 0, parent_topic_name = "", content_id = 0, content_description = "", exam_board_id = 0, exam_board_name = "", key_stage_id = 0, key_stage_name = "", learning_episode_id = 0, learning_episode_name = "", parent_id = None, created = "", created_by = ""):
        this.id = int(id_)
        this.description = description
        this.solo_taxonomy_id = solo_taxonomy_id
        this.solo_taxonomy_name = solo_taxonomy_name
        this.solo_taxonomy_level = solo_taxonomy_level
        this.topic_id = topic_id
        this.topic_name = topic_name
        this.parent_topic_id = parent_topic_id
        this.parent_topic_name = parent_topic_name
        this.content_id = content_id
        this.content_name = content_description
        this.exam_board_id = exam_board_id
        this.exam_board_name = exam_board_name
        this.learning_episode_id = learning_episode_id
        this.learning_episode_name = learning_episode_name
        this.key_stage_id = key_stage_id
        this.key_stage_name = key_stage_name
        this.parent_id = None if parent_id is None else parent_id
        this.created = created
        this.created_by = created_by


    def validate(this):
        this.is_valid = True
        return True


    def _update(this):

        # build update statement

        str_update = "UPDATE sow_learning_objective SET description = '{}', solo_taxonomy_id = {}, topic_id = {}, content_id = {}, exam_board_id = {} ".format(this.description, this.solo_taxonomy_id, this.topic_id, this.content_id, this.exam_board_id)

        # update parent id, if supplid
        if int(this.parent_id) > 0:
            str_update = str_update + ", parent_id = {} ".format(this.parent_id)

        str_update = str_update + " WHERE id =  {};".format(this.id)

        db.executesql(str_update)

        # insert if entry in sow_learning_objective__has__learning_episode doesn't already map sow learning_objective and sow_learning_episode

        str_check_duplicate = "SELECT id FROM sow_learning_objective__has__learning_episode WHERE learning_objective_id = {} AND learning_episode_id = {};"
        str_check_duplicate = str_check_duplicate.format(this.id, this.learning_episode_id)

        rows = db.executesql(str_check_duplicate)

        if(len(rows) == 0):
            str_insert2 = "INSERT INTO sow_learning_objective__has__learning_episode (learning_objective_id, learning_episode_id) VALUES ({}, {});"
            str_insert2 = str_insert2.format(this.id, this.learning_episode_id)
            db.executesql(str_insert2)

        return True


    def _insert(this):

        str_insert = "INSERT INTO sow_learning_objective (description, solo_taxonomy_id, topic_id, content_id, exam_board_id, parent_id, created, created_by) VALUES ('{}', {}, {}, {}, {}, {}, '{}', {});"
        str_insert = str_insert.format(this.description, this.solo_taxonomy_id, this.topic_id, this.content_id, this.exam_board_id, this.parent_id, this.created, this.created_by)

        db.executesql(str_insert)

        this.id = this.get_last_insert_row_id(db)

        # insert into linking table between objective and learning episode
        this._insert__sow_learning_objective__has__learning_episode()


        return True


    def _insert__sow_learning_objective__has__learning_episode(this):
        str_insert = "INSERT INTO sow_learning_objective__has__learning_episode (learning_objective_id, learning_episode_id) VALUES ({}, {});"
        str_insert = str_insert.format(this.id, this.learning_episode_id)
        db.executesql(str_insert)


    def _delete(this):
        str_delete = "DELETE FROM sow_learning_objective__has__learning_episode WHERE learning_objective_id = {};"
        str_delete = str_delete.format(this.id)

        rval = db.executesql(str_delete)

        return rval


def get_all(learning_episode_id):

    select_sql = ("SELECT " +
                 "  lob.id as id, " + # 0
                 "  lob.description as description, " + #1
                 "  solo.id as solo_id, " + #2
                 "  solo.name as solo_taxonomy_name, " + #3
                 "  solo.lvl as solo_taxonomy_level, " + #4
                 "  top.id as topic_id, " + #5
                 "  top.name as topic_name, " + #6
                 "  pnt_top.id as parent_topic_id, " + #7
                 "  pnt_top.name as parent_topic_name, " + #8
                 "  cnt.id as content_id, " + #9
                 "  cnt.description as content_description, " #10
                 "  exam.id as exam_board_id, " + #11
                 "  exam.name as exam_board_name, " #12
                 "  sow.key_stage_id as key_stage_id, " + #13
                 "  ks.name as key_stage_name, " + #14
                 "  le.id as learning_episode_id, " + #15
                 "  le.order_of_delivery_id as learning_episode_name, " + #16
                 "  lob.created as created, " + #17
                 "  CONCAT_WS(' ', user.first_name, user.last_name) as created_by " + #18
                 " FROM sow_scheme_of_work as sow " +
                 "  INNER JOIN sow_learning_episode as le ON le.scheme_of_work_id = sow.id " +
                 "  INNER JOIN sow_learning_objective__has__learning_episode as le_lo ON le_lo.learning_episode_id = le.id " +
                 "  INNER JOIN sow_learning_objective as lob ON lob.id = le_lo.learning_objective_id " +
                 "  LEFT JOIN sow_key_stage as ks ON ks.id = sow.key_stage_id " +
                 "  LEFT JOIN sow_topic as top ON top.id = lob.topic_id " +
                 "  LEFT JOIN sow_topic as pnt_top ON pnt_top.id = top.parent_id " +
                 "  LEFT JOIN sow_solo_taxonomy as solo ON solo.id = lob.solo_taxonomy_id " +
                 "  LEFT JOIN sow_content as cnt ON cnt.id = lob.content_id " +
                 "  LEFT JOIN sow_exam_board as exam ON exam.id = sow.exam_board_id " +
                 "  LEFT JOIN auth_user as user ON user.id = lob.created_by " +
                 "  WHERE le.id = {};".format(learning_episode_id))

    rows = db.executesql(select_sql)

    data = [];

    for row in rows:
        model = LearningObjectiveModel(
            id_ = row[0],
            description = row[1],
            solo_taxonomy_id = row[2],
            solo_taxonomy_name = row[3],
            solo_taxonomy_level = row[4],
            topic_id = row[5],
            topic_name = row[6],
            parent_topic_id = [7],
            parent_topic_name = [8],
            content_id = row[9],
            content_description = row[10],
            exam_board_id = row[11],
            exam_board_name = row[12],
            key_stage_id = row[13],
            key_stage_name = row[14],
            learning_episode_id = row[15],
            learning_episode_name = row[16],
            created = row[17],
            created_by = row[18])
        data.append(model)

    return data


def get_new_model(id_):
    model = LearningObjectiveModel(id_);

    select_sql = ("SELECT " +
                  "  lob.id AS id," +
                  "  lob.description AS description," +
                  "  solo.id AS solo_id," +
                  "  solo.name AS solo_taxonomy_name," +
                  "  solo.lvl AS solo_taxonomy_level," +
                  "  top.id AS topic_id," +
                  "  top.name AS topic_name," +
                  "  pnt_top.id AS parent_topic_id," +
                  "  pnt_top.name AS parent_topic_name," +
                  "  cnt.id AS content_id," +
                  "  cnt.description AS content_description," +
                  "  exam.id AS exam_board_id," +
                  "  exam.name AS exam_board_name," +
                  "  0 AS learning_episode_id," +
                  "  ks.id AS key_stage_id," +
                  "  ks.name AS key_stage_name," +
                  "  lob.created AS created," +
                  "  CONCAT_WS(' ', user.first_name, user.last_name) AS created_by" +
                  " FROM sow_learning_objective AS lob" +
                  "  LEFT JOIN sow_topic AS top ON top.id = lob.topic_id" +
                  "  LEFT JOIN sow_topic AS pnt_top ON pnt_top.id = top.parent_id" +
                  "  LEFT JOIN sow_solo_taxonomy AS solo ON solo.id = lob.solo_taxonomy_id" +
                  "  LEFT JOIN sow_content AS cnt ON cnt.id = lob.content_id" +
                  "  LEFT JOIN sow_key_stage AS ks ON ks.id = cnt.key_stage_id" +
                  "  LEFT JOIN sow_exam_board AS exam ON exam.id = lob.exam_board_id" +
                  "  LEFT JOIN auth_user AS user ON user.id = lob.created_by" +
                  "  WHERE lob.id = {};".format(id_))

    rows = db.executesql(select_sql)

    for row in rows:
        model = LearningObjectiveModel(
            id_ = row[0],
            description = row[1],
            solo_taxonomy_id = row[2],
            solo_taxonomy_name = row[3],
            solo_taxonomy_level = row[4],
            topic_id = row[5],
            topic_name = row[6],
            parent_topic_id = [7],
            parent_topic_name = [8],
            content_id = row[9],
            content_description = row[10],
            exam_board_id = row[11],
            exam_board_name = row[12],
            learning_episode_id = row[13],
            key_stage_id = row[14],
            key_stage_name = row[15],
            created = row[16],
            created_by = row[17])

    return model


def get_model(id_):
    model = LearningObjectiveModel(id_);

    select_sql = ("SELECT " +
                 "  lob.id as id, " + # 0
                 "  lob.description as description, " + #1
                 "  solo.id as solo_id, " + #2
                 "  solo.name as solo_taxonomy_name, " + #3
                 "  solo.lvl as solo_taxonomy_level, " + #4
                 "  top.id as topic_id, " + #5
                 "  top.name as topic_name, " + #6
                 "  pnt_top.id as parent_topic_id, " + #7
                 "  pnt_top.name as parent_topic_name, " + #8
                 "  cnt.id as content_id, " + #9
                 "  cnt.description as content_description, " #10
                 "  exam.id as exam_board_id, " + #11
                 "  exam.name as exam_board_name, " #12
                 "  le.id as learning_episode_id, " + #13
                 "  sow.key_stage_id as key_stage_id, " + #14
                 "  ks.name as key_stage_name, " + #15
                 "  lob.created as created, " + #15
                 "  CONCAT_WS(' ', user.first_name, user.last_name) as created_by " + #16
                 " FROM sow_scheme_of_work as sow " +
                 "  INNER JOIN sow_learning_episode as le ON le.scheme_of_work_id = sow.id " +
                 "  INNER JOIN sow_learning_objective__has__learning_episode as le_lo ON le_lo.learning_episode_id = le.id " +
                 "  INNER JOIN sow_learning_objective as lob ON lob.id = le_lo.learning_objective_id " +
                 "  LEFT JOIN sow_key_stage as ks ON ks.id = sow.key_stage_id " +
                 "  LEFT JOIN sow_topic as top ON top.id = lob.topic_id " +
                 "  LEFT JOIN sow_topic as pnt_top ON pnt_top.id = top.parent_id " +
                 "  LEFT JOIN sow_solo_taxonomy as solo ON solo.id = lob.solo_taxonomy_id " +
                 "  LEFT JOIN sow_content as cnt ON cnt.id = lob.content_id " +
                 "  LEFT JOIN sow_exam_board as exam ON exam.id = lob.exam_board_id " +
                 "  LEFT JOIN auth_user as user ON user.id = lob.created_by " +
                 "  WHERE lob.id = {};".format(id_))

    rows = db.executesql(select_sql)

    for row in rows:
        model = LearningObjectiveModel(
            id_ = row[0],
            description = row[1],
            solo_taxonomy_id = row[2],
            solo_taxonomy_name = row[3],
            solo_taxonomy_level = row[4],
            topic_id = row[5],
            topic_name = row[6],
            parent_topic_id = [7],
            parent_topic_name = [8],
            content_id = row[9],
            content_description = row[10],
            exam_board_id = row[11],
            exam_board_name = row[12],
            learning_episode_id = row[13],
            key_stage_id = row[14],
            key_stage_name = row[15],
            created = row[16],
            created_by = row[17])

    return model


def get_parent_options(current_key_stage_id = 0, topic_id = 0):
    select_sql = ("SELECT " +
                    "  lob.id as id, " + # 0
                     "  lob.description as description, " + #1
                     "  solo.id as solo_id, " + #2
                     "  solo.name as solo_taxonomy_name, " + #3
                     "  solo.lvl as solo_taxonomy_level, " + #4
                     "  top.id as topic_id, " + #5
                     "  top.name as topic_name, " + #6
                     "  pnt_top.id as parent_topic_id, " + #7
                     "  pnt_top.name as parent_topic_name, " + #8
                     "  cnt.id as content_id, " + #9
                     "  cnt.description as content_description, " #10
                     "  exam.id as exam_board_id, " + #11
                     "  exam.name as exam_board_name, " #12
                     "  ks.id as key_stage_id, " + #13
                     "  ks.name as key_stage_name, " + #14
                     "  lob.created as created, " + #15
                     "  CONCAT_WS(' ', user.first_name, user.last_name) as created_by " + #16
                    " FROM sow_learning_objective as lob " +
                    " LEFT JOIN sow_topic as top ON top.id = lob.topic_id " +
                    " LEFT JOIN sow_topic as pnt_top ON pnt_top.id = top.parent_id " +
                    " LEFT JOIN sow_solo_taxonomy as solo ON solo.id = lob.solo_taxonomy_id " +
                    " LEFT JOIN sow_content as cnt ON cnt.id = lob.content_id " +
                    " LEFT JOIN sow_exam_board as exam ON exam.id = lob.exam_board_id " +
                    " LEFT JOIN sow_key_stage as ks ON ks.id = cnt.key_stage_id " +
                    " LEFT JOIN auth_user as user ON user.id = lob.created_by " +
                    " WHERE ks.id > {} AND (top.id = {} OR pnt_top.id = {}) ORDER BY solo.lvl;".format(current_key_stage_id, topic_id, topic_id))

    rows = db.executesql(select_sql)

    data = [];

    for row in rows:
        model = LearningObjectiveModel(
            id_ = row[0],
            description = row[1],
            solo_taxonomy_id = row[2],
            solo_taxonomy_name = row[3],
            solo_taxonomy_level = row[4],
            topic_id = row[5],
            topic_name = row[6],
            parent_topic_id = [7],
            parent_topic_name = [8],
            content_id = row[9],
            content_description = row[10],
            exam_board_id = row[11],
            exam_board_name = row[12],
            key_stage_id = row[13],
            key_stage_name = row[14],
            created = row[15],
            created_by = row[16])
        data.append(model)

    return data


def get_unassociated_learning_objectives(learning_episode_id, key_stage_id, topic_id, parent_topic_id):

    select_sql = ("SELECT " +
            "  lob.id as id, " + # 0
             "  lob.description as description, " + #1
             "  solo.id as solo_id, " + #2
             "  solo.name as solo_taxonomy_name, " + #3
             "  solo.lvl as solo_taxonomy_level, " + #4
             "  top.id as topic_id, " + #5
             "  top.name as topic_name, " + #6
             "  pnt_top.id as parent_topic_id, " + #7
             "  pnt_top.name as parent_topic_name, " + #8
             "  cnt.id as content_id, " + #9
             "  cnt.description as content_description, " #10
             "  exam.id as exam_board_id, " + #11
             "  exam.name as exam_board_name, " #12
             "  ks.id as key_stage_id, " + #13
             "  ks.name as key_stage_name, " + #14
             "  le.id as learning_episode_id, " + #15
             "  le.order_of_delivery_id as order_of_delivery_id, " + #16
             "  lob.created as created, " + #17
             "  CONCAT_WS(' ', user.first_name, user.last_name) as created_by " + #19
            " FROM sow_learning_objective as lob " +
            " LEFT JOIN sow_learning_objective__has__learning_episode as le_lo ON le_lo.learning_objective_id = lob.id " +
            " LEFT JOIN sow_learning_episode as le ON le.id = le_lo.learning_episode_id " +
            " LEFT JOIN sow_topic as top ON top.id = lob.topic_id " +
            " LEFT JOIN sow_topic as pnt_top ON pnt_top.id = top.parent_id " +
            " LEFT JOIN sow_solo_taxonomy as solo ON solo.id = lob.solo_taxonomy_id " +
            " LEFT JOIN sow_content as cnt ON cnt.id = lob.content_id " +
            " LEFT JOIN sow_exam_board as exam ON exam.id = lob.exam_board_id " +
            " LEFT JOIN sow_key_stage as ks ON ks.id = cnt.key_stage_id " +
            " LEFT JOIN auth_user as user ON user.id = lob.created_by " +
            " WHERE ks.id = {} AND (le.id != {} OR le_lo.learning_objective_id is null) AND (top.id = {} ".format(key_stage_id, learning_episode_id, topic_id, parent_topic_id))
    if parent_topic_id is not None:
        select_sql = select_sql + " OR top.id = {} OR pnt_top.id = {}".format(parent_topic_id, parent_topic_id)
    select_sql = select_sql + ") ORDER BY solo.lvl;"

    #raise Exception(select_sql)
    rows = db.executesql(select_sql)

    data = [];

    for row in rows:
        model = LearningObjectiveModel(
            id_ = row[0],
            description = row[1],
            solo_taxonomy_id = row[2],
            solo_taxonomy_name = row[3],
            solo_taxonomy_level = row[4],
            topic_id = row[5],
            topic_name = row[6],
            parent_topic_id = [7],
            parent_topic_name = [8],
            content_id = row[9],
            content_description = row[10],
            exam_board_id = row[11],
            exam_board_name = row[12],
            key_stage_id = row[13],
            key_stage_name = row[14],
            learning_episode_id = learning_episode_id,
            learning_episode_name = row[16],
            created = row[17],
            created_by = row[18])
        data.append(model)

    return data


def save(auth_user_id, description):

    # refresh model for validation
    model = LearningObjectiveModel(
        id_ = request.vars.id,
        description = description,
        solo_taxonomy_id = request.vars.solo_taxonomy_id,
        topic_id = request.vars.topic_id,
        content_id = request.vars.content_id,
        exam_board_id = request.vars.exam_board_id,
        parent_id = request.vars.parent_id,
        learning_episode_id = request.vars.learning_episode_id,
        created = datetime.now(),
        created_by = auth_user_id
    )

    rval = model.validate()
    if model.is_valid == True:
        if model.is_new() == True:
            rval = model._insert()
        else:
            rval = model._update()

def add_existing_objective(auth_user_id, id_, learning_episode_id):
    model = LearningObjectiveModel(id_ = id_, learning_episode_id = learning_episode_id)
    model._insert__sow_learning_objective__has__learning_episode()

def delete(auth_user_id, id_):

    model = LearningObjectiveModel(id_)
    model._delete();
