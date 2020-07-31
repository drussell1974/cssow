# -*- coding: utf-8 -*-
from .core.basemodel import BaseModel, try_int
from .core.db_helper import ExecHelper, sql_safe
from .core.log import handle_log_info

# TODO: Get this from settings
MARKDOWN_TYPE_ID = 10

def check_type_id(model):
    """ checks if the type_id is a markdown document """
    return model.type_id == MARKDOWN_TYPE_ID


class ResourceTypeModel:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class ResourceModel (BaseModel):
        
    def __init__(self, id_, lesson_id = 0, scheme_of_work_id = 0, title="", publisher="", page_note="", page_uri="", md_document_name="", type_id = 0, type_name = "", type_icon = "", last_accessed = "", is_expired = False, created = "", created_by_id = 0, created_by_name = "", published=1):
        
        #TODO: #231 call super().__init__(id_, created, created_by_id, created_by_name, published)
        super().__init__( id_, title, created, created_by_id, created_by_name, published)
        self.title = title
        self.publisher = publisher
        self.page_note = page_note
        self.page_uri = page_uri
        self.md_document_name = md_document_name
        self.type_id = try_int(type_id)
        self.type_name = type_name
        self.type_icon = type_icon
        self.lesson_id = lesson_id
        self.scheme_of_work_id = scheme_of_work_id
        self.last_accessed = last_accessed
        #self.created = created
        #self.created_by_id = try_int(created_by_id)
        #self.created_by_name = created_by_name
        #self.published = published
        self.is_expired = is_expired

        self.set_published_state()  


    def validate(self):

        """ clean up and validate model """

        self._on_before_validate()

        # clean properties before validation
        self._clean_up()

        # validate title
        self._validate_required_string("title", self.title, 1, 300)

        # validate type_id
        self._validate_required_integer("type_id", self.type_id, 1, 15)

        # validate publisher
        self._validate_required_string("publisher", self.publisher, 1, 500)

        # validate page_note
        self._validate_required_string("page_note", self.page_note, 1, 2500)

        # validate page_uri
        self._validate_optional_uri("page_uri", self.page_uri)

        # validate md_document_name
        self._validate_required_string_if("md_document_name", self.md_document_name, 1, 200, check_type_id)


    def _clean_up(self):
        """ clean up properties by casting and ensuring safe for inserting etc """

        self.id = int(self.id)

        # trim title
        if self.title is not None:
            self.title = sql_safe(self.title)

        # trim publisher
        if self.publisher is not None:
            self.publisher = sql_safe(self.publisher)

        # trim uri
        if self.page_uri is not None:
            self.page_uri = sql_safe(self.page_uri)

        # trim notes
        if self.page_note is not None:
            self.page_note = sql_safe(self.page_note)

        # trim md_document_name
        if self.md_document_name is not None:
            self.md_document_name = sql_safe(self.md_document_name)


class ResourceDataAccess:

    @staticmethod
    def get_model(db, id_, scheme_of_work_id, auth_user):
        """ Get Resource """
        execHelper = ExecHelper()
        #TODO: #231 get published
        str_select = "SELECT" \
                    " res.id as id," \
                    " res.title as title," \
                    " res.publisher as publisher," \
                    " res.type_id as type_id,"\
                    " res_typ.name as resource_type_name,"\
                    " res_typ.task_icon as task_icon,"\
                    " res.md_document_name as md_document_name, "\
                    " res.page_notes as page_notes, "\
                    " res.url as page_uri, " \
                    " res.lesson_id as lesson_id, "\
                    " res.created as created, "\
                    " res.created_by as created_by_id, "\
                    " CONCAT_WS(' ', user.first_name, user.last_name) as created_by_name, "\
                    " res.published as published " \
                    "FROM sow_resource AS res " \
                    " LEFT JOIN sow_resource_type as res_typ ON res.type_id = res_typ.id " \
                    " LEFT JOIN auth_user AS user ON user.id = res.created_by "\
                    "WHERE res.id = {id} " \
                    " AND (res.published = 1 OR res.created_by = {auth_user});"

        str_select = str_select.format(id=(id_), auth_user=to_db_null(auth_user))

        rows = []
        rows = execHelper.execSql(db, str_select, rows, log_info=handle_log_info)

        data = None
        
        for row in rows:
            model = ResourceModel(
                id_=row[0], 
                title=row[1], 
                publisher=row[2], 
                type_id=row[3],
                type_name=row[4],
                type_icon=row[5],
                md_document_name=to_empty(row[6]),
                page_note=row[7], 
                page_uri=row[8], 
                lesson_id=row[9],
                created = row[10],
                created_by_id = row[11],
                created_by_name = row[12], 
                published = row[13], 
                scheme_of_work_id=scheme_of_work_id)

            data = model
            

        return data


    @staticmethod
    def get_all(db, scheme_of_work_id, lesson_id, auth_user, resource_type_id = 0):
        """ Get resources for lesson """
        execHelper = ExecHelper()

        #TODO: #231 get published
        str_select = "SELECT" \
                    " res.id as id," \
                    " res.title as title," \
                    " res.publisher as publisher," \
                    " res.type_id as type_id,"\
                    " res_typ.name as resource_type_name,"\
                    " res_typ.task_icon as task_icon,"\
                    " res.md_document_name as md_document_name,"\
                    " res.page_notes as page_notes, "\
                    " res.url as page_uri, " \
                    " res.lesson_id as lesson_id, "\
                    " res.created as created, "\
                    " res.created_by as created_by_id, "\
                    " CONCAT_WS(' ', user.first_name, user.last_name) as created_by_name, "\
                    " res.published as published "\
                    "FROM sow_resource AS res " \
                    " LEFT JOIN sow_resource_type as res_typ ON res.type_id = res_typ.id " \
                    " LEFT JOIN auth_user AS user ON user.id = res.created_by "\
                    "WHERE res.lesson_id = {lesson_id} AND (res.type_id = {resource_type_id} or {resource_type_id} = 0)" \
                    " AND (res.published = 1 OR res.created_by = {auth_user});"
                    
        str_select = str_select.format(auth_user=to_db_null(auth_user), scheme_of_work_id=int(scheme_of_work_id), lesson_id=int(lesson_id), resource_type_id=int(resource_type_id))

        rows = []
        rows = execHelper.execSql(db, str_select, rows, log_info=handle_log_info)

        data = []
        
        for row in rows:
            model = ResourceModel(
                id_=row[0], 
                title=row[1], 
                publisher=row[2], 
                type_id=row[3],
                type_name=row[4],
                type_icon=row[5],
                md_document_name=row[6], 
                page_note=row[7], 
                page_uri=row[8], 
                lesson_id=row[9],
                created = row[10],
                created_by_id = row[11],
                created_by_name = row[12],
                published = row[13], 
                scheme_of_work_id=scheme_of_work_id)

            # TODO: remove __dict__ . The object should be serialised to json further up the stack
            data.append(model.__dict__)

        return data


    @staticmethod
    def save(db, model, auth_user, published=1):
        '''
        Upsert the reference
        :param db: database context
        :param model: the ReferenceModel
        :return: the updated ReferenceModel
        '''
        #TODO: #231: Add delete        
        if published == 2:
            ResourceDataAccess._delete(db, model.id, auth_user)
            model.published = 2
        else:
            
            if model.is_new() == True:
                model = ResourceDataAccess._insert(db, model, auth_user)
            else:
                model = ResourceDataAccess._update(db, model, auth_user)

        return model


    @staticmethod
    def delete(db, id_, auth_user):
        """
        :param db: the database context
        :param id_: the id of the record to delete
        :return: nothing
        """
        return ResourceDataAccess._delete(db, id_, auth_user);


    @staticmethod
    def _insert(db, model, auth_user_id):
        """ inserts the sow_resource and sow_scheme_of_work__has__reference """
        execHelper = ExecHelper()

        ## 1. Insert the reference

        str_insert = "INSERT INTO sow_resource (title, publisher, type_id, page_notes, url, md_document_name, is_expired, lesson_id, created, created_by, published) VALUES ('{title}', '{publisher}', {type_id}, '{page_note}', '{page_uri}', '{md_document_name}', {is_expired}, {lesson_id}, '{created}', {created_by}, {published});SELECT LAST_INSERT_ID();"
        str_insert = str_insert.format(
            title=model.title,
            publisher=model.publisher,
            type_id=to_db_null(model.type_id, as_null=""),
            page_note=to_db_null(model.page_note),
            page_uri=to_db_null(model.page_uri),
            md_document_name=to_db_null(model.md_document_name, as_null=""),
            is_expired=to_db_bool(model.is_expired),
            lesson_id = model.lesson_id,
            created=model.created,
            created_by=model.created_by_id,
            published=model.published,
            expired=model.is_expired)

        rows = []

        new_id = execHelper.execCRUDSql(db, str_insert, result=rows, log_info=handle_log_info)
    
        model.id = new_id

        return model


    @staticmethod
    def _update(db, model, auth_user_id):
        """ updates the sow_lesson and sow_lesson__has__topics """
        execHelper = ExecHelper()

        # 1. Update the lesson

        str_update = "UPDATE sow_resource SET title = '{title}', publisher = '{publisher}', type_id = {type_id}, page_notes = '{page_note}', url = '{page_uri}', md_document_name = '{md_document_name}', is_expired = {is_expired}, lesson_id = {lesson_id}, published = {published} WHERE id = {id};"
        str_update = str_update.format(
            id=model.id,
            title=model.title,
            publisher=model.publisher,
            type_id=to_db_null(model.type_id, as_null=""),
            page_note=to_db_null(model.page_note),
            page_uri=to_db_null(model.page_uri),
            md_document_name=to_db_null(model.md_document_name),
            is_expired=to_db_bool(model.is_expired),
            lesson_id = model.lesson_id,
            published=model.published)

        execHelper.execCRUDSql(db, str_update, log_info=handle_log_info)

        # 2. upsert related topics
        #if scheme_of_work_id > 0:
        #    _upsert_sow_scheme_of_work__has__reference(db, model, scheme_of_work_id)

        return model


    @staticmethod
    def _delete(db, id_, auth_user_id):
        execHelper = ExecHelper()

        str_delete = "DELETE FROM sow_resource WHERE id = {id_};"
        str_delete = str_delete.format(id_=int(id_))

        rval = []
        rval = execHelper.execCRUDSql(db, str_delete, rval, handle_log_info)

        return rval


"""
DAL
"""
from datetime import datetime
from .core.db_helper import to_db_null, to_empty, to_db_bool



def get_resource_type_options(db, auth_user):
    execHelper = ExecHelper()

    str_select = "SELECT" \
                 " type.id as id," \
                 " type.name as name " \
                 "FROM sow_resource_type as type "\
                 "WHERE type.published = 1 OR type.created_by = {auth_user};"

    str_select = str_select.format(auth_user=to_db_null(auth_user))

    data = []

    rows = []
    rows = execHelper.execSql(db, str_select, rows, log_info=handle_log_info)

    for row in rows:
        data.append(ResourceTypeModel(id=row[0], name=row[1]))

    return data

'''
def get_options(db, scheme_of_work_id, lesson_id, auth_user):
    execHelper = ExecHelper()

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
                 "FROM sow_resource as ref " \
                 "INNER JOIN sow_lesson as le ON le.scheme_of_work_id = ref.scheme_of_work_id AND le.id = {lesson_id} " \
                 "LEFT JOIN sow_lesson__has__references as le_ref ON le_ref.lesson_id = le.id AND le_ref.reference_id = ref.id " \
                 "LEFT JOIN sow_reference_type as ref_type ON ref.reference_type_id = ref_type.id " \
                 "WHERE ref.scheme_of_work_id = {scheme_of_work_id}" \
                 " OR (ref.published = 1 OR ref.created_by = {auth_user}) " \
                 "ORDER BY reference_type_id, title, authors;"

    str_select = str_select.format(auth_user=to_db_null(auth_user), scheme_of_work_id=int(scheme_of_work_id), lesson_id=int(lesson_id))

    rows = []
    rows = execHelper.execSql(db, str_select, rows)

    data = []

    for row in rows:
        model = ResourceModel(id_=row[0], title=row[1], publisher=row[2], type_id=row[1], type_name = row[2], authors=row[6], uri=row[7], scheme_of_work_id = scheme_of_work_id)
        model.page_id = row[8]
        model.page_note = row[9] if row[9] is not None else ''
        model.page_uri = row[10] if row[10] is not None else ''
        # TODO: call tojson() in basemodel ... data.append(model.tojson())
        data.append(model.__dict__)

    return data
'''


def get_number_of_resources(db, lesson_id, auth_user):
    """
    get the number of resources for the lesson
    :param db: database context
    :param learning_epsiode_id:
    :param auth_user:
    :return:
    """
    execHelper = ExecHelper()
    
    select_sql = "SELECT " \
                 " lesson_id " \
                 "FROM sow_resource "\
                 "WHERE lesson_id = {lesson_id};"

    select_sql = select_sql.format(lesson_id=lesson_id)

    rows = []
    rows = execHelper.execSql(db, select_sql, rows, log_info=handle_log_info)

    return len(rows)


def delete_unpublished(db, lesson_id, auth_user_id):
    """ Delete all unpublished lessons """

    return _delete_unpublished(db, lesson_id, auth_user_id)


def publish_item(db, id_, auth_user_id):

    model = ResourceModel(id_=id_)
    model.publish = True
    return _publish(db, model)


"""
Private CRUD functions 
"""

def _delete_unpublished(db, lesson_id, auth_user_id):
    """ Delete all unpublished resources """
    execHelper = ExecHelper()
    
    str_delete = "DELETE FROM sow_resource WHERE lesson_id = {} AND published = 0;".format(lesson_id)
        
    rows = []
    rows = execHelper.execSql(db, str_delete, rows, handle_log_info)
    return rows


def _publish(db, model):
    execHelper = ExecHelper()

    str_publish = "UPDATE sow_resource SET published = {published} WHERE id = {resource_id};"
    str_publish = str_publish.format(published=1 if model.published else 0, resource_id=model.id)
    
    rval = []
    rval = execHelper.execSql(db, str_publish, rval)

    return rval