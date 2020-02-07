# -*- coding: utf-8 -*-
from .core.basemodel import BaseModel, try_int
from .core.db_helper import sql_safe, execSql

enable_logging = False

class ResourceModel (BaseModel):

    def __init__(self, id_, lesson_id, scheme_of_work_id, title, publisher, year_published, authors = "", page_note="", page_uri="", task_icon = "", last_accessed = "", created = "", created_by_id = 0, created_by_name = "", published=1):
        self.id = int(id_)
        self.title = title
        self.publisher = publisher
        self.year_published = try_int(year_published)
        self.authors = authors
        self.page_note = page_note
        self.page_uri = page_uri
        self.task_icon = task_icon
        self.lesson_id = lesson_id
        self.scheme_of_work_id = scheme_of_work_id
        self.last_accessed = last_accessed
        self.created = created
        self.created_by_id = try_int(created_by_id)
        self.created_by_name = created_by_name
        self.published = published


    def validate(self):

        """ clean up and validate model """

        self._on_before_validate()

        # clean properties before validation
        self._clean_up()

        # validate title
        self._validate_required_string("title", self.title, 1, 300)

        # validate authors
        self._validate_optional_string("authors", self.authors, 200)

        # validate publisher
        self._validate_required_string("publisher", self.publisher, 1, 70)

        # validate year_published
        self._validate_required_integer("year_published", self.year_published, 1700, 2100)

        # validate page_note
        self._validate_required_string("page_note", self.page_note, 1, 250)

        # validate page_uri
        self._validate_optional_uri("page_uri", self.page_uri)

        # validate task_icon
        self._validate_optional_string("task_icon", self.task_icon, 500)


    def _clean_up(self):
        """ clean up properties by casting and ensuring safe for inserting etc """

        self.id = int(self.id)

        # trim title
        if self.title is not None:
            self.title = sql_safe(self.title)

        # trim authors
        if self.authors is not None:
            self.authors = sql_safe(self.authors)

        # trim publisher
        if self.publisher is not None:
            self.publisher = sql_safe(self.publisher)

        # trim uri
        if self.page_uri is not None:
            self.page_uri = sql_safe(self.page_uri)

        # trim notes
        if self.page_note is not None:
            self.page_note = sql_safe(self.page_note)

        # trim notes
        if self.task_icon is not None:
            self.task_icon = sql_safe(self.task_icon)

"""
DAL
"""
from datetime import datetime
from .core.db_helper import to_db_null, to_empty


def log_info(db, msg, is_enabled = False):
    from .core.log import Log
    logger = Log()
    logger.is_enabled = is_enabled
    logger.write(db, msg)
    
    
def handle_log_info(db, msg):
    log_info(db, msg, is_enabled=enable_logging)


def get(db, scheme_of_work_id, lesson_id, auth_user):
    """ Get resources for lesson """

    str_select = "SELECT" \
                " res.id as id," \
                " res.title as title," \
                " res.publisher as publisher," \
                " res.year_published as year_published," \
                " res.authors as authors," \
                " res.page_notes as page_notes, "\
                " res.url as page_uri, " \
                " res.task_icon as task_icon, "\
                " res.lesson_id as lesson_id, "\
                " res.created as created, "\
                " res.created_by as created_by_id, "\
                " CONCAT_WS(' ', user.first_name, user.last_name) as created_by_name "\
                "FROM sow_resource AS res " \
                " LEFT JOIN auth_user AS user ON user.id = res.created_by "\
                "WHERE res.lesson_id = {lesson_id} " \
                " AND (res.published = 1 OR res.created_by = {auth_user});"
                
    str_select = str_select.format(auth_user=to_db_null(auth_user), scheme_of_work_id=int(scheme_of_work_id), lesson_id=int(lesson_id))

    rows = []
    execSql(db, str_select, rows, handle_log_info)

    data = []
    
    for row in rows:
        model = ResourceModel(
            id_=row[0], 
            title=row[1], 
            publisher=row[2], 
            year_published=row[3], 
            authors=row[4], 
            page_note=row[5], 
            page_uri=row[6], 
            task_icon=row[7], 
            lesson_id=row[8],
            created = row[9],
            created_by_id = row[10],
            created_by_name = row[11], 
            scheme_of_work_id=scheme_of_work_id)

        data.append(model)

    return data


def get_model(db, id_, scheme_of_work_id, auth_user):
    """ Get Resource """

    str_select = "SELECT" \
                " res.id as id," \
                " res.title as title," \
                " res.publisher as publisher," \
                " res.year_published as year_published," \
                " res.authors as authors," \
                " res.page_notes as page_notes, "\
                " res.url as page_uri, " \
                " res.task_icon as task_icon, "\
                " res.lesson_id as lesson_id, "\
                " res.created as created, "\
                " res.created_by as created_by_id, "\
                " CONCAT_WS(' ', user.first_name, user.last_name) as created_by_name "\
                "FROM sow_resource AS res " \
                " LEFT JOIN auth_user AS user ON user.id = res.created_by "\
                "WHERE res.id = {id} " \
                " AND (res.published = 1 OR res.created_by = {auth_user});"

    str_select = str_select.format(id=(id_), auth_user=to_db_null(auth_user))

    rows = []
    execSql(db, str_select, rows, handle_log_info)

    data = None
    
    for row in rows:
        model = ResourceModel(
            id_=row[0],
            title=row[1], 
            publisher=row[2], 
            year_published=row[3], 
            authors=row[4], 
            page_note=row[5], 
            page_uri=row[6], 
            task_icon=row[7],
            lesson_id=row[8],
            created = row[9],
            created_by_id = row[10],
            created_by_name = row[11], 
            scheme_of_work_id=scheme_of_work_id)

        data = model
        

    return data


'''
def get_options(db, scheme_of_work_id, auth_user):

    str_select = "SELECT" \
                 " ref.id as id," \
                 " ref.reference_type_id as reference_type_id," \
                 " type.name as reference_type_name," \
                 " ref.title as title," \
                 " ref.publisher as publisher," \
                 " ref.year_published as year_published," \
                 " ref.authors as authors," \
                 " ref.url as uri " \
                 "FROM sow_reference as ref " \
                 "INNER JOIN sow_reference_type as type ON type.id = ref.reference_type_id " \
                 "WHERE ref.scheme_of_work_id = {scheme_of_work_id}" \
                 " AND (ref.published = 1 OR ref.created_by = {auth_user});"

    str_select = str_select.format(auth_user=to_db_null(auth_user), scheme_of_work_id=int(scheme_of_work_id))

    rows = db.executesql(str_select)

    data = []

    for row in rows:
        model = ReferenceModel(id_=row[0], reference_type_id = row[1], reference_type_name = row[2], title=row[3], publisher=row[4], year_published=row[5], authors=row[6], uri=row[7], scheme_of_work_id = scheme_of_work_id)

        data.append(model)

    return data
'''

def get_lesson_options(db, scheme_of_work_id, lesson_id, auth_user):

    str_select = "SELECT " \
                 " ref.id as id," \
                 " ref.title as title," \
                 " ref.publisher as publisher," \
                 " ref.year_published as year_published," \
                 " ref.authors as authors," \
                 " ref.url as uri," \
                 " le_ref.id as page_id," \
                 " le_ref.page_notes," \
                 " le_ref.page_url," \
                 " le_ref.task_icon " \
                 "FROM sow_reference as ref " \
                 "INNER JOIN sow_lesson as le ON le.scheme_of_work_id = ref.scheme_of_work_id AND le.id = {lesson_id} " \
                 "LEFT JOIN sow_lesson__has__references as le_ref ON le_ref.lesson_id = le.id AND le_ref.reference_id = ref.id " \
                 "LEFT JOIN sow_reference_type as ref_type ON ref.reference_type_id = ref_type.id " \
                 "WHERE ref.scheme_of_work_id = {scheme_of_work_id}" \
                 " OR (ref.published = 1 OR ref.created_by = {auth_user}) " \
                 "ORDER BY reference_type_id, title, authors;"

    str_select = str_select.format(auth_user=to_db_null(auth_user), scheme_of_work_id=int(scheme_of_work_id), lesson_id=int(lesson_id))

    rows = []
    execSql(db, str_select, rows)

    data = []

    for row in rows:
        model = ReferenceModel(id_=row[0], reference_type_id=row[1], reference_type_name = row[2], title=row[3], publisher=row[4], year_published=row[5], authors=row[6], uri=row[7], scheme_of_work_id = scheme_of_work_id)
        model.page_id = row[8]
        model.page_note = row[9] if row[9] is not None else ''
        model.page_uri = row[10] if row[10] is not None else ''
        model.task_icon = row[11] if row[11] is not None else ''
        data.append(model.__dict__)

    return data


def get_number_of_resources(db, lesson_id, auth_user):
    """
    get the number of resources for the lesson
    :param db: database context
    :param learning_epsiode_id:
    :param auth_user:
    :return:
    """
    select_sql = "SELECT " \
                 " lesson_id " \
                 "FROM sow_resource "\
                 "WHERE lesson_id = {lesson_id};"

    select_sql = select_sql.format(lesson_id=lesson_id)

    rows = []
    execSql(db, select_sql, rows)

    return len(rows)


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
    """ updates the sow_lesson and sow_lesson__has__topics """

    # 1. Update the lesson

    str_update = "UPDATE sow_reference SET reference_type_id = {reference_type_id}, title = '{title}', authors = '{authors}', publisher = '{publisher}', year_published = {year_published}, url = '{uri}', scheme_of_work_id = {scheme_of_work_id} WHERE id = {id};"
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

    str_insert = "INSERT INTO sow_reference (reference_type_id, title, authors, publisher, year_published, url, scheme_of_work_id, created, created_by) VALUES ({reference_type_id}, '{title}', '{authors}', '{publisher}', {year_published}, '{uri}', {scheme_of_work_id}, '{created}', {created_by});"
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


def _delete(db, id_):
    str_delete = "DELETE FROM sow_reference WHERE id = {id_};"
    str_delete = str_delete.format(id_=int(id_))

    rval = db.executesql(str_delete)

    return rval
