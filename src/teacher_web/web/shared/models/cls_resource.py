# -*- coding: utf-8 -*-
import markdown
from .core.basemodel import BaseModel, BaseDataAccess, try_int
from .core.db_helper import ExecHelper, sql_safe
from .core.log import handle_log_info
from datetime import datetime
from .core.db_helper import to_db_null, to_empty, to_db_bool



class ResourceTypeModel:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class ResourceModel (BaseModel):
        
    id = 0
    title = ""
    lesson_id = 0
    md_document_name = ""
    page_note = ""
    page_uri = ""
    publisher = ""
    type_id = 0
    type_name = ""
    # default Get this from settings
    MARKDOWN_TYPE_ID = 10 # default

    def __init__(self, id_, lesson_id = 0, scheme_of_work_id = 0, title="", publisher="", page_note="", page_uri="", md_document_name="", type_id = 0, type_name = "", type_icon = "", last_accessed = "", is_expired = False, created = "", created_by_id = 0, created_by_name = "", published=1, is_from_db=False):
        
        super().__init__( id_, title, created, created_by_id, created_by_name, published, is_from_db)
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
        self._validate_required_string_if("md_document_name", self.md_document_name, 1, 200, ResourceModel.is_markdown)


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


    @staticmethod
    def is_markdown(model):
        """ checks if the type_id is a markdown document """
        return model.type_id == ResourceModel.MARKDOWN_TYPE_ID


    @staticmethod
    def get_markdown_html(document_path):
        with open( document_path, "r", encoding="utf-8") as input_file:
            text = input_file.read()
            html = markdown.markdown(text)
            return html


    @staticmethod
    #248 Added parameters
    def get_model(db, resource_id, lesson_id, scheme_of_work_id, auth_user):
        rows = ResourceDataAccess.get_model(db, resource_id, lesson_id, scheme_of_work_id, auth_user)
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
            model.is_from_db = True
            data = model
        return data


    @staticmethod
    def get_all(db, scheme_of_work_id, lesson_id, auth_user, resource_type_id=0):
        rows =  ResourceDataAccess.get_all(db, scheme_of_work_id, lesson_id, auth_user, resource_type_id)
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
    def get_number_of_resources(db, lesson_id, auth_user):
        rows = ResourceDataAccess.get_number_of_resources(db, lesson_id, auth_user)
        return len(rows)


    @staticmethod
    def get_resource_type_options(db, auth_user):
        rows = ResourceDataAccess.get_resource_type_options(db, auth_user)
        return rows


    @staticmethod
    def save(db, model, auth_user, published = 1):
        ''' Upsert the resource (use BaseModel.upsert) '''
        model = ResourceModel.upsert(db, model, auth_user, published, ResourceDataAccess)
        return model


    @staticmethod
    def publish_item(db, resource_id, scheme_of_work_id, auth_user):
        return ResourceDataAccess.publish_item(db, resource_id, scheme_of_work_id, auth_user)


    @staticmethod
    def delete(db, resource_id, auth_user):
        return ResourceDataAccess.delete(db, resource_id, auth_user)


    @staticmethod
    def delete_unpublished(db, lesson_id, auth_user):
        return ResourceDataAccess.delete_unpublished(db, lesson_id, auth_user)


class ResourceDataAccess:

    @staticmethod
    #248 Added parameters
    def get_model(db, id_, lesson_id, scheme_of_work_id,auth_user):
        """ Get Resource """
        execHelper = ExecHelper()
        
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
                    " INNER JOIN sow_lesson as les ON les.id = res.lesson_id "\
                    " INNER JOIN sow_scheme_of_work as sow ON sow.id = les.scheme_of_work_id "\
                    " LEFT JOIN sow_resource_type as res_typ ON res.type_id = res_typ.id " \
                    " LEFT JOIN auth_user AS user ON user.id = res.created_by "\
                    "WHERE res.id = {id} "\
                    " AND (res.published = 1 OR res.created_by = {auth_user});"

        str_select = str_select.format(id=(id_), auth_user=to_db_null(auth_user))

        rows = []
        #TODO: #271 Stored procedure
        rows = execHelper.execSql(db, str_select, rows, log_info=handle_log_info)
        return rows


    @staticmethod
    def get_all(db, scheme_of_work_id, lesson_id, auth_user, resource_type_id = 0):
        """ Get resources for lesson """
        execHelper = ExecHelper()

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
        #TODO: #271 Stored procedure
        rows = execHelper.execSql(db, str_select, rows, log_info=handle_log_info)
        return rows


    @staticmethod
    def delete(db, id_, auth_user):
        """
        :param db: the database context
        :param id_: the id of the record to delete
        :return: nothing
        """
        model = ResourceModel(id_)
        return ResourceDataAccess._delete(db, model, auth_user);


    @staticmethod
    def _insert(db, model, auth_user_id):
        """ inserts the sow_resource and sow_scheme_of_work__has__reference """
       
        sql_insert_statement = "INSERT INTO sow_resource (title, publisher, type_id, page_notes, url, md_document_name, is_expired, lesson_id, created, created_by, published) VALUES ('{title}', '{publisher}', {type_id}, '{page_note}', '{page_uri}', '{md_document_name}', {is_expired}, {lesson_id}, '{created}', {created_by}, {published});SELECT LAST_INSERT_ID();"\
                .format(
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

        rows, new_id = BaseDataAccess._insert(db, sql_insert_statement)
        
        return rows, new_id


    @staticmethod
    def _update(db, model, auth_user_id):
        """ updates the sow_lesson and sow_lesson__has__topics """
        return BaseDataAccess._update(db, 
            "UPDATE sow_resource SET title = '{title}', publisher = '{publisher}', type_id = {type_id}, page_notes = '{page_note}', url = '{page_uri}', md_document_name = '{md_document_name}', is_expired = {is_expired}, lesson_id = {lesson_id}, published = {published} WHERE id = {id};"\
                .format(
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
        )
        return model


    @staticmethod
    def _delete(db, model, auth_user_id):
        return BaseDataAccess._delete(db,
            "DELETE FROM sow_resource WHERE id = {id_};"\
                .format(id_=model.id)
        )


    @staticmethod
    def get_resource_type_options(db, auth_user):
        
        execHelper = ExecHelper()

        str_select = "resource_type__get_options"
        params = (auth_user,)

        data = []

        rows = []
        #271 Stored procedure
        rows = execHelper.select(db, str_select, params, rows, log_info=handle_log_info)

        for row in rows:
            data.append(ResourceTypeModel(id=row[0], name=row[1]))

        return data


    @staticmethod
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
        #TODO: #271 Stored procedure
        rows = execHelper.execSql(db, select_sql, rows, log_info=handle_log_info)

        return rows


    @staticmethod
    def delete_unpublished(db, lesson_id, auth_user_id):
        """ Delete all unpublished resources """
        
        execHelper = ExecHelper()
        
        str_delete = "DELETE FROM sow_resource WHERE lesson_id = {} AND published = 0;".format(lesson_id)
            
        rows = []
        #TODO: #271 Stored procedure
        rows = execHelper.execSql(db, str_delete, rows, handle_log_info)
        return rows


    @staticmethod
    def publish_item(db, model, scheme_of_work_id, auth_user):
        
        execHelper = ExecHelper()

        str_publish = "lesson_resource__publish_item"
        params = (model.id, scheme_of_work_id, model.published, auth_user)
        
        rval = execHelper.update(db, str_publish, params)

        return rval