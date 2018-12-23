# -*- coding: utf-8 -*-

from gluon.contrib.appconfig import AppConfig
configuration = AppConfig(reload=True)
db = DAL(configuration.get('db.uri'),
     pool_size=configuration.get('db.pool_size'),
     migrate_enabled=configuration.get('db.migrate'),
     check_reserved=['all'])


from datetime import datetime
from cls_learningobjective import LearningObjectiveModel

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
                 "  lob.created_by as created_by_id, " + #18
                 "  CONCAT_WS(' ', user.first_name, user.last_name) as created_by_name " + #19
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
            created_by_id = row[18],
            created_by_name = row[19])
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
            created_by_id = row[17],
            created_by_name = row[18])

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
                 "  lob.created as created, " + #16
                 "  lob.created_by as created_by_id, " + #17
                 "  CONCAT_WS(' ', user.first_name, user.last_name) as created_by_name " + #18
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
            created_by_id = row[17],
            created_by_name = row[18])

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
                     "  lob.created_by as created_by_id, " + #16
                     "  CONCAT_WS(' ', user.first_name, user.last_name) as created_by_name " + #17
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
            created_by_id = row[16],
            created_by_name = row[17])
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
             "  lob.created_by as created_by_id, " + #18
             "  CONCAT_WS(' ', user.first_name, user.last_name) as created_by_name " + #19
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
    select_sql = select_sql + ") ORDER BY top.name;"

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
            created_by_id = row[18],
            created_by_name = row[19])
        data.append(model)

    return data


def save(auth_user_id, id_, description, solo_taxonomy_id, topic_id, content_id, exam_board_id, parent_id, learning_episode_id):

    # refresh model for validation
    model = LearningObjectiveModel(
        id_ = id_,
        description = description,
        solo_taxonomy_id = solo_taxonomy_id,
        topic_id = topic_id,
        content_id = content_id,
        exam_board_id = exam_board_id,
        parent_id = parent_id,
        learning_episode_id = learning_episode_id,
        created = datetime.now(),
        created_by_id = auth_user_id
    )

    rval = model.validate()
    if model.is_valid == True:
        if model.is_new() == True:
            rval = _insert(model)
        else:
            rval = _update(model)



def add_existing_objective(auth_user_id, id_, learning_episode_id):
    model = LearningObjectiveModel(id_ = id_, learning_episode_id = learning_episode_id)

    # insert into linking table between objective and learning episode
    str_insert = "INSERT INTO sow_learning_objective__has__learning_episode (learning_objective_id, learning_episode_id) VALUES ({}, {});"
    str_insert = str_insert.format(model.id, model.learning_episode_id)
    db.executesql(str_insert)


def delete(auth_user_id, id_):

    model = LearningObjectiveModel(id_)
    _delete(model);

"""
Private CRUD functions 
"""

def _delete(model):

    str_delete = "DELETE FROM sow_learning_objective__has__learning_episode WHERE learning_objective_id = {};"
    str_delete = str_delete.format(model.id)

    rval = db.executesql(str_delete)

    return rval


def _update(model):

    # build update statement

    str_update = "UPDATE sow_learning_objective SET description = '{}', solo_taxonomy_id = {}, topic_id = {}, content_id = {}, exam_board_id = {} ".format(model.description, model.solo_taxonomy_id, model.topic_id, model.content_id, model.exam_board_id)

    # update parent id, if supplid
    if int(model.parent_id) > 0:
        str_update = str_update + ", parent_id = {} ".format(model.parent_id)

    str_update = str_update + " WHERE id =  {};".format(model.id)

    db.executesql(str_update)

    # insert if entry in sow_learning_objective__has__learning_episode doesn't already map sow learning_objective and sow_learning_episode

    str_check_duplicate = "SELECT id FROM sow_learning_objective__has__learning_episode WHERE learning_objective_id = {} AND learning_episode_id = {};"
    str_check_duplicate = str_check_duplicate.format(model.id, model.learning_episode_id)

    rows = db.executesql(str_check_duplicate)

    if(len(rows) == 0):
        str_insert2 = "INSERT INTO sow_learning_objective__has__learning_episode (learning_objective_id, learning_episode_id) VALUES ({}, {});"
        str_insert2 = str_insert2.format(model.id, model.learning_episode_id)
        db.executesql(str_insert2)

    return True


def _insert(model):

    str_insert = "INSERT INTO sow_learning_objective (description, solo_taxonomy_id, topic_id, content_id, exam_board_id, created, created_by"
    str_values = "VALUES ('{}', {}, {}, {}, {}, '{}', {}".format(model.description, model.solo_taxonomy_id, model.topic_id, model.content_id, model.exam_board_id, model.created, model.created_by_id)

    if int(model.parent_id) > 0:
        str_insert = str_insert + ", parent_id"
        str_values = str_values + ", {}".format(model.parent_id)

    str_insert = str_insert + ")"
    str_values = str_values + ");"
    db.executesql(str_insert + str_values)

    # get last inserted row id
    rows = db.executesql("SELECT LAST_INSERT_ID();")

    for row in rows:
        model.id = int(row[0])

    # insert into linking table between objective and learning episode
    str_insert = "INSERT INTO sow_learning_objective__has__learning_episode (learning_objective_id, learning_episode_id) VALUES ({}, {});"
    str_insert = str_insert.format(model.id, model.learning_episode_id)
    db.executesql(str_insert)

    return True

