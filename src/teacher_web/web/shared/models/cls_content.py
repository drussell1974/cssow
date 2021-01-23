# -*- coding: utf-8 -*-
from .core.basemodel import BaseModel, BaseDataAccess, try_int
from .core.db_helper import ExecHelper, sql_safe
from .core.log import handle_log_info


class ContentModel(BaseModel):
    
    class Meta:
        permissions = [('publish_contentmodel', 'Can pubish Curriculum Content')]


    def __init__(self, id_ = 0, description = "", letter_prefix = "", key_stage_id = 0, scheme_of_work_id = None, created = "", created_by_id = 0, created_by_name = "", published=1, is_from_db=False):
        #231: implement across all classes
        super().__init__(id_, description, created, created_by_id, created_by_name, published, is_from_db)
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

        #self.on__from_post(mvdict_obj)

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
        rows = ContentDataAccess.get_model(db, content_id, scheme_of_work_id, auth_user)
        model = None
        for row in rows:
            model = ContentModel(row[0], row[1], row[2], published=row[3])
            model.on_fetched_from_db()
        return model


    @staticmethod
    def get_options(db, key_stage_id, auth_user, scheme_of_work_id = 0):
        rows = ContentDataAccess.get_options(db, key_stage_id, auth_user, scheme_of_work_id)
        data = []
        for row in rows:
            model = ContentModel(row[0], row[1], row[2])
            data.append(model)
        return data


    @staticmethod
    def get_all(db, scheme_of_work_id, key_stage_id, auth_user):
        rows = ContentDataAccess.get_all(db, scheme_of_work_id, key_stage_id, auth_user)
        data = []
        for row in rows:
            model = ContentModel(row[0], row[1], row[2], published=row[3])
            data.append(model)
        return data


    @staticmethod
    def save(db, model, auth_user, published=1):
        if try_int(published) == 2:
            rval = ContentDataAccess._delete(db, model, auth_user)
            if rval == 0:
                raise Exception("The item is either in use or you are not permitted to perform this action.")
            #TODO: check row count before updating
            model.published = 2
        else:
            if model.is_new() == True:
                model = ContentDataAccess._insert(db, model, published, auth_user)
            else:
                model = ContentDataAccess._update(db, model, published, auth_user)

        return model

    @staticmethod
    def delete_unpublished(db, scheme_of_work_id, auth_user):
        pass


class ContentDataAccess(BaseDataAccess):

    @staticmethod
    def get_options(db, key_stage_id, auth_user, scheme_of_work_id = 0):

        execHelper = ExecHelper()

        #TODO: #270 get ContentModel.get_options by scheme_of_work (look up many-to-many)
        str_select = "content__get_options"
        params = (scheme_of_work_id, key_stage_id, auth_user)

        rows = []
        #271 Stored procedure (get_options)
        rows = execHelper.select(db, str_select, params, rows, handle_log_info)
        return rows



    @staticmethod
    def get_model(db, content_id, scheme_of_work_id, auth_user):
        """
        Get a full list of terms and definitions
        :param db:
        :param id: content id
        :param scheme_of_work_id: CURRENTLY NOT USED
        :return: content description and letter prefix
        """
        execHelper = ExecHelper()

        select_sql = "content__get"
        params = (content_id, scheme_of_work_id, auth_user)

        rows = []
        #271 Stored procedure
        rows = execHelper.select(db, select_sql, params, rows, handle_log_info)

        return rows


    @staticmethod
    def get_all(db, scheme_of_work_id, key_stage_id, auth_user):
        """
        Get a full list of content
        :param db: database context
        :return: list of curriculum / course content in letter prefix order
        """
        execHelper = ExecHelper()

        select_sql = "content__get_all"
        params = (scheme_of_work_id, key_stage_id, auth_user)
            
        rows = []
        #271 Stored procedure
        rows = execHelper.select(db, select_sql, params, rows, handle_log_info)

        return rows


    @staticmethod
    def _insert(db, model, published, auth_user):
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
            auth_user
        )
    
        new_id = execHelper.insert(db, sql_insert_statement, params, handle_log_info)

        return new_id


    @staticmethod
    def _update(db, model, published, auth_user):
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
            auth_user
        )

        rows = execHelper.update(db, stored_procedure, params, handle_log_info)

        return rows
 

    @staticmethod
    def _delete(db, model, auth_user):
        """ Delete the content """

        execHelper = ExecHelper()

        stored_procedure = "content__delete"
        params = (model.id, model.scheme_of_work_id, auth_user)

        rows = execHelper.delete(db, stored_procedure, params, handle_log_info)

        return rows