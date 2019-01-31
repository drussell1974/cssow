# -*- coding: utf-8 -*-
from datetime import datetime
from cls_reference import ReferenceModel
from db_helper import to_db_null

def get_options(db, scheme_of_work_id, auth_user):

    str_select = "SELECT" \
                 " ref.id as id," \
                 " ref.reference_type_id as reference_type_id," \
                 " ref.title as title," \
                 " ref.publisher as publisher," \
                 " ref.year_published as year_published," \
                 " ref.authors as authors," \
                 " ref.uri as uri " \
                 "FROM sow_reference as ref " \
                 "WHERE ref.scheme_of_work_id = {scheme_of_work_id}" \
                 " AND (ref.published = 1 OR ref.created_by = {auth_user});"

    str_select = str_select.format(auth_user=to_db_null(auth_user), scheme_of_work_id=scheme_of_work_id)

    rows = db.executesql(str_select)

    data = [];

    for row in rows:
        model = ReferenceModel(id_=row[0], reference_type_id = row[1], title=row[2], publisher=row[3], year_published=row[4], authors=row[5], uri=row[6], scheme_of_work_id = scheme_of_work_id)

        data.append(model)

    return data


def get_learning_episode_options(db, scheme_of_work_id, learning_episode_id, auth_user):

    str_select = "SELECT " \
                 " ref.id as id," \
                 " ref.reference_type_id as reference_type_id," \
                 " ref.title as title," \
                 " ref.publisher as publisher," \
                 " ref.year_published as year_published," \
                 " ref.authors as authors," \
                 " ref.uri as uri, " \
                 " le_ref.page_notes, " \
                 " le_ref.page_uri " \
                 "FROM sow_reference as ref " \
                 "INNER JOIN sow_learning_episode as le ON le.scheme_of_work_id = ref.scheme_of_work_id AND le.id = {learning_episode_id} " \
                 "LEFT JOIN sow_learning_episode__has__references as le_ref ON le_ref.learning_episode_id = le.id AND le_ref.reference_id = ref.id " \
                 "WHERE ref.scheme_of_work_id = {scheme_of_work_id}" \
                 " OR (ref.published = 1 OR ref.created_by = {auth_user});"

    str_select = str_select.format(auth_user=to_db_null(auth_user), scheme_of_work_id=scheme_of_work_id, learning_episode_id=learning_episode_id)

    rows = db.executesql(str_select)

    data = [];

    for row in rows:
        model = ReferenceModel(id_=row[0], reference_type_id=row[1], title=row[2], publisher=row[3], year_published=row[4], authors=row[5], uri=row[6], scheme_of_work_id = scheme_of_work_id)
        model.page_notes = row[7] if row[7] is not None else ''
        model.page_uri = row[8] if row[8] is not None else ''
        data.append(model)

    return data


def get_model(db, id_, scheme_of_work_id, auth_user):
    now = datetime.now()
    model = ReferenceModel(id_=0, reference_type_id = 6, title="", publisher="", year_published=now.year, authors="", uri="", scheme_of_work_id = scheme_of_work_id)

    str_select = "SELECT" \
                 " ref.id as id," \
                 " ref.reference_type_id as reference_type_id, " \
                 " ref.title as title," \
                 " ref.publisher as publisher," \
                 " ref.year_published as year_published," \
                 " ref.authors as authors," \
                 " ref.uri as uri " \
                 "FROM sow_reference as ref" \
                 " WHERE ref.id = {id_} AND (ref.published = 1 OR ref.created_by = {auth_user});"
    str_select = str_select.format(id_=id_, auth_user=to_db_null(auth_user))

    rows = db.executesql(str_select)

    for row in rows:
        model = ReferenceModel(id_=row[0], reference_type_id=row[1], title=row[2], publisher=row[3], year_published=row[4], authors=row[5], uri=row[6], scheme_of_work_id=scheme_of_work_id)

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

    # 1. Update the learning episode

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

    ## 2. insert related topics
    #if scheme_of_work_id > 0:
    #    _upsert_sow_scheme_of_work__has__reference(db, model, scheme_of_work_id)

    return model.id


def upsert_learning_episode_page_references(db, model):
    """ deletes and reinserts sow_learning_episode__has__references """

    if model.page_reference_ids is not None:
        # delete existing
        str_delete = "DELETE FROM sow_learning_episode__has__references WHERE learning_episode_id = {learning_episode_id};".format(learning_episode_id=model.id)

        db.executesql(str_delete)

        # reinsert
        str_insert = "INSERT INTO sow_learning_episode__has__references (reference_id, learning_episode_id, page_notes, page_uri) VALUES "
        str_insert_values = ""
        for index in range(len(model.page_reference_ids)):
            note = model.page_reference_notes[index].lstrip(' ').rstrip(' ') # clean up
            uri = model.page_reference_uri[index].lstrip(' ').rstrip(' ') # clean up
            if len(note) > 0: # and ensure it has a value worth inserting
                str_insert_values = str_insert_values + "({reference_id}, {learning_episode_id}, '{page_notes}', '{page_uri}'),"\
                    .format(reference_id=model.page_reference_ids[index], learning_episode_id=model.id, page_notes=note, page_uri=uri)

        if len(str_insert_values) > 0: # have we added any notes
            str_insert_values = str_insert_values.rstrip(",")
            db.executesql(str_insert + str_insert_values + ";")


def _delete(db, id_):
    str_delete = "DELETE FROM sow_reference WHERE id = {id_};"
    str_delete = str_delete.format(id_=id_)

    rval = db.executesql(str_delete)

    return rval
