# -*- coding: utf-8 -*-
from .core.basemodel import BaseModel, try_int
from .core.db_helper import ExecHelper, BaseDataAccess, sql_safe
from shared.models.core.log_handlers import handle_log_info
from shared.models.enums.publlished import STATE

class ContentModel(BaseModel):
    
    class Meta:
        permissions = [('publish_contentmodel', 'Can pubish Curriculum Content')]


    def __init__(self, id_ = 0, description = "", letter_prefix = "", key_stage_id = 0, scheme_of_work_id = None, created = "", created_by_id = 0, created_by_name = "", published=STATE.PUBLISH, is_from_db=False, ctx=None):
        #231: implement across all classes
        super().__init__(id_, description, created, created_by_id, created_by_name, published, is_from_db, ctx=ctx)
        self.id = id_
        self.description = description
        self.letter_prefix = letter_prefix
        self.key_stage_id = key_stage_id
        self.scheme_of_work_id = scheme_of_work_id


    def _clean_up(self):
        """ clean up properties by removing by casting and ensuring safe for inserting etc """

        # id
        self.id = int(self.id)

        # trim description
        if self.description is not None:
            self.description = sql_safe(self.description)


        # trim letter_prefix
        if self.letter_prefix is not None:
            self.letter_prefix = sql_safe(self.letter_prefix)


    def from_post(self, mvdict_obj):
        """ Transform multi-value dictionary to object """

        self.id = mvdict_obj["id"]
        self.description = mvdict_obj["description"]
        self.letter_prefix = mvdict_obj["letter_prefix"]
        self.key_stage_id = mvdict_obj["key_stage_id"]
        self.published = mvdict_obj["published"]

        # validate
        self.validate()

        return self 


    def validate(self, skip_validation = []):
        """ clean up and validate model """
        super().validate(skip_validation)

        # validate description
        self._validate_required_string("description", self.description, 1, 500)

        # validate letter prefix
        self._validate_required_string("letter_prefix", self.letter_prefix, 1, 1)
        self._validate_regular_expression("letter_prefix", self.letter_prefix, r"([A-Z]+)?", "value must be an uppercase letter")


    @staticmethod
    def get_model(db, content_id, scheme_of_work_id, auth_user):
        rows = ContentDataAccess.get_model(db, content_id, scheme_of_work_id, auth_user_id=auth_user.auth_user_id)
        model = None
        for row in rows:
            model = ContentModel(row[0], row[1], row[2], published=row[3])
            model.on_fetched_from_db()
        return model


    @staticmethod
    def get_options(db, key_stage_id, auth_user, scheme_of_work_id = 0):
        rows = ContentDataAccess.get_options(db, key_stage_id, auth_user_id=auth_user.auth_user_id, scheme_of_work_id=scheme_of_work_id)
        data = []
        for row in rows:
            model = ContentModel(row[0], row[1], row[2])
            data.append(model)
        return data


    @staticmethod
    def get_all(db, scheme_of_work_id, key_stage_id, auth_user):
        rows = ContentDataAccess.get_all(db, scheme_of_work_id, key_stage_id, auth_user_id=auth_user.auth_user_id)
        data = []
        for row in rows:
            model = ContentModel(row[0], row[1], row[2], published=row[3])
            data.append(model)
        return data


    @staticmethod
    def save(db, model, auth_user, published=STATE.PUBLISH):
        if try_int(published) == STATE.DELETE:
            rval = ContentDataAccess._delete(db, model, auth_user.auth_user_id)
            if rval == 0:
                raise Exception("The item is either in use or you are not permitted to perform this action.")
            # TODO: check row count before updating
            model.published = STATE.DELETE
        else:
            if model.is_new() == True:
                model = ContentDataAccess._insert(db, model, published, auth_user_id=auth_user.auth_user_id)
            else:
                model = ContentDataAccess._update(db, model, published, auth_user_id=auth_user.auth_user_id)

        return model

    @staticmethod
    def delete_unpublished(db, scheme_of_work_id, auth_user):
        return ContentDataAccess.delete_unpublished(db, scheme_of_work_id, auth_user_id=auth_user.auth_user_id)


class ContentDataAccess(BaseDataAccess):

    @staticmethod
    def get_options(db, key_stage_id, auth_user_id, scheme_of_work_id = 0):

        execHelper = ExecHelper()

        #270 get ContentModel.get_options by scheme_of_work (look up many-to-many)
        str_select = "content__get_options"
        params = (scheme_of_work_id, key_stage_id, auth_user_id)

        rows = []
        #271 Stored procedure (get_options)
        rows = execHelper.select(db, str_select, params, rows, handle_log_info)
        return rows



    @staticmethod
    def get_model(db, content_id, scheme_of_work_id, auth_user_id):
        """
        Get a full list of terms and definitions
        :param db:
        :param id: content id
        :param scheme_of_work_id: CURRENTLY NOT USED
        :return: content description and letter prefix
        """
        execHelper = ExecHelper()

        select_sql = "content__get"
        params = (content_id, scheme_of_work_id, auth_user_id)

        rows = []
        #271 Stored procedure
        rows = execHelper.select(db, select_sql, params, rows, handle_log_info)

        return rows


    @staticmethod
    def get_all(db, scheme_of_work_id, key_stage_id, auth_user_id):
        """
        Get a full list of content
        :param db: database context
        :return: list of curriculum / course content in letter prefix order
        """
        execHelper = ExecHelper()

        select_sql = "content__get_all"
        params = (scheme_of_work_id, key_stage_id, auth_user_id)
            
        rows = []
        #271 Stored procedure
        rows = execHelper.select(db, select_sql, params, rows, handle_log_info)

        return rows


    @staticmethod
    def _insert(db, model, published, auth_user_id):
        """ Inserts content description and letter_prefix """
        
        execHelper = ExecHelper()

        sql_insert_statement = "content__insert"
        params = (
            model.id,
            model.description,
            model.letter_prefix,
            model.key_stage_id,
            model.scheme_of_work_id,
            published,
            auth_user_id
        )
    
        new_id = execHelper.insert(db, sql_insert_statement, params, handle_log_info)

        return new_id


    @staticmethod
    def _update(db, model, published, auth_user_id):
        """ Updates content description and letter_prefix """
        
        execHelper = ExecHelper()

        stored_procedure = "content__update"
        params = (
            model.id,
            model.description, 
            model.letter_prefix, 
            model.key_stage_id,
            model.scheme_of_work_id,
            published,
            auth_user_id
        )

        rows = execHelper.update(db, stored_procedure, params, handle_log_info)

        return rows
 

    @staticmethod
    def _delete(db, model, auth_user_id):
        """ Delete the content """

        execHelper = ExecHelper()

        stored_procedure = "content__delete"
        params = (model.id, model.scheme_of_work_id, auth_user_id)

        rows = execHelper.delete(db, stored_procedure, params, handle_log_info)

        return rows


    @staticmethod
    def delete_unpublished(db, scheme_of_work_id, auth_user_id):
        """ 
        Delete all unpublished content 

        :param db: the database context
        :param scheme_of_work_id: the scheme of work identifier
        :param auth_user_id: the user executing the command
        :return: the rows
        """

        execHelper = ExecHelper()
        
        str_delete = "content__delete_unpublished"
        params = (scheme_of_work_id, auth_user_id)
        
        rows = []
        rows = execHelper.delete(db, str_delete, params, handle_log_info)
        
        return rows