# -*- coding: utf-8 -*-
from datetime import datetime
from cls_reference import ReferenceModel
from db_helper import to_db_null

def get_options(db, scheme_of_work_id, auth_user):

    str_select = "SELECT" \
                 " ref.id as id," \
                 " ref.reference_type_id as reference_type_id," \
                 " type.name as reference_type_name," \
                 " ref.title as title," \
                 " ref.publisher as publisher," \
                 " ref.year_published as year_published," \
                 " ref.authors as authors," \
                 " ref.uri as uri " \
                 "FROM sow_reference as ref " \
                 "INNER JOIN sow_reference as type ON type.id = ref.reference_type_id " \
                 "WHERE ref.scheme_of_work_id = {scheme_of_work_id}" \
                 " AND (ref.published = 1 OR ref.created_by = {auth_user});"

    str_select = str_select.format(auth_user=to_db_null(auth_user), scheme_of_work_id=scheme_of_work_id)

    rows = db.executesql(str_select)

    data = [];

    for row in rows:
        model = ReferenceModel(id_=row[0], reference_type_id = row[1], reference_type_name = row[2], title=row[3], publisher=row[4], year_published=row[5], authors=row[6], uri=row[7], scheme_of_work_id = scheme_of_work_id)

        data.append(model)

    return data


def get_learning_episode_options(db, scheme_of_work_id, learning_episode_id, auth_user):

    str_select = "SELECT " \
                 " ref.id as id," \
                 " ref.reference_type_id as reference_type_id," \
                 " ref_type.name as reference_type_name,"\
                 " ref.title as title," \
                 " ref.publisher as publisher," \
                 " ref.year_published as year_published," \
                 " ref.authors as authors," \
                 " ref.uri as uri," \
                 " le_ref.id as page_id," \
                 " le_ref.page_notes, " \
                 " le_ref.page_uri " \
                 "FROM sow_reference as ref " \
                 "INNER JOIN sow_learning_episode as le ON le.scheme_of_work_id = ref.scheme_of_work_id AND le.id = {learning_episode_id} " \
                 "LEFT JOIN sow_learning_episode__has__references as le_ref ON le_ref.learning_episode_id = le.id AND le_ref.reference_id = ref.id " \
                 "LEFT JOIN sow_reference_type as ref_type ON ref.reference_type_id = ref_type.id " \
                 "WHERE ref.scheme_of_work_id = {scheme_of_work_id}" \
                 " OR (ref.published = 1 OR ref.created_by = {auth_user}) " \
                 "ORDER BY reference_type_id, title, authors;"

    str_select = str_select.format(auth_user=to_db_null(auth_user), scheme_of_work_id=scheme_of_work_id, learning_episode_id=learning_episode_id)

    rows = db.executesql(str_select)

    data = [];

    for row in rows:
        model = ReferenceModel(id_=row[0], reference_type_id=row[1], reference_type_name = row[2], title=row[3], publisher=row[4], year_published=row[5], authors=row[6], uri=row[7], scheme_of_work_id = scheme_of_work_id)
        model.page_id = row[8]
        model.page_note = row[9] if row[9] is not None else ''
        model.page_uri = row[10] if row[10] is not None else ''
        data.append(model)

    return data


def get_model(db, id_, scheme_of_work_id, auth_user):
    now = datetime.now()
    model = ReferenceModel(id_=0, reference_type_id = 6, reference_type_name = "Website", title="", publisher="", year_published=now.year, authors="", uri="", scheme_of_work_id = scheme_of_work_id)

    str_select = "SELECT" \
                 " ref.id as id," \
                 " ref.reference_type_id as reference_type_id, " \
                 " ref_type.name as reference_type_name," \
                 " ref.title as title," \
                 " ref.publisher as publisher," \
                 " ref.year_published as year_published," \
                 " ref.authors as authors," \
                 " ref.uri as uri " \
                 "FROM sow_reference as ref " \
                 "INNER JOIN sow_reference_type as ref_type ON ref_type.id = ref.reference_type_id" \
                 " WHERE ref.id = {id_} AND (ref.published = 1 OR ref.created_by = {auth_user});"
    str_select = str_select.format(id_=id_, auth_user=to_db_null(auth_user))

    rows = db.executesql(str_select)

    for row in rows:
        model = ReferenceModel(id_=row[0], reference_type_id=row[1], reference_type_name=row[2], title=row[3], publisher=row[4], year_published=row[5], authors=row[6], uri=row[7], scheme_of_work_id=scheme_of_work_id)

    return model


def save(db, model):
    """
    Upsert the reference
    :param db: database context
    :param model: the ReferenceModel
    :return: the updated ReferenceModel
    """
    if model.is_new() == True:
        model.id = _insert(db, model)
    else:
        _update(db, model)

    return model


def delete(db, id_):
    """

    :param db: the database context
    :param id_: the id of the record to delete
    :return: nothing
    """
    _delete(db, id_);

"""
Private CRUD functions 
"""

def _update(db, model):
    """ updates the sow_learning_episode and sow_learning_episode__has__topics """

    # 1. Update the lesson

    str_update = "UPDATE sow_reference SET reference_type_id = {reference_type_id}, title = '{title}', authors = '{authors}', publisher = '{publisher}', year_published = {year_published}, uri = '{uri}', scheme_of_work_id = {scheme_of_work_id} WHERE id = {id};"
    str_update = str_update.format(
        id=model.id,
        reference_type_id=model.reference_type_id,
        title=model.title,
        authors=to_db_null(model.authors),
        publisher=model.publisher,
        year_published = model.year_published,
        uri=to_db_null(model.uri),
        scheme_of_work_id = model.scheme_of_work_id)

    db.executesql(str_update)

    # 2. upsert related topics
    #if scheme_of_work_id > 0:
    #    _upsert_sow_scheme_of_work__has__reference(db, model, scheme_of_work_id)

    return True


def _insert(db, model):
    """ inserts the sow_reference and sow_scheme_of_work__has__reference """

    ## 1. Insert the reference

    str_insert = "INSERT INTO sow_reference (reference_type_id, title, authors, publisher, year_published, uri, scheme_of_work_id, created, created_by) VALUES ({reference_type_id}, '{title}', '{authors}', '{publisher}', {year_published}, '{uri}', {scheme_of_work_id}, '{created}', {created_by});"
    str_insert = str_insert.format(
        reference_type_id = model.reference_type_id,
        title=model.title,
        authors=to_db_null(model.authors),
        publisher=model.publisher,
        year_published = model.year_published,
        uri=to_db_null(model.uri),
        scheme_of_work_id = model.scheme_of_work_id,
        created=model.created,
        created_by=model.created_by_id)

    db.executesql(str_insert)

    rows = db.executesql("SELECT LAST_INSERT_ID();")

    for row in rows:
        model.id = int(row[0])

    return model.id



def insert_page_note(db, model):
    """ deletes and reinserts sow_learning_episode__has__references """
    # insert
    str_insert = "INSERT INTO sow_learning_episode__has__references (reference_id, learning_episode_id, page_notes, page_uri) VALUES ({reference_id}, {learning_episode_id}, '{page_notes}', '{page_uri}');"
    str_insert = str_insert.format(reference_id=model.reference_id, learning_episode_id=model.learning_episode_id, page_notes=model.page_note, page_uri=model.page_uri)

    db.executesql(str_insert)


def update_page_note(db, model):
    """ deletes and reinserts sow_learning_episode__has__references """
    # insert
    str_update = "UPDATE sow_learning_episode__has__references SET" \
                 " reference_id = {reference_id}," \
                 " learning_episode_id = {learning_episode_id}," \
                 " page_notes = '{page_notes}'," \
                 " page_uri = '{page_uri}' " \
                 "WHERE id = {id};"
    str_update = str_update.format(id=model.id, reference_id=model.reference_id, learning_episode_id=model.learning_episode_id, page_notes=model.page_note, page_uri=model.page_uri)

    db.executesql(str_update)


def delete_page_note(db, id_):
        # delete existing
        str_delete = "DELETE FROM sow_learning_episode__has__references WHERE id = {id};".format(id=id_)

        db.executesql(str_delete)


def _delete(db, id_):
    str_delete = "DELETE FROM sow_reference WHERE id = {id_};"
    str_delete = str_delete.format(id_=id_)

    rval = db.executesql(str_delete)

    return rval
