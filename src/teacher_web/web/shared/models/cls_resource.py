# -*- coding: utf-8 -*-
import markdown
from .core.basemodel import BaseModel, try_int
from .core.db_helper import ExecHelper, BaseDataAccess, sql_safe
from shared.models.core.log_handlers import handle_log_info
from shared.models.enums.publlished import STATE
from datetime import datetime
from .core.db_helper import to_empty

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

    def __init__(self, id_, lesson_id = 0, scheme_of_work_id = 0, title="", publisher="", page_note="", page_uri="", md_document_name="", type_id = 0, type_name = "", type_icon = "", last_accessed = "", is_expired = False, created = "", created_by_id = 0, created_by_name = "", published=STATE.PUBLISH, is_from_db=False, ctx=None):
        
        super().__init__( id_, title, created, created_by_id, created_by_name, published, is_from_db, ctx=ctx)
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


    def validate(self, skip_validation = []):
        """ clean up and validate model """
        super().validate(skip_validation)

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
        rows = ResourceDataAccess.get_model(db, resource_id, lesson_id, scheme_of_work_id, auth_user_id=auth_user.auth_user_id, show_published_state=auth_user.can_view)
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
        rows =  ResourceDataAccess.get_all(db, scheme_of_work_id, lesson_id, auth_user_id=auth_user.auth_user_id, resource_type_id=resource_type_id, show_published_state=auth_user.can_view)
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
        value = ResourceDataAccess.get_number_of_resources(db, lesson_id, auth_user_id=auth_user.auth_user_id)
        return value


    @staticmethod
    def get_resource_type_options(db, auth_user):
        rows = ResourceDataAccess.get_resource_type_options(db, auth_user_id=auth_user.auth_user_id)
        return rows


    @staticmethod
    def save(db, model, auth_user, published=STATE.PUBLISH):
        if try_int(published) == STATE.DELETE:
            rval = ResourceDataAccess._delete(db, model, auth_user.auth_user_id)
            # TODO: check row count before updating
            model.published = STATE.DELETE
        else:
            if model.is_new() == True:
                new_id = ResourceDataAccess._insert(db, model, published, auth_user_id=auth_user.auth_user_id)
                model.id = new_id[0]
            else:
                rows = ResourceDataAccess._update(db, model, published, auth_user_id=auth_user.auth_user_id)

        return model


    @staticmethod
    def publish_item(db, resource_id, scheme_of_work_id, auth_user):
        return ResourceDataAccess.publish_item(db, resource_id, scheme_of_work_id, auth_user_id=auth_user.auth_user_id)


    @staticmethod
    def delete(db, resource_id, auth_user):
        return ResourceDataAccess.delete(db, resource_id, auth_user.auth_user_id)


    @staticmethod
    def delete_unpublished(db, lesson_id, auth_user):
        return ResourceDataAccess.delete_unpublished(db, lesson_id, auth_user_id=auth_user.auth_user_id)


class ResourceDataAccess:

    @staticmethod
    #248 Added parameters
    def get_model(db, id_, lesson_id, scheme_of_work_id, auth_user_id, show_published_state=STATE.PUBLISH):
        """ Get Resource """

        execHelper = ExecHelper()
        
        str_select = "lesson_resource__get"
        params = (id_, int(show_published_state), auth_user_id)

        rows = []
        #271 Stored procedure
        rows = execHelper.select(db, str_select, params, rows, handle_log_info)
        return rows


    @staticmethod
    def get_all(db, scheme_of_work_id, lesson_id, auth_user_id, show_published_state=STATE.PUBLISH, resource_type_id = 0):
        """ Get resources for lesson """

        execHelper = ExecHelper()

        str_select = "lesson_resource__get_all"
        params = (lesson_id, resource_type_id, int(show_published_state), auth_user_id)

        rows = []
        #271 Stored procedure
        rows = execHelper.select(db, str_select, params, rows, handle_log_info)
        return rows


    @staticmethod
    def delete(db, id_, auth_user_id):
        """
        :param db: the database context
        :param id_: the id of the record to delete
        :return: nothing
        """

        model = ResourceModel(id_)
        
        return ResourceDataAccess._delete(db, model, auth_user_id);


    @staticmethod
    def _insert(db, model, published, auth_user_id):
        """ inserts the sow_resource and sow_scheme_of_work__has__reference """
        execHelper = ExecHelper()

        sql_insert_statement = "lesson_resource__insert"
        params = (
            model.id,
            model.title,
            model.publisher,
            model.type_id,
            model.page_note,
            model.page_uri,
            model.md_document_name,
            model.is_expired,
            model.lesson_id,
            model.created,
            model.created_by_id,
            int(published),
            auth_user_id
        )
               
        result = execHelper.insert(db, sql_insert_statement, params, handle_log_info)

        return result


    @staticmethod
    def _update(db, model, published, auth_user_id):
        """ updates the sow_lesson and sow_lesson__has__topics """
        
        execHelper = ExecHelper()
        
        str_update = "lesson_resource__update"
        params = (
            model.id,
            model.title,
            model.publisher,
            model.type_id,
            model.page_note,
            model.page_uri,
            model.md_document_name,
            model.is_expired,
            model.lesson_id,
            int(published),
            auth_user_id
        )
        
        result = execHelper.update(db, str_update, params, handle_log_info)

        return result


    @staticmethod
    def _delete(db, model, auth_user_id):

        execHelper = ExecHelper()

        sql = "lesson_resource__delete"
        params = (model.id, auth_user_id)
    
        #271 Stored procedure
        rows = execHelper.delete(db, sql, params, handle_log_info)
        
        return rows


    @staticmethod
    def get_resource_type_options(db, auth_user_id):
        
        execHelper = ExecHelper()

        str_select = "resource_type__get_options"
        params = (auth_user_id,)

        data = []

        rows = []
        #271 Stored procedure
        rows = execHelper.select(db, str_select, params, rows, handle_log_info)

        for row in rows:
            data.append(ResourceTypeModel(id=row[0], name=row[1]))

        return data


    @staticmethod
    def get_number_of_resources(db, lesson_id, auth_user_id):
        """
        get the number of resources for the lesson
        :param db: database context
        :param learning_epsiode_id:
        :param auth_user:
        :return:
        """
        
        execHelper = ExecHelper()
        
        select_sql = "lesson__get_number_of_resources"

        params = (lesson_id, 1, auth_user_id)

        rows = []
        #271 Stored procedure
 
        rows = execHelper.scalar(db, select_sql, rows, handle_log_info, params)

        return rows[0]


    @staticmethod
    def delete_unpublished(db, lesson_id, auth_user_id):
        """ Delete all unpublished resources """
        
        execHelper = ExecHelper()
        
        str_delete = "lesson_resource__delete_unpublished"
        params = (lesson_id, auth_user_id)
        rows = []
        #271 Stored procedure

        rows = execHelper.delete(db, str_delete, params, handle_log_info)
        return rows


    @staticmethod
    def publish_item(db, resource_id, scheme_of_work_id, auth_user_id):
        
        execHelper = ExecHelper()

        str_publish = "lesson_resource__publish_item"
        params = (resource_id, scheme_of_work_id, 1, auth_user_id)
        
        rval = execHelper.update(db, str_publish, params)

        return rval