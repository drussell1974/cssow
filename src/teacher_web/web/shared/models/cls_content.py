# -*- coding: utf-8 -*-
from .core.basemodel import BaseModel, BaseDataAccess
from .core.db_helper import ExecHelper, sql_safe
from .core.log import handle_log_info


class ContentModel(BaseModel):
    def __init__(self, id_ = 0, description = "", letter_prefix = "", key_stage_id = 0, created = "", created_by_id = 0, created_by_name = "", published=1):
        #231: implement across all classes
        super().__init__(id_, description, created, created_by_id, created_by_name, published)
        self.id = id_
        self.description = description
        self.letter_prefix = letter_prefix
        self.key_stage_id = key_stage_id


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


    def validate(self):
        """ clean up and validate model """

        self._on_before_validate()

        # clean properties before validation
        self._clean_up()

        # validate description
        self._validate_required_string("description", self.description, 1, 500)

        # validate letter prefix
        self._validate_required_string("letter_prefix", self.letter_prefix, 1, 1)
        self._validate_regular_expression("letter_prefix", self.letter_prefix, r"([A-Z]+)?", "value must be an uppercase letter")


    @staticmethod
    def get_model(db, content_id, auth_user):
        rows = ContentDataAccess.get_model(db, content_id, auth_user)
        model = None
        for row in rows:
            model = ContentModel(row[0], row[1], row[2], published=row[3])
        return model


    @staticmethod
    def get_options(db, key_stage_id):
        rows = ContentDataAccess.get_options(db, key_stage_id)
        data = []
        for row in rows:
            model = ContentModel(row[0], row[1], row[2])
            data.append(model)
        return data


    @staticmethod
    def get_all(db, key_stage_id, auth_user):
        rows = ContentDataAccess.get_all(db, key_stage_id, auth_user)
        data = []
        for row in rows:
            model = ContentModel(row[0], row[1], row[2], published=row[3])
            data.append(model)
        return data


    @staticmethod
    def save(db, model, auth_user, published):
        ''' Upsert the content (use BaseModel.upsert) '''
        model = ContentModel.upsert(db, model, auth_user, published, ContentDataAccess)
        return model


class ContentDataAccess(BaseDataAccess):

    @staticmethod
    def get_options(db, key_stage_id):

        execHelper = ExecHelper()

        str_select = "SELECT cnt.id as id, cnt.description as description, cnt.letter as letter_prefix FROM sow_content as cnt WHERE key_stage_id = {};".format(int(key_stage_id))

        rows = []
        rows = execHelper.execSql(db, str_select, rows, handle_log_info)
        return rows



    @staticmethod
    def get_model(db, content_id, auth_user):
        """
        Get a full list of terms and definitions
        :param db:
        :param id: content id
        :return: content description and letter prefix
        """
        execHelper = ExecHelper()

        select_sql = "SELECT id as id, description as description, letter as letter_prefix, published as published "\
            "FROM sow_content WHERE id = {id} AND (published = 1 or created_by = {auth_user});".format(id=sql_safe(content_id), auth_user=sql_safe(auth_user))

        rows = []
        rows = execHelper.execSql(db, select_sql, rows, log_info=handle_log_info)

        return rows


    @staticmethod
    def get_all(db, key_stage_id, auth_user):
        """
        Get a full list of content
        :param db: database context
        :return: list of curriculum / course content in letter prefix order
        """
        execHelper = ExecHelper()

        select_sql = "SELECT id as id, description as description, letter as letter_prefix, published as published "\
            "FROM sow_content WHERE key_stage_id = {key_stage_id} AND (published = 1 or created_by = {auth_user}) ORDER BY letter ASC;".format(key_stage_id=sql_safe(key_stage_id), auth_user=sql_safe(auth_user))
            
        rows = []
        rows = execHelper.execSql(db, select_sql, rows, log_info=handle_log_info)

        return rows


    @staticmethod
    def _insert(db, model, auth_user):
        """ Inserts content description and letter_prefix """

        sql_insert_statement = "INSERT INTO sow_content (description, letter, key_stage_id, created_by, published) VALUES ('{description}', '{letter}', {key_stage_id}, {created_by}, {published});"\
            .format(
                description=sql_safe(model.description), 
                letter=sql_safe(model.letter_prefix), 
                key_stage_id=sql_safe(model.key_stage_id),
                created_by=sql_safe(auth_user),
                published=sql_safe(model.published)
            )
    

        rows, new_id = BaseDataAccess._insert(db, sql_insert_statement)
        

        return rows, new_id


    @staticmethod
    def _update(db, model, auth_user):
        """ Updates content description and letter_prefix """
                
        return BaseDataAccess._update(db, 
            "UPDATE sow_content SET description = '{description}', letter = '{letter}', published = {published} WHERE id = {id};"\
                .format(
                    description=model.description, 
                    letter=model.letter_prefix, 
                    published=model.published,
                    id=model.id)
        )
 

    @staticmethod
    def _delete(db, model, auth_user):
        """ Delete the content """
        
        return BaseDataAccess._delete(db, 
            "DELETE FROM sow_content WHERE id = {id} AND published IN (0,2);".format(id=model.id)
        )