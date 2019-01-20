# -*- coding: utf-8 -*-
from cls_learningepisode import LearningEpisodeModel
from db_helper import to_db_null
from helper_string import merge_string_list

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
        model = LearningEpisodeModel(
            id_=row[0],
            order_of_delivery_id=row[1],
            scheme_of_work_id=row[2],
            scheme_of_work_name=row[3],
            topic_id=row[4],
            topic_name=row[5],
            parent_topic_id=row[6],
            parent_topic_name=row[7],
            key_stage_id=row[8],
            key_words = row[9],
            summary = row[10],
            created=row[11],
            created_by_id=row[12],
            created_by_name=row[13])

        ' get the key words from the learning objectives '
        learning_objective_key_words = _get_learning_objective_keywords(db, learning_epsiode_id = model.id, auth_user = auth_user)

        ' merge the learning_objective keywords with the learning episode keywords '
        model.key_words = merge_string_list(model.key_words, learning_objective_key_words, ",")

        model.number_of_learning_objective = _get_number_of_learning_objectives(db, model.id, auth_user)

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
        model = LearningEpisodeModel(
            id_=row[0],
            order_of_delivery_id=row[1],
            scheme_of_work_id=row[2],
            scheme_of_work_name=row[3],
            topic_id=row[4],
            topic_name=row[5],
            parent_topic_id=row[6],
            parent_topic_name=row[7],
            key_stage_id=row[8],
            key_words = row[9],
            summary = row[10],
            created=row[11],
            created_by_id=row[12],
            created_by_name=row[13])

        #model.related_topic_ids = _get_related_topic_ids(db, model.id, row[4])

    return model


def _get_learning_objective_keywords(db, learning_epsiode_id, auth_user):
    """
    Append all keywords from learning objectives for this learning episode
    :param db:
    :param learning_epsiode_id:
    :param auth_user:
    :return: the results as a single list all comma seperated
    """

    select_sql = "SELECT "\
                 " lob.key_words as key_words"\
                 " FROM sow_learning_objective AS lob"\
                 " INNER JOIN sow_learning_episode AS le"\
                 " INNER JOIN sow_learning_objective__has__learning_episode AS lo_le ON lo_le.learning_objective_id = lob.id AND lo_le.learning_episode_id = le.id"\
                 " WHERE le.id = {learning_episode_id} AND (le.published = 1 OR le.created_by = {auth_user});"

    select_sql = select_sql.format(learning_episode_id=learning_epsiode_id, auth_user=to_db_null(auth_user))

    rows = db.executesql(select_sql)

    all = ""

    for row in rows:
        if row[0] is not None:
            all = all + row[0] + ","

    return all.lstrip(",").rstrip(",")

def _get_number_of_learning_objectives(db, learning_epsiode_id, auth_user):
    """
    get the number of learning objective for the learning episodes
    :param db: database context
    :param learning_epsiode_id:
    :param auth_user:
    :return:
    """
    count = 0

    select_sql = "SELECT "\
                 " id"\
                 " FROM sow_learning_objective__has__learning_episode"\
                 " WHERE learning_episode_id = {learning_episode_id};"

    select_sql = select_sql.format(learning_episode_id=learning_epsiode_id, auth_user=to_db_null(auth_user))

    rows = db.executesql(select_sql)

    return len(rows)


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
    """ updates the sow_learning_episode and sow_learning_episode__has__topics """

    # 1. Update the learning episode

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

    # 2. upsert related topics

    _upsert_related_topic_ids(db, model)
    _upsert_pathway_objective_ids(db, model)

    return True


def _insert(db, model, published):
    """ inserts the sow_learning_episode and sow_learning_episode__has__topics """

    # 1. Insert the learning episode

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

    rows = db.executesql("SELECT LAST_INSERT_ID();")

    for row in rows:
        model.id = int(row[0])

    # 2. insert related topics

    _upsert_related_topic_ids(db, model)

    return model.id


def _upsert_related_topic_ids(db, model):
    """ deletes and reinserts sow_learning_episode__has__topics """

    # delete existing
    str_delete = "DELETE FROM sow_learning_episode__has__topics WHERE learning_episode_id = {learning_episode_id};".format(learning_episode_id=model.id)

    db.executesql(str_delete)

    if len(model.related_topic_ids) > 0:
        # reinsert
        str_insert = "INSERT INTO sow_learning_episode__has__topics (learning_episode_id, topic_id) VALUES"

        for topic_id in model.related_topic_ids:
            if topic_id.isdigit():
                str_insert = str_insert + "({learning_episode_id}, {topic_id}),".format(learning_episode_id=model.id, topic_id=topic_id)

        str_insert = str_insert.rstrip(",") + ";"

        db.executesql(str_insert)


def _upsert_pathway_objective_ids(db, model):
    """ deletes and reinserts sow_learning_episode__has__topics """

    # delete existing
    str_delete = "DELETE FROM sow_learning_episode__has__pathway WHERE learning_episode_id = {learning_episode_id};".format(learning_episode_id=model.id)

    db.executesql(str_delete)

    if model.pathway_objective_ids is not None:
        # reinsert
        str_insert = "INSERT INTO sow_learning_episode__has__pathway (learning_episode_id, learning_objective_id) VALUES"

        for objective_id in model.pathway_objective_ids:
            if objective_id.isdigit():
                str_insert = str_insert + "({learning_episode_id}, {learning_objective_id}),".format(learning_episode_id=model.id, learning_objective_id=objective_id)

        str_insert = str_insert.rstrip(",") + ";"
        print(str_insert)
        db.executesql(str_insert)


def _delete(db, model):
    str_delete = "DELETE FROM sow_learning_episode WHERE id = {learning_episode_id};"
    str_delete = str_delete.format(learning_episode_id=model.id)

    rval = db.executesql(str_delete)

    return rval


def get_related_topic_ids(db, learning_episode_id, parent_topic_id):
    """
    gets the related topic ids for the learning episode and whether they are selected or should be disabled
    :param db: the database context
    :param learning_episode_id:
    :param parent_topic_id:
    :return: all topics and linked
    """

    str_select = " SELECT" \
                 " top.id as id," \
                 " top.name as name," \
                 " letop.topic_id as checked," \
                 " (SELECT count(topic_id)" \
                    " FROM sow_learning_objective AS lob" \
                    " LEFT JOIN" \
                    " sow_learning_objective__has__learning_episode AS lole ON lole.learning_objective_id = lob.id" \
                    " WHERE" \
                    " lole.learning_episode_id = letop.learning_episode_id and lob.topic_id = top.id) as disabled" \
                 " FROM sow_topic AS top" \
                 " LEFT JOIN" \
                 " sow_learning_episode__has__topics AS letop ON top.id = letop.topic_id and letop.learning_episode_id = {learning_episode_id}" \
                 " WHERE top.parent_id = {parent_topic_id};"

    str_select = str_select.format(learning_episode_id=learning_episode_id, parent_topic_id=parent_topic_id)

    rows = db.executesql(str_select)

    serializable_list = []

    for row in rows:
        serializable_list.append({"id":row[0], "name":row[1], "checked":row[2] is not None, "disabled":int(row[3]) > 0})

    return serializable_list


def get_pathway_objective_ids(db, learning_episode_id):
    """
    Get the learning objectives ids for the learning episcde
    :param db: database context
    :param learning_episode_id:
    :return: serialized learning objective ids
    """

    str_select = " SELECT" \
                 " learning_objective_id"\
                 " FROM sow_learning_episode__has__pathway" \
                 " WHERE learning_episode_id = {learning_episode_id};"

    str_select = str_select.format(learning_episode_id=learning_episode_id)

    rows = db.executesql(str_select)

    data = []

    for row in rows:
        data.append(int(row[0]))

    return data
