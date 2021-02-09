# -*- coding: utf-8 -*-
import json
from uuid import uuid1
from shared.models.core.basemodel import BaseModel, try_int
from shared.models.core.db_helper import ExecHelper, sql_safe, to_empty
from shared.models.core.log_handlers import handle_log_exception, handle_log_info, handle_log_warning, handle_log_error


class KeywordModel(BaseModel):
    
    id = 0
    term = ""
    definition = ""
    scheme_of_work_id = 0
    belongs_to_lessons = []
    number_of_lessons = 0

    exception_handler=None
    warning_handler=None
    info_handler=None
    
    def __init__(self, id_ = 0, term = "", definition = "", scheme_of_work_id = 0, created = "", created_by_id = 0, created_by_name = "", published=1, is_from_db=False, all_terms = []):

        super().__init__(id_, definition, created, created_by_id, created_by_name, published, is_from_db)
        self.id = id_
        self.term = term
        self.definition = definition
        self.scheme_of_work_id = try_int(scheme_of_work_id)
        self.belongs_to_lessons = []
        self.number_of_lessons = 0
        self.published = try_int(published)
        self.all_terms = []


    def from_dict(self, dict_obj, scheme_of_work_id):
    
        if type(dict_obj) is not dict:
            raise TypeError("dict_json Type is {}. Value <{}> must be type dictionary (dict).".format(type(dict_obj), dict_obj))

        self.id = dict_obj["id"]
        self.term = dict_obj["term"]
        self.definition = dict_obj["definition"]
        self.scheme_of_work_id = scheme_of_work_id
        self.published = dict_obj["published"]
        
        self.validate()
        
        return self 


    def from_json(self, str_json, scheme_of_work_id, encoding="utf8"):
        """ takes a json string and creates an instance of this object """
        if type(str_json) is not str:
            raise TypeError("str_json Type is {}. Value <{}> must be type string (str).".format(type(str_json), str_json))
        
        dict_obj = json.loads(str_json)

        return self.from_dict(dict_obj, scheme_of_work_id)


    def validate(self, skip_validation = []):
        """ clean up and validate model """
        super().validate(skip_validation)

        # do not validate deleted items
        if self.published == 2:
            self.is_valid = True;
            self.on_after_validate()
            return

        # validate title
        self._validate_required_string("term", self.term, 1, 100)
        self._validate_regular_expression("term", self.term, r"[^0-9,;!-())]([A-Za-z0-9 ()\-/)]+)?", "value must be alphanumeric, but start with or be a number")

        # validate defintion
        self._validate_optional_string("definition", self.definition, 250)

        # validate required scheme_of_work_id
        self._validate_required_integer("scheme_of_work_id", self.scheme_of_work_id, 1, 99999)

        if self.published != 2:
            # 299 validate duplicates
            self._validate_duplicate("term", self.term, self.all_terms, "Cannot save duplicate term")
        
        self.on_after_validate()
        

    def _clean_up(self):
        """ clean up properties by removing by casting and ensuring safe for inserting etc """
        # id
        self.id = int(self.id)

        # trim term
        if self.term is not None:
            self.term = sql_safe(self.term)

        # trim definition
        if self.definition is not None:
            self.definition = sql_safe(self.definition)
        else:
            self.definition = ""


    @staticmethod
    def get_model(db, id, scheme_of_work_id, auth_user):
        rows = KeywordDataAccess.get_model(db, id, scheme_of_work_id, auth_user_id=auth_user.id)
        
        model = KeywordModel(0, "", "")
        for row in rows:
            model = KeywordModel(row[0], row[1], row[2], row[3], published=row[4])
            model.on_fetched_from_db()

        return model


    @staticmethod
    def get_options(db, scheme_of_work_id, auth_user, exclude_id = 0):
        rows = KeywordDataAccess.get_options(db, scheme_of_work_id, auth_user_id=auth_user.id, exclude_id=exclude_id)

        data = []
        for row in rows:
            item = KeywordModel(row[0], term=row[1], definition=row[2], scheme_of_work_id=row[3], published=row[4])
            item.number_of_lessons = row[5]
            item.created = row[6]

            data.append(item)
            
        return data


    @staticmethod
    def get_all(db, scheme_of_work_id, lesson_id, auth_user):
        
        rows = []

        if lesson_id > 0:
            rows = KeywordDataAccess.get_lesson_all(db, scheme_of_work_id, lesson_id, auth_user_id=auth_user.id)
        else:
            rows = KeywordDataAccess.get_all(db, scheme_of_work_id, auth_user.id)
        data = []
        for row in rows:
            data.append(KeywordModel(row[0], row[1], row[2], row[3], published=row[4]))
        return data


    @staticmethod
    def get_by_terms(db, key_words_list, allow_all, scheme_of_work_id, auth_user):
        rows = KeywordDataAccess.get_by_terms(db, key_words_list, allow_all, scheme_of_work_id, auth_user_id=auth_user.id)

        data = []

        for row in rows:
            data.append(KeywordModel(row[0], term=row[1], definition=row[2], scheme_of_work_id=row[3], published=row[4], created=row[5]))

        return data


    @staticmethod
    def save(db, model, auth_user):
        """ save model """
        if model.published == 2:
            data = KeywordDataAccess.delete(db, model.id, model.scheme_of_work_id, auth_user_id=auth_user.id)
        else:
            if model.is_new():
                data = KeywordDataAccess._insert(db, model, model.scheme_of_work_id, model.published, auth_user_id=auth_user.id)
                model.id = data[0]
            else:
                data = KeywordDataAccess._update(db, model, model.scheme_of_work_id, model.published, auth_user_id=auth_user.id)
            
            for lesson_id in model.belongs_to_lessons:
                KeywordDataAccess.upsert_lesson(db, model.id, lesson_id, model.scheme_of_work_id, auth_user_id=auth_user.id)

        return model


    @staticmethod
    def delete(db, model, auth_user):
        return KeywordDataAccess.delete(db, model.id, model.scheme_of_work_id, auth_user_id=auth_user.id)


    @staticmethod
    def delete_unpublished(db, scheme_of_work_id, auth_user):
        rows = KeywordDataAccess.delete_unpublished(db, scheme_of_work_id, auth_user_id=auth_user.id)
        return rows


    @staticmethod
    def publish_by_id(db, id, auth_user):
        return KeywordDataAccess.publish(db, auth_user_id=auth_user.id, id_=id)        
        

    @staticmethod
    def merge_duplicates(db, id, scheme_of_work_id, auth_user):
        merged_model = KeywordModel.get_model(db, id, scheme_of_work_id, auth_user=auth_user)
        KeywordDataAccess.merge_duplicates(db, merged_model, scheme_of_work_id, auth_user_id=auth_user.id)
        return merged_model


class KeywordDataAccess:

    @staticmethod
    def get_options(db, scheme_of_work_id, auth_user_id, exclude_id = 0):
        """
        Get list of options
        :param db:
        :scheme_of_work_id: scheme of work
        :auth_user_id: authorised user id
        :exclude_id: used to excluce current option
        :return: term and definition
        """
        execHelper = ExecHelper()
        
        select_sql = "keyword__get_options"
        params = (scheme_of_work_id, exclude_id, auth_user_id)
        rows = []
        #271 Stored procedure (get_options)
        rows = execHelper.select(db, select_sql, params, rows, handle_log_info)
        return rows


    @staticmethod
    def get_model(db, id, scheme_of_work_id, auth_user_id):
        """
        Get a full list of terms and definitions
        :param db:
        :param id: keyword id
        :return: term and defintion
        """
        execHelper = ExecHelper()

        select_sql = "keyword__get"
        
        params = (id, scheme_of_work_id, auth_user_id)

        rows = []

        #271 Stored procedure
        rows = execHelper.select(db, select_sql, params, rows, handle_log_info)
    
        return rows


    @staticmethod
    def get_all(db, scheme_of_work_id, auth_user_id):
        """
        Get a full list of terms and definitions
        :param db: database context
        :return: list of terms and defintion
        """
        execHelper = ExecHelper()

        select_sql = "scheme_of_work__get_all_keywords"

        params = (scheme_of_work_id, auth_user_id)
        
        rows = []
        
        # 271 Stored procedure
        rows = execHelper.select(db, select_sql, params, rows, handle_log_info)

        return rows


    @staticmethod
    def get_lesson_all(db, scheme_of_work_id, lesson_id, auth_user_id):
        """
        Get a full list of terms and definitions
        :param db: database context
        :return: list of terms and defintion
        """
        execHelper = ExecHelper()

        select_sql = "lesson__get_all_keywords"

        params = (lesson_id, auth_user_id)
        
        rows = []
        
        # 271 Stored procedure
        rows = execHelper.select(db, select_sql, params, rows, handle_log_info)

        return rows


    @staticmethod
    def get_by_terms(db, key_words_list, allow_all, scheme_of_work_id, auth_user_id):
        """
        Get a full list of terms and definitions
        :param db:
        :param key_words_list: not seperated keywords
        :return: list of terms and defintion
        """
        execHelper = ExecHelper()
    
        if len(key_words_list) == 0 and allow_all == False:
            return []
    

        select_sql = "keyword__get_by_term"
        params = ("", scheme_of_work_id, auth_user_id)

        ' remove whitespace and use lower'
        key_words_list = key_words_list.replace(' , ', ',').replace(', ', ',').replace(' ,', ',').lower()

        if len(key_words_list) > 0:
            params = ("','".join(sql_safe(key_words_list).split(',')), scheme_of_work_id, auth_user_id)
    
    
        rows = []
        #271 Stored procedure
        rows = execHelper.select(db, select_sql, params, rows, handle_log_info)

        return rows


    @staticmethod
    def _insert(db, model, scheme_of_work_id, published, auth_user_id):
        """ Inserts key word and definition """

        execHelper = ExecHelper()

        stored_procedure = "keyword__insert"

        params = (model.id, model.term, model.definition, scheme_of_work_id, auth_user_id, published)    
    
        new_id = execHelper.insert(db,
            stored_procedure
            , params
            , handle_log_info
        )
        
        return new_id


    @staticmethod
    def _update(db, model, scheme_of_work_id, published, auth_user_id):
        """ Inserts key word and definition """
        
        execHelper = ExecHelper()
        
        str_update = "keyword__update"
        
        params = (model.id, model.term, model.definition, scheme_of_work_id, published, auth_user_id)
        
        execHelper.update(db, str_update, params, handle_log_info)

        return model
 

    @staticmethod
    def delete(db, id, scheme_of_work_id, auth_user_id):
        """ Delete the keyword by term """

        execHelper = ExecHelper()
        
        str_delete = "keyword__delete"
            
        params = (id, scheme_of_work_id, auth_user_id)

        rval = execHelper.delete(db, str_delete, params, handle_log_info)
        return rval


    @staticmethod
    def delete_unpublished(db, scheme_of_work_id, auth_user_id):
        """ Delete all unpublished keywords for the scheme of work"""

        execHelper = ExecHelper()
        
        str_delete = "keyword__delete_unpublished"
        params = (scheme_of_work_id, auth_user_id)
    
        rval = execHelper.delete(db, str_delete, params, handle_log_info)
        return rval


    @staticmethod
    def publish(db, auth_user_id, id_):
        
        model = KeywordModel(id_)
        model.publish = True

        execHelper = ExecHelper()

        str_update = "keyword__publish"
        
        params = (model.id, model.published, auth_user_id)

        rval = []
        rval = execHelper.update(db, str_update, params, handle_log_info)

        return rval


    @staticmethod
    def upsert_lesson(db, keyword_id, lesson_id, scheme_of_work_id, auth_user_id):
        """ Checks if the keyword already belongs to the lesson and inserts accordingly """
        execHelper = ExecHelper()
            
        str_upsert = "lesson__insert_keywords"
        
        params = (keyword_id, lesson_id, scheme_of_work_id, auth_user_id)

        rval = []
        rval = execHelper.insert(db, str_upsert, params, handle_log_info)

        return rval



    @staticmethod
    def merge_duplicates(db, model, scheme_of_work_id, auth_user_id):
        """ Inserts key word and definition """

        execHelper = ExecHelper()

        stored_procedure = "keyword__merge_duplicates"
        params = (model.id, scheme_of_work_id, auth_user_id)
        execHelper.add_custom(stored_procedure, params)
    
        rval = execHelper.custom(db,
            stored_procedure
            , handle_log_info
        )
        
        return rval
