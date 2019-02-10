# -*- coding: utf-8 -*-
from datetime import datetime
from cls_learningobjective import LearningObjectiveModel
from db_helper import to_db_null
import db_keyword

def get_all(db, learning_episode_id, auth_user):

    select_sql = "SELECT "\
                 " lob.id as id, "\
                 " lob.description as description, "\
                 " solo.id as solo_id, "\
                 " solo.name as solo_taxonomy_name, "\
                 " solo.lvl as solo_taxonomy_level, "\
                 " top.id as topic_id, "\
                 " top.name as topic_name, "\
                 " pnt_top.id as parent_topic_id, "\
                 " pnt_top.name as parent_topic_name, "\
                 " cnt.id as content_id, "\
                 " cnt.description as content_description, "\
                 " exam.id as exam_board_id, "\
                 " exam.name as exam_board_name, "\
                 " sow.key_stage_id as key_stage_id, "\
                 " ks.name as key_stage_name, "\
                 " le.id as learning_episode_id, "\
                 " le.order_of_delivery_id as learning_episode_name, "\
                 " lob.key_words as key_words,"\
                 " lob.notes as notes,"\
                 " lob.group_name as group_name,"\
                 " lob.created as created, "\
                 " lob.created_by as created_by_id, "\
                 " CONCAT_WS(' ', user.first_name, user.last_name) as created_by_name "\
                 " FROM sow_scheme_of_work as sow "\
                 " INNER JOIN sow_learning_episode as le ON le.scheme_of_work_id = sow.id "\
                 " INNER JOIN sow_learning_objective__has__learning_episode as le_lo ON le_lo.learning_episode_id = le.id "\
                 " INNER JOIN sow_learning_objective as lob ON lob.id = le_lo.learning_objective_id "\
                 " LEFT JOIN sow_key_stage as ks ON ks.id = sow.key_stage_id "\
                 " LEFT JOIN sow_topic as top ON top.id = lob.topic_id "\
                 " LEFT JOIN sow_topic as pnt_top ON pnt_top.id = top.parent_id "\
                 " LEFT JOIN sow_solo_taxonomy as solo ON solo.id = lob.solo_taxonomy_id "\
                 " LEFT JOIN sow_content as cnt ON cnt.id = lob.content_id "\
                 " LEFT JOIN sow_exam_board as exam ON exam.id = sow.exam_board_id "\
                 " LEFT JOIN auth_user as user ON user.id = lob.created_by "\
                 " WHERE le.id = {learning_episode_id} AND (le.published = 1 or le.created_by = {auth_user});"
    select_sql = select_sql.format(learning_episode_id=learning_episode_id, auth_user=to_db_null(auth_user))

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
            key_words=row[17],
            notes=row[18],
            group_name=row[19],
            created = row[20],
            created_by_id = row[21],
            created_by_name = row[22])
        data.append(model)

    return data


def get_new_model(db, id_, auth_user):
    model = LearningObjectiveModel(id_);

    select_sql = "SELECT "\
                  " lob.id AS id,"\
                  " lob.description AS description,"\
                  " solo.id AS solo_id,"\
                  " solo.name AS solo_taxonomy_name,"\
                  " solo.lvl AS solo_taxonomy_level,"\
                  " top.id AS topic_id,"\
                  " top.name AS topic_name,"\
                  " pnt_top.id AS parent_topic_id,"\
                  " pnt_top.name AS parent_topic_name,"\
                  " cnt.id AS content_id,"\
                  " cnt.description AS content_description,"\
                  " exam.id AS exam_board_id,"\
                  " exam.name AS exam_board_name,"\
                  " 0 AS learning_episode_id,"\
                  " ks.id AS key_stage_id,"\
                  " ks.name AS key_stage_name,"\
                  " lob.key_words as key_words,"\
                  " lob.notes as notes,"\
                  " lob.group_name as group_name,"\
                  " lob.created AS created,"\
                  " CONCAT_WS(' ', user.first_name, user.last_name) AS created_by"\
                  " FROM sow_learning_objective AS lob"\
                  " LEFT JOIN sow_topic AS top ON top.id = lob.topic_id"\
                  " LEFT JOIN sow_topic AS pnt_top ON pnt_top.id = top.parent_id"\
                  " LEFT JOIN sow_solo_taxonomy AS solo ON solo.id = lob.solo_taxonomy_id"\
                  " LEFT JOIN sow_content AS cnt ON cnt.id = lob.content_id"\
                  " LEFT JOIN sow_key_stage AS ks ON ks.id = cnt.key_stage_id"\
                  " LEFT JOIN sow_exam_board AS exam ON exam.id = lob.exam_board_id"\
                  " LEFT JOIN auth_user AS user ON user.id = lob.created_by"\
                  " WHERE lob.id = {learning_objective_id} AND (lob.published = 1 or lob.created_by = {auth_user};"
    select_sql = select_sql.format(learning_objective_id=id_, auth_user=to_db_null(auth_user))

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
            key_words=row[16],
            notes=row[17],
            group_name=row[18],
            created = row[19],
            created_by_id = row[20],
            created_by_name = row[21])

    return model


def get_model(db, id_, auth_user):
    model = LearningObjectiveModel(id_);

    select_sql = "SELECT"\
                 " lob.id as id,"\
                 " lob.description as description,"\
                 " solo.id as solo_id,"\
                 " solo.name as solo_taxonomy_name,"\
                 " solo.lvl as solo_taxonomy_level,"\
                 " top.id as topic_id,"\
                 " top.name as topic_name,"\
                 " pnt_top.id as parent_topic_id,"\
                 " pnt_top.name as parent_topic_name,"\
                 " cnt.id as content_id,"\
                 " cnt.description as content_description,"\
                 " exam.id as exam_board_id,"\
                 " exam.name as exam_board_name,"\
                 " le.id as learning_episode_id,"\
                 " sow.key_stage_id as key_stage_id,"\
                 " ks.name as key_stage_name,"\
                 " lob.key_words as key_words,"\
                 " lob.notes as notes,"\
                 " lob.group_name as group_name,"\
                 " lob.created as created,"\
                 " lob.created_by as created_by_id,"\
                 " CONCAT_WS(' ', user.first_name, user.last_name) as created_by_name"\
                 " FROM sow_scheme_of_work as sow"\
                 " INNER JOIN sow_learning_episode as le ON le.scheme_of_work_id = sow.id"\
                 " INNER JOIN sow_learning_objective__has__learning_episode as le_lo ON le_lo.learning_episode_id = le.id"\
                 " INNER JOIN sow_learning_objective as lob ON lob.id = le_lo.learning_objective_id"\
                 " LEFT JOIN sow_key_stage as ks ON ks.id = sow.key_stage_id"\
                 " LEFT JOIN sow_topic as top ON top.id = lob.topic_id"\
                 " LEFT JOIN sow_topic as pnt_top ON pnt_top.id = top.parent_id"\
                 " LEFT JOIN sow_solo_taxonomy as solo ON solo.id = lob.solo_taxonomy_id"\
                 " LEFT JOIN sow_content as cnt ON cnt.id = lob.content_id"\
                 " LEFT JOIN sow_exam_board as exam ON exam.id = lob.exam_board_id"\
                 " LEFT JOIN auth_user as user ON user.id = lob.created_by"\
                 " WHERE lob.id = {learning_objective_id} AND (lob.published = 1 or lob.created_by = {auth_user});"

    select_sql = select_sql.format(learning_objective_id=id_, auth_user=to_db_null(auth_user))

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
            key_words=row[16],
            notes=row[17],
            group_name=row[18],
            created = row[19],
            created_by_id = row[20],
            created_by_name = row[21])

    # TODO: Clean up keywords - Remove once fixed
    sanitised_keywords = db_keyword.get_options(db)
    for skw in sanitised_keywords:
        model.key_words = model.key_words.replace(skw.lower(), skw)
    print(model.key_words)

    return model


def get_all_pathway_objectives(db, key_stage_id, key_words):

    select_sql = "SELECT"\
                 " lob.id as id,"\
                 " lob.description as description,"\
                 " solo.id as solo_id,"\
                 " solo.name as solo_taxonomy_name,"\
                 " solo.lvl as solo_taxonomy_level,"\
                 " top.id as topic_id,"\
                 " top.name as topic_name,"\
                 " pnt_top.id as parent_topic_id,"\
                 " pnt_top.name as parent_topic_name,"\
                 " cnt.id as content_id,"\
                 " cnt.description as content_description,"\
                 " exam.id as exam_board_id,"\
                 " exam.name as exam_board_name,"\
                 " ks.id as key_stage_id,"\
                 " ks.name as key_stage_name,"\
                 " lob.key_words as key_words,"\
                 " lob.group_name as group_name,"\
                 " lob.created as created,"\
                 " lob.created_by as created_by_id,"\
                 " CONCAT_WS(' ', user.first_name, user.last_name) as created_by_name"\
                " FROM sow_learning_objective as lob"\
                " LEFT JOIN sow_topic as top ON top.id = lob.topic_id"\
                " LEFT JOIN sow_topic as pnt_top ON pnt_top.id = top.parent_id"\
                " LEFT JOIN sow_solo_taxonomy as solo ON solo.id = lob.solo_taxonomy_id"\
                " LEFT JOIN sow_content as cnt ON cnt.id = lob.content_id"\
                " LEFT JOIN sow_exam_board as exam ON exam.id = lob.exam_board_id"\
                " LEFT JOIN sow_key_stage as ks ON ks.id = cnt.key_stage_id"\
                " LEFT JOIN auth_user as user ON user.id = lob.created_by"\
                " WHERE ks.id < {key_stage_id}" \
                " ORDER BY ks.name DESC, solo.lvl;"

    select_sql = select_sql.format(key_stage_id=key_stage_id)

    rows = db.executesql(select_sql)

    data = [];

    for row in rows:
        if len(row[15]) > 0:
            for keyword in key_words.split(","):
                if len(keyword) > 0 and keyword in row[15]:
                    model = LearningObjectiveModel(
                        id_ = row[0],
                        description = row[1],
                        solo_taxonomy_id = row[2],
                        solo_taxonomy_name = row[3],
                        solo_taxonomy_level = row[4],
                        topic_id = row[5],
                        topic_name = row[6],
                        parent_topic_id = row[7],
                        parent_topic_name = row[8],
                        content_id = row[9],
                        content_description = row[10],
                        exam_board_id = row[11],
                        exam_board_name = row[12],
                        key_stage_id = row[13],
                        key_stage_name = row[14],
                        key_words = row[15],
                        group_name = row[16],
                        created = row[17],
                        created_by_id = row[18],
                        created_by_name = row[19]
                        )

                    data.append(model)
                    break # only add objective once

    return data


def get_linked_pathway_objectives(db, learning_episode_id):

    select_sql = "SELECT"\
                 " lob.id as id,"\
                 " lob.description as description,"\
                 " solo.id as solo_id,"\
                 " solo.name as solo_taxonomy_name,"\
                 " solo.lvl as solo_taxonomy_level,"\
                 " top.id as topic_id,"\
                 " top.name as topic_name,"\
                 " pnt_top.id as parent_topic_id,"\
                 " pnt_top.name as parent_topic_name,"\
                 " cnt.id as content_id,"\
                 " cnt.description as content_description,"\
                 " exam.id as exam_board_id,"\
                 " exam.name as exam_board_name,"\
                 " ks.id as key_stage_id,"\
                 " ks.name as key_stage_name,"\
                 " lob.key_words as key_words,"\
                 " lob.group_name as group_name,"\
                 " lob.created as created,"\
                 " lob.created_by as created_by_id,"\
                 " CONCAT_WS(' ', user.first_name, user.last_name) as created_by_name"\
                " FROM sow_learning_objective as lob"\
                " INNER JOIN sow_learning_episode__has__pathway as pw ON pw.learning_objective_id = lob.id"\
                " LEFT JOIN sow_topic as top ON top.id = lob.topic_id"\
                " LEFT JOIN sow_topic as pnt_top ON pnt_top.id = top.parent_id"\
                " LEFT JOIN sow_solo_taxonomy as solo ON solo.id = lob.solo_taxonomy_id"\
                " LEFT JOIN sow_content as cnt ON cnt.id = lob.content_id"\
                " LEFT JOIN sow_exam_board as exam ON exam.id = lob.exam_board_id"\
                " LEFT JOIN sow_key_stage as ks ON ks.id = cnt.key_stage_id"\
                " LEFT JOIN auth_user as user ON user.id = lob.created_by"\
                " WHERE pw.learning_episode_id = {learning_episode_id}" \
                " ORDER BY ks.name DESC, solo.lvl;"

    select_sql = select_sql.format(learning_episode_id=learning_episode_id)

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
            parent_topic_id = row[7],
            parent_topic_name = row[8],
            content_id = row[9],
            content_description = row[10],
            exam_board_id = row[11],
            exam_board_name = row[12],
            key_stage_id = row[13],
            key_stage_name = row[14],
            key_words = row[15],
            group_name = row[16],
            created = row[17],
            created_by_id = row[18],
            created_by_name = row[19]
            )

        data.append(model)

    return data


def save(db, model, published=1):
    model.validate()
    if model.is_valid == True:
        if model.is_new() == True:
            _insert(db, model, published)
        else:
            _update(db, model, published)
    return model


def add_existing_objective(db, auth_user_id, id_, learning_episode_id):
    model = LearningObjectiveModel(id_ = id_, learning_episode_id = learning_episode_id)

    # insert into linking table between objective and lesson
    str_insert = "INSERT INTO sow_learning_objective__has__learning_episode (learning_objective_id, learning_episode_id) VALUES ({learning_objective_id}, {learning_episode_id});"
    str_insert = str_insert.format(learning_objective_id=model.id, learning_episode_id=model.learning_episode_id)
    db.executesql(str_insert)


def delete(db, auth_user_id, id_):

    model = LearningObjectiveModel(id_)
    _delete(db, model);


"""
Private CRUD functions 
"""

def _delete(db, model):

    str_delete = "DELETE FROM sow_learning_objective__has__learning_episode WHERE learning_objective_id = {learning_objective_id};"
    str_delete = str_delete.format(learning_objective_id=model.id)

    rval = db.executesql(str_delete)

    return rval


def _update(db, model, published):

    # build update statement

    str_update = "UPDATE sow_learning_objective SET description = '{description}', group_name = '{group_name}', notes = '{notes}', key_words = '{key_words}', solo_taxonomy_id = {solo_taxonomy_id}, topic_id = {topic_id}, content_id = {content_id}, exam_board_id = {exam_board_id}, parent_id = {parent_id}, published = {published} WHERE id = {learning_objective_id};"
    str_update = str_update.format(description=model.description, group_name=to_db_null(model.group_name), notes=to_db_null(model.notes), key_words=to_db_null(model.key_words), solo_taxonomy_id=model.solo_taxonomy_id, topic_id=model.topic_id, content_id=to_db_null(model.content_id), exam_board_id=to_db_null(model.exam_board_id), parent_id=to_db_null(model.parent_id), published=to_db_null(published), learning_objective_id=model.id)

    db.executesql(str_update)

    # insert if entry in sow_learning_objective__has__learning_episode doesn't already map sow learning_objective and sow_learning_episode

    str_check_duplicate = "SELECT id FROM sow_learning_objective__has__learning_episode WHERE learning_objective_id = {learning_objective_id} AND learning_episode_id = {learning_episode_id};"
    str_check_duplicate = str_check_duplicate.format(learning_objective_id=model.id, learning_episode_id=model.learning_episode_id)

    rows = db.executesql(str_check_duplicate)

    if(len(rows) == 0):
        str_insert2 = "INSERT INTO sow_learning_objective__has__learning_episode (learning_objective_id, learning_episode_id) VALUES ({learning_objective_id}, {learning_episode_id});"
        str_insert2 = str_insert2.format(learning_objective_id=model.id, learning_episode_id=model.learning_episode_id)
        db.executesql(str_insert2)

    return True


def _insert(db, model, published):

    str_insert = "INSERT INTO sow_learning_objective (description, group_name, notes, key_words, solo_taxonomy_id, topic_id, content_id, exam_board_id, parent_id, created, created_by, published)"
    str_insert = str_insert + " VALUES ('{description}', '{group_name}', '{notes}', '{key_words}', {solo_taxonomy_id}, {topic_id}, {content_id}, {exam_board_id}, {parent_id}, '{created}', {created_by}, {published});"
    str_insert = str_insert.format(
        description=model.description,
        group_name=model.group_name,
        solo_taxonomy_id=model.solo_taxonomy_id,
        topic_id=model.topic_id,
        content_id=to_db_null(model.content_id),
        exam_board_id=to_db_null(model.exam_board_id),
        parent_id=to_db_null(model.parent_id),
        key_words=to_db_null(model.key_words),
        notes=to_db_null(model.notes),
        created=model.created,
        created_by=model.created_by_id,
        published=published)

    db.executesql(str_insert)

    # get last inserted row id
    rows = db.executesql("SELECT LAST_INSERT_ID();")

    for row in rows:
        model.id = int(row[0])

    # insert into linking table between objective and lesson
    str_insert = "INSERT INTO sow_learning_objective__has__learning_episode (learning_objective_id, learning_episode_id) VALUES ({learning_objective_id}, {learning_episode_id});"
    str_insert = str_insert.format(learning_objective_id=model.id, learning_episode_id=model.learning_episode_id)
    db.executesql(str_insert)

    return True

