# -*- coding: utf-8 -*-
from .core.basemodel import BaseModel, try_int
from .core.db_helper import sql_safe, from_db_bool, execSql, execCRUDSql

enable_logging = False

class LearningObjectiveModel (BaseModel):

    def __init__(self, id_, description = "", notes = "", scheme_of_work_name = "", solo_taxonomy_id = 0, solo_taxonomy_name = "", solo_taxonomy_level = "", parent_topic_id = None, parent_topic_name = "", content_id = None, content_description = "", key_stage_id = 0, key_stage_name = "", lesson_id = 0, lesson_name = "", parent_id = None, key_words = "", group_name = "", is_key_objective = True, created = "", created_by_id = 0, created_by_name = "", published=1):
        self.id = int(id_)
        self.description = description
        self.notes = notes
        self.scheme_of_work_name = scheme_of_work_name
        self.solo_taxonomy_id = int(solo_taxonomy_id)
        self.solo_taxonomy_name = solo_taxonomy_name
        self.solo_taxonomy_level = solo_taxonomy_level
        self.parent_topic_id =  try_int(parent_topic_id)
        self.parent_topic_name = parent_topic_name
        self.content_id = try_int(content_id)
        self.content_description = content_description
        self.lesson_id = int(lesson_id)
        self.lesson_name = lesson_name
        self.key_stage_id = try_int(key_stage_id)
        self.key_stage_name = key_stage_name
        self.parent_id = try_int(parent_id)
        self.key_words = key_words
        self.group_name = group_name
        self.is_key_objective = from_db_bool(is_key_objective)
        self.created=created
        self.created_by_id=try_int(created_by_id)
        self.created_by_name=created_by_name
        self.published=published


    def validate(self):

        """ clean up and validate model """

        self._on_before_validate()

        # clean properties before validation
        self._clean_up()

        # validate description
        self._validate_required_string("description", self.description, 1, 1000)

        # validate group_name
        self._validate_optional_string("group_name", self.group_name, 15)

        # validate notes
        self._validate_optional_string("notes", self.notes, 2500)

        # validate content_id
        self._validate_optional_integer("content_id", self.content_id, 1, 9999)

        # validate solo_taxonomy_id
        self._validate_required_integer("solo_taxonomy_id", self.solo_taxonomy_id, 1, 9999)

        # validate lesson_id
        self._validate_required_integer("lesson_id", self.lesson_id, 1, 9999)

        # validate parent_id
        self._validate_optional_integer("parent_id", self.parent_id, 1, 9999)

        # Validate key_words
        self._validate_optional_list("key_words", self.key_words, sep=",", max_items=15)


    def _clean_up(self):
        """ clean up properties by casting and ensuring safe for inserting etc """

        self.id = int(self.id)

        # trim description
        if self.description is not None:
            self.description = sql_safe(self.description)

        # trim notes
        if self.notes is not None:
            self.notes = sql_safe(self.notes)

        # trim parent_topic_name
        if self.parent_topic_name is not None:
            self.parent_topic_name = sql_safe(self.parent_topic_name)

        # trim content_description
        if self.content_description is not None:
            self.content_description = sql_safe(self.content_description)

        # trim lesson_name
        if self.lesson_name is not None:
            self.lesson_name = sql_safe(self.lesson_name)

        # trim key_stage_name
        if self.key_stage_name is not None:
            self.key_stage_name = sql_safe(self.key_stage_name)

        if self.key_words is not None:
            self.key_words = sql_safe(self.key_words).replace(', ',',')

        # trim group_name
        if self.group_name is not None:
            self.group_name = sql_safe(self.group_name)


def sort_by_solo_taxonomy_level(unsorted_list):
    """
    Bubble sort by solo taxonomy level
    :param unsorted_list: the unsorted data
    :return: a sorted list
    """

    staging_list = unsorted_list

    while True:
        swapped = False
        for i in range(len(staging_list)-1):
            if staging_list[i].solo_taxonomy_level > staging_list[i+1].solo_taxonomy_level:
                """ put item in the correct position """
                temp1 = staging_list[i]
                temp2 = staging_list[i+1]

                staging_list[i] = temp2
                staging_list[i+1] = temp1
                swapped = True

        if swapped == False:
            """ no more sorting required so finish """
            break

    return staging_list

"""
DAL
"""

def log_info(db, msg, is_enabled = False):
    from .core.log import Log
    logger = Log()
    logger.is_enabled = is_enabled
    logger.write(db, msg)
    
    
def handle_log_info(db, msg):
    log_info(db, msg, is_enabled=enable_logging)


# -*- coding: utf-8 -*-
from datetime import datetime
#from .cls_learningobjective import LearningObjectiveModel
from .core.db_helper import to_db_null, to_empty, sql_safe, to_db_bool

def get_all(db, lesson_id, auth_user):

    select_sql = "SELECT "\
                 " lob.id as id, "\
                 " lob.description as description, "\
                 " solo.id as solo_id, "\
                 " solo.name as solo_taxonomy_name, "\
                 " solo.lvl as solo_taxonomy_level, "\
                 " cnt.id as content_id, "\
                 " cnt.description as content_description, "\
                 " sow.key_stage_id as key_stage_id, "\
                 " ks.name as key_stage_name, "\
                 " le.id as lesson_id, "\
                 " le.order_of_delivery_id as lesson_name, "\
                 " lob.key_words as key_words,"\
                 " lob.notes as notes,"\
                 " lob.group_name as group_name," \
                 " le_lo.is_key_objective as is_key_objective,"\
                 " lob.created as created, "\
                 " lob.created_by as created_by_id, "\
                 " CONCAT_WS(' ', user.first_name, user.last_name) as created_by_name "\
                 " FROM sow_scheme_of_work as sow "\
                 " INNER JOIN sow_lesson as le ON le.scheme_of_work_id = sow.id "\
                 " INNER JOIN sow_learning_objective__has__lesson as le_lo ON le_lo.lesson_id = le.id "\
                 " INNER JOIN sow_learning_objective as lob ON lob.id = le_lo.learning_objective_id "\
                 " LEFT JOIN sow_key_stage as ks ON ks.id = sow.key_stage_id "\
                 " LEFT JOIN sow_solo_taxonomy as solo ON solo.id = lob.solo_taxonomy_id "\
                 " LEFT JOIN sow_content as cnt ON cnt.id = lob.content_id "\
                 " LEFT JOIN auth_user as user ON user.id = lob.created_by "\
                 " WHERE le.id = {lesson_id} AND (le.published = 1 or le.created_by = {auth_user});"
    select_sql = select_sql.format(lesson_id=int(lesson_id), auth_user=to_db_null(auth_user))

    rows = []
    execSql(db, select_sql, rows)

    data = []

    for row in rows:
        model = LearningObjectiveModel(
            id_ = row[0],
            description = row[1],
            solo_taxonomy_id = row[2],
            solo_taxonomy_name = row[3],
            solo_taxonomy_level = row[4],
            content_id = row[5],
            content_description = row[6],
            key_stage_id = row[7],
            key_stage_name = row[8],
            lesson_id = row[9],
            lesson_name = row[10],
            key_words=row[11],
            notes=row[12],
            group_name=row[13],
            is_key_objective= row[14],
            created = row[15],
            created_by_id = row[16],
            created_by_name = row[17])
        data.append(model.__dict__)

    return data


def get_key_objectives(db, lesson_id, auth_user):

    select_sql = "SELECT "\
                 " lob.id as id, "\
                 " lob.description as description, "\
                 " solo.id as solo_id, "\
                 " solo.name as solo_taxonomy_name, "\
                 " solo.lvl as solo_taxonomy_level, "\
                 " cnt.id as content_id, "\
                 " cnt.description as content_description, "\
                 " sow.key_stage_id as key_stage_id, "\
                 " ks.name as key_stage_name, "\
                 " le.id as lesson_id, "\
                 " le.order_of_delivery_id as lesson_name, "\
                 " lob.key_words as key_words,"\
                 " lob.notes as notes,"\
                 " lob.group_name as group_name," \
                 " le_lo.is_key_objective as is_key_objective,"\
                 " lob.created as created, "\
                 " lob.created_by as created_by_id, "\
                 " CONCAT_WS(' ', user.first_name, user.last_name) as created_by_name "\
                 " FROM sow_scheme_of_work as sow "\
                 " INNER JOIN sow_lesson as le ON le.scheme_of_work_id = sow.id "\
                 " INNER JOIN sow_learning_objective__has__lesson as le_lo ON le_lo.lesson_id = le.id "\
                 " INNER JOIN sow_learning_objective as lob ON lob.id = le_lo.learning_objective_id "\
                 " LEFT JOIN sow_key_stage as ks ON ks.id = sow.key_stage_id "\
                 " LEFT JOIN sow_solo_taxonomy as solo ON solo.id = lob.solo_taxonomy_id "\
                 " LEFT JOIN sow_content as cnt ON cnt.id = lob.content_id "\
                 " LEFT JOIN auth_user as user ON user.id = lob.created_by "\
                 " WHERE le.id = {lesson_id} AND le_lo.is_key_objective = 1 AND (le.published = 1 or le.created_by = {auth_user});"

    select_sql = select_sql.format(lesson_id=int(lesson_id), auth_user=to_db_null(auth_user))

    rows = db.executesql(select_sql)

    data = []

    for row in rows:
        model = LearningObjectiveModel(
            id_ = row[0],
            description = row[1],
            solo_taxonomy_id = row[2],
            solo_taxonomy_name = row[3],
            solo_taxonomy_level = row[4],
            content_id = row[5],
            content_description = row[6],
            key_stage_id = row[7],
            key_stage_name = row[8],
            lesson_id = row[9],
            lesson_name = row[10],
            key_words=row[11],
            notes=row[12],
            group_name=row[13],
            is_key_objective= row[14],
            created = row[15],
            created_by_id = row[16],
            created_by_name = row[17])
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
                  " cnt.id AS content_id,"\
                  " cnt.description AS content_description,"\
                  " 0 AS lesson_id,"\
                  " ks.id AS key_stage_id,"\
                  " ks.name AS key_stage_name,"\
                  " lob.key_words as key_words,"\
                  " lob.notes as notes,"\
                  " lob.group_name as group_name,"\
                  " lob.created AS created,"\
                  " CONCAT_WS(' ', user.first_name, user.last_name) AS created_by"\
                  " FROM sow_learning_objective AS lob"\
                  " LEFT JOIN sow_solo_taxonomy AS solo ON solo.id = lob.solo_taxonomy_id"\
                  " LEFT JOIN sow_content AS cnt ON cnt.id = lob.content_id"\
                  " LEFT JOIN sow_key_stage AS ks ON ks.id = cnt.key_stage_id"\
                  " LEFT JOIN auth_user AS user ON user.id = lob.created_by"\
                  " WHERE lob.id = {learning_objective_id} AND (lob.published = 1 or lob.created_by = {auth_user})  ;"
    select_sql = select_sql.format(learning_objective_id=int(id_), auth_user=to_db_null(auth_user))

    rows = []
    execSql(db, select_sql, rows, log_info=handle_log_info)

    for row in rows:
        model = LearningObjectiveModel(
            id_ = row[0],
            description = row[1],
            solo_taxonomy_id = row[2],
            solo_taxonomy_name = row[3],
            solo_taxonomy_level = row[4],
            content_id = row[5],
            content_description = row[6],
            lesson_id = row[7],
            key_stage_id = row[8],
            key_stage_name = row[9],
            key_words=row[10],
            notes=row[11],
            group_name=row[12],
            created = row[13],
            created_by_id = row[14],
            created_by_name = row[15])

    return model


def get_model(db, id_, auth_user):
    model = LearningObjectiveModel(id_)

    select_sql = "SELECT"\
                 " lob.id as id,"\
                 " lob.description as description,"\
                 " solo.id as solo_id,"\
                 " solo.name as solo_taxonomy_name,"\
                 " solo.lvl as solo_taxonomy_level,"\
                 " cnt.id as content_id,"\
                 " cnt.description as content_description,"\
                 " le.id as lesson_id,"\
                 " sow.key_stage_id as key_stage_id,"\
                 " ks.name as key_stage_name,"\
                 " lob.key_words as key_words,"\
                 " lob.notes as notes,"\
                 " lob.group_name as group_name,"\
                 " lob.created as created,"\
                 " lob.created_by as created_by_id,"\
                 " CONCAT_WS(' ', user.first_name, user.last_name) as created_by_name"\
                 " FROM sow_scheme_of_work as sow"\
                 " INNER JOIN sow_lesson as le ON le.scheme_of_work_id = sow.id"\
                 " INNER JOIN sow_learning_objective__has__lesson as le_lo ON le_lo.lesson_id = le.id"\
                 " INNER JOIN sow_learning_objective as lob ON lob.id = le_lo.learning_objective_id"\
                 " LEFT JOIN sow_key_stage as ks ON ks.id = sow.key_stage_id"\
                 " LEFT JOIN sow_solo_taxonomy as solo ON solo.id = lob.solo_taxonomy_id"\
                 " LEFT JOIN sow_content as cnt ON cnt.id = lob.content_id"\
                 " LEFT JOIN auth_user as user ON user.id = lob.created_by"\
                 " WHERE lob.id = {learning_objective_id} AND (lob.published = 1 or lob.created_by = {auth_user});"

    select_sql = select_sql.format(learning_objective_id=int(id_), auth_user=to_db_null(auth_user))

    rows = []
    execSql(db, select_sql, rows, handle_log_info)

    for row in rows:
        model = LearningObjectiveModel(
            id_ = row[0],
            description = row[1],
            solo_taxonomy_id = row[2],
            solo_taxonomy_name = row[3],
            solo_taxonomy_level = row[4],
            content_id = row[5],
            content_description = row[6],
            lesson_id = row[7],
            key_stage_id = row[8],
            key_stage_name = row[9],
            key_words=row[10],
            notes=row[11],
            group_name=row[12],
            created = row[13],
            created_by_id = row[14],
            created_by_name = row[15])

    return model


def get_all_pathway_objectives(db, key_stage_id, key_words):

    select_sql = "SELECT"\
                 " lob.id as id,"\
                 " lob.description as description,"\
                 " solo.id as solo_id,"\
                 " solo.name as solo_taxonomy_name,"\
                 " solo.lvl as solo_taxonomy_level,"\
                 " cnt.id as content_id,"\
                 " cnt.description as content_description,"\
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
                " LEFT JOIN sow_key_stage as ks ON ks.id = cnt.key_stage_id"\
                " LEFT JOIN auth_user as user ON user.id = lob.created_by"\
                " WHERE ks.id < {key_stage_id}" \
                " ORDER BY ks.name DESC, solo.lvl;"

    select_sql = select_sql.format(key_stage_id=int(key_stage_id))

    rows = []
    execSql(db, select_sql, rows)

    data = []

    for row in rows:
        if len(row[15]) > 0 and key_words is not None:
            for keyword in key_words.split(","):
                if len(keyword) > 0 and keyword in row[15]:
                    model = LearningObjectiveModel(
                        id_ = row[0],
                        description = row[1],
                        solo_taxonomy_id = row[2],
                        solo_taxonomy_name = row[3],
                        solo_taxonomy_level = row[4],
                        content_id = row[5],
                        content_description = row[6],
                        key_stage_id = row[7],
                        key_stage_name = rows[8],
                        key_words = row[9],
                        group_name = row[10],
                        created = row[11],
                        created_by_id = row[12],
                        created_by_name = row[13]
                        )

                    data.append(model.__dict__)
                    break # only add objective once

    return data


def get_linked_pathway_objectives(db, lesson_id):

    select_sql = "SELECT"\
                 " lob.id as id,"\
                 " lob.description as description,"\
                 " solo.id as solo_id,"\
                 " solo.name as solo_taxonomy_name,"\
                 " solo.lvl as solo_taxonomy_level,"\
                 " cnt.id as content_id,"\
                 " cnt.description as content_description,"\
                 " ks.id as key_stage_id,"\
                 " ks.name as key_stage_name,"\
                 " lob.key_words as key_words,"\
                 " lob.group_name as group_name,"\
                 " lob.created as created,"\
                 " lob.created_by as created_by_id,"\
                 " CONCAT_WS(' ', user.first_name, user.last_name) as created_by_name"\
                " FROM sow_learning_objective as lob"\
                " INNER JOIN sow_lesson__has__pathway as pw ON pw.learning_objective_id = lob.id"\
                " LEFT JOIN sow_solo_taxonomy as solo ON solo.id = lob.solo_taxonomy_id"\
                " LEFT JOIN sow_content as cnt ON cnt.id = lob.content_id"\
                " LEFT JOIN sow_key_stage as ks ON ks.id = cnt.key_stage_id"\
                " LEFT JOIN auth_user as user ON user.id = lob.created_by"\
                " WHERE pw.lesson_id = {lesson_id}" \
                " ORDER BY ks.name DESC, solo.lvl;"

    select_sql = select_sql.format(lesson_id=int(lesson_id))

    rows = db.executesql(select_sql)

    data = []

    for row in rows:
        model = LearningObjectiveModel(
            id_ = row[0],
            description = row[1],
            solo_taxonomy_id = row[2],
            solo_taxonomy_name = row[3],
            solo_taxonomy_level = row[4],
            content_id = row[5],
            content_description = row[6],
            key_stage_id = row[7],
            key_stage_name = row[8],
            key_words = row[9],
            group_name = row[10],
            created = row[11],
            created_by_id = row[12],
            created_by_name = row[13]
            )

        data.append(model)

    return data


def get_other_objectives(db, lesson_id, scheme_of_work_id, key_word):

    select_sql = "SELECT DISTINCT"\
                 " lob.id as id,"\
                 " lob.description as description,"\
                 " lob.key_words as key_words "\
                 " FROM sow_learning_objective as lob"\
                 " INNER JOIN sow_learning_objective__has__lesson as lo_le ON lo_le.learning_objective_id = lob.id" \
                 " INNER JOIN sow_lesson as le ON le.id = lo_le.lesson_id" \
                 " WHERE le.scheme_of_work_id = {scheme_of_work_id}" \
                 " AND lob.id NOT IN (SELECT learning_objective_id FROM sow_learning_objective__has__lesson WHERE lesson_id = {lesson_id});"

    select_sql = select_sql.format(scheme_of_work_id=int(scheme_of_work_id),lesson_id=int(lesson_id), key_word=sql_safe(key_word))

    rows = db.executesql(select_sql)

    data = []

    for row in rows:
        if len(key_word) > 0 and key_word.lower() in row[2].lower():
            model = LearningObjectiveModel(
                id_ = row[0],
                description = row[1],
                key_words = row[2]
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


def add_existing_objective(db, learning_objective_id, lesson_id, auth_user_id):
    model = LearningObjectiveModel(id_ = learning_objective_id, lesson_id = lesson_id)

    # insert into linking table between objective and lesson
    str_insert = "INSERT INTO sow_learning_objective__has__lesson (learning_objective_id, lesson_id) VALUES ({learning_objective_id}, {lesson_id});"
    str_insert = str_insert.format(learning_objective_id=model.id, lesson_id=model.lesson_id)
    db.executesql(str_insert)


def delete(db, auth_user_id, id_):
    """ Delete learning objective """
    
    model = LearningObjectiveModel(id_)
    _delete(db, model);


def delete_unpublished(db, lesson_id, auth_user_id):
    """ Delete all unpublished learning objectives """

    _delete_unpublished(db, lesson_id, auth_user_id)
    

def update_is_key_objective(db, learning_objective_id, lesson_id, is_key_objective):

    str_update = "UPDATE sow_learning_objective__has__lesson SET is_key_objective = {is_key_objective} WHERE learning_objective_id = {learning_objective_id};"
    str_update = str_update.format(learning_objective_id=int(learning_objective_id), lesson_id=int(lesson_id), is_key_objective=to_db_bool(is_key_objective))

    db.executesql(str_update)

    return "updated"

"""
Private CRUD functions 
"""

def _delete(db, model):

    str_delete = "DELETE FROM sow_learning_objective__has__lesson WHERE learning_objective_id = {learning_objective_id};"
    str_delete = str_delete.format(learning_objective_id=model.id)

    rval = execCRUDSql(db, str_delete, log_info=handle_log_info)

    return rval


def _update(db, model, published):

    # build update statement

    str_update = "UPDATE sow_learning_objective SET description = '{description}', group_name = '{group_name}', notes = '{notes}', key_words = '{key_words}', solo_taxonomy_id = {solo_taxonomy_id}, content_id = {content_id}, parent_id = {parent_id}, published = {published} WHERE id = {learning_objective_id};"
    str_update = str_update.format(description=model.description, group_name=to_db_null(model.group_name), notes=to_db_null(model.notes), key_words=to_db_null(model.key_words), solo_taxonomy_id=model.solo_taxonomy_id, content_id=to_db_null(model.content_id), parent_id=to_db_null(model.parent_id), published=to_db_null(published), learning_objective_id=model.id)

    execCRUDSql(db, str_update, log_info=handle_log_info)

    # insert if entry in sow_learning_objective__has__lesson doesn't already map sow learning_objective and sow_lesson

    str_check_duplicate = "SELECT id FROM sow_learning_objective__has__lesson WHERE learning_objective_id = {learning_objective_id} AND lesson_id = {lesson_id};"
    str_check_duplicate = str_check_duplicate.format(learning_objective_id=model.id, lesson_id=model.lesson_id)

    rows = []
    execSql(db, str_check_duplicate, rows, handle_log_info)

    if(len(rows) == 0):
        str_insert2 = "INSERT INTO sow_learning_objective__has__lesson (learning_objective_id, lesson_id) VALUES ({learning_objective_id}, {lesson_id});"
        str_insert2 = str_insert2.format(learning_objective_id=model.id, lesson_id=model.lesson_id)
        execCRUDSql(db, str_insert2, log_info=handle_log_info)

    return True


def _insert(db, model, published):

    str_insert = "INSERT INTO sow_learning_objective (description, group_name, notes, key_words, solo_taxonomy_id, content_id, parent_id, created, created_by, published)"
    str_insert = str_insert + " VALUES ('{description}', '{group_name}', '{notes}', '{key_words}', {solo_taxonomy_id}, {content_id}, {parent_id}, '{created}', {created_by}, {published});"
    str_insert = str_insert.format(
        description=model.description,
        group_name=model.group_name,
        solo_taxonomy_id=model.solo_taxonomy_id,
        content_id=to_db_null(model.content_id),
        parent_id=to_db_null(model.parent_id),
        key_words=to_db_null(model.key_words),
        notes=to_db_null(model.notes),
        created=model.created,
        created_by=model.created_by_id,
        published=published)
    str_insert = str_insert + "SELECT LAST_INSERT_ID();"

    rows = []
    execCRUDSql(db, str_insert, result=rows, log_info=handle_log_info)

    for row in rows:
        model.id = int(row[0])

    # insert into linking table between objective and lesson
    str_insert = "INSERT INTO sow_learning_objective__has__lesson (learning_objective_id, lesson_id) VALUES ({learning_objective_id}, {lesson_id});"
    str_insert = str_insert.format(learning_objective_id=model.id, lesson_id=model.lesson_id)
    execCRUDSql(db, str_insert, log_info=handle_log_info)

    return True


def _delete_unpublished(db, lesson_id, auth_user_id):
    """ Delete all unpublished learning objectives """
    str_select = "SELECT lol.learning_objective_id "\
        "FROM sow_learning_objective__has__lesson AS lol "\
        "INNER JOIN sow_lesson AS l ON l.id = lol.lesson_id "\
        "INNER JOIN sow_learning_objective AS lo ON lo.id = lol.learning_objective_id "\
        "WHERE lo.published = 0 AND l.id={lesson_id} AND l.created_by = {auth_user_id};".format(lesson_id=lesson_id, auth_user_id=auth_user_id)
    rows = []
    execSql(db, str_select, rows, handle_log_info)

    for row in rows:
        _id = row[0]
        str_delete = "DELETE FROM sow_learning_objective__has__lesson WHERE lesson_id = {lesson_id} AND learning_objective_id={_id};".format(lesson_id=lesson_id,_id=_id)
        execCRUDSql(db, str_delete, log_info=handle_log_info)
    pass