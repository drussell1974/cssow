# -*- coding: utf-8 -*-
import json
from .core.basemodel import BaseModel, try_int
from .core.db_helper import ExecHelper, sql_safe, to_empty
from .core.log import handle_log_exception, handle_log_info, handle_log_warning, handle_log_error


class KeywordModel(BaseModel):
    
    id = 0
    term = ""
    definition = ""
    scheme_of_work_id = 0

    exception_handler=None
    warning_handler=None
    info_handler=None
    
    def __init__(self, id_ = 0, term = "", definition = "", scheme_of_work_id = 0):
        self.id = id_
        self.term = term
        self.definition = definition
        self.scheme_of_work_id = try_int(scheme_of_work_id)


    def from_dict(self, dict_obj, scheme_of_work_id):
        
        if type(dict_obj) is not dict:
            raise TypeError("dict_json Type is {}. Value <{}> must be type dictionary (dict).".format(type(dict_obj), dict_obj))

        self.id = dict_obj["id"]
        self.term = dict_obj["term"]
        self.definition = dict_obj["definition"]
        self.scheme_of_work_id = scheme_of_work_id

        # validate
        self.validate()
        

        return self 


    def from_json(self, str_json, scheme_of_work_id, encoding="utf8"):
        """ takes a json string and creates an instance of this object """
        if type(str_json) is not str:
            raise TypeError("str_json Type is {}. Value <{}> must be type string (str).".format(type(str_json), str_json))
        
        dict_obj = json.loads(str_json)

        return self.from_dict(dict_obj, scheme_of_work_id)


    def validate(self):
        """ clean up and validate model """

        self._on_before_validate()

        # clean properties before validation
        self._clean_up()

        # validate title
        self._validate_required_string("term", self.term, 1, 100)
        self._validate_regular_expression("term", self.term, r"[^0-9,;!-())]([A-Za-z0-9 ())]+)?", "value must be alphanumeric, but start with or be a number")

        # validate defintion
        self._validate_optional_string("definition", self.definition, 250)

        # validate required scheme_of_work_id
        self._validate_required_integer("scheme_of_work_id", self.scheme_of_work_id, 1, 99999)
        

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
        rows = KeywordDataAccess.get_model(db, id, scheme_of_work_id, auth_user)
        
        data = KeywordModel(0, "", "")

        for row in rows:
            data = KeywordModel(row[0], row[1], row[2], row[3])

        return data


    @staticmethod
    def get_options(db, scheme_of_work_id, auth_user):
        rows = KeywordDataAccess.get_options(db, scheme_of_work_id, auth_user)

        data = []
        for row in rows:
            item = KeywordModel(row[0], row[1], row[2], row[3])
            data.append(item)
            
        return data


    @staticmethod
    def get_all(db, scheme_of_work_id, auth_user):
        rows = KeywordDataAccess.get_all(db, scheme_of_work_id, auth_user)
        data = []
        for row in rows:
            data.append(KeywordModel(row[0], row[1], row[2], row[3]))
        return data


    @staticmethod
    def get_by_terms(db, key_words_list, allow_all, scheme_of_work_id, auth_user):
        rows = KeywordDataAccess.get_by_terms(db, key_words_list, allow_all, scheme_of_work_id, auth_user)

        data = []

        for row in rows:
            data.append(KeywordModel(row[0], row[1], row[2], row[3]))

        return data


    @staticmethod
    def save(db, model, published, auth_user):
        if model.is_new():
            data = KeywordDataAccess._insert(db, model, model.scheme_of_work_id, published, auth_user)
            model.id = data[0]            
            model.published = 2
        else:
            data = KeywordDataAccess._update(db, model, model.scheme_of_work_id, published, auth_user)

        return model


    @staticmethod
    def delete(db, id, auth_user):
        return KeywordDataAccess.delete(db, id, auth_user)


class KeywordDataAccess:


    @staticmethod
    def get_options(db, scheme_of_work_id, auth_user):
        execHelper = ExecHelper()

        select_sql = "keyword__get_options"
        params = (scheme_of_work_id, auth_user)
        rows = []
        #271 Stored procedure (get_options)
        rows = execHelper.select(db, select_sql, params, rows, handle_log_info)
        return rows


    @staticmethod
    def get_model(db, id, scheme_of_work_id, auth_user):
        """
        Get a full list of terms and definitions
        :param db:
        :param id: keyword id
        :return: term and defintion
        """
        execHelper = ExecHelper()

        select_sql = "keyword__get"
    
        params = (id, scheme_of_work_id, auth_user)

        rows = []

        #271 Stored procedure
        rows = execHelper.select(db, select_sql, params, rows, handle_log_info)

        return rows


    @staticmethod
    def get_all(db, scheme_of_work_id, auth_user):
        """
        Get a full list of terms and definitions
        :param db: database context
        :return: list of terms and defintion
        """
        execHelper = ExecHelper()

        select_sql = "keyword__get_all"

        params = (scheme_of_work_id, auth_user)
        
        rows = []
        
        #TODO: 271 Stored procedure
        rows = execHelper.select(db, select_sql, params, rows, handle_log_info)

        return rows


    @staticmethod
    def get_by_terms(db, key_words_list, allow_all, scheme_of_work_id, auth_user):
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
        params = ("", scheme_of_work_id, auth_user)

        ' remove whitespace and use lower'
        key_words_list = key_words_list.replace(' , ', ',').replace(', ', ',').replace(' ,', ',').lower()

        if len(key_words_list) > 0:
            params = ("','".join(sql_safe(key_words_list).split(',')), scheme_of_work_id, auth_user)
    
    
        rows = []
        #271 Stored procedure
        rows = execHelper.select(db, select_sql, params, rows, handle_log_info)

        return rows


    @staticmethod
    def _insert(db, model, scheme_of_work_id, published, auth_user):
        """ Inserts key word and definition """

        execHelper = ExecHelper()

        stored_procedure = "keyword__insert"

        params = (model.id, model.term, model.definition, scheme_of_work_id, auth_user, published)    
    
        new_id = execHelper.insert(db,
            stored_procedure
            , params
            , handle_log_info
        )
        
        return new_id


    @staticmethod
    def _update(db, model, scheme_of_work_id, published, auth_user):
        """ Inserts key word and definition """
        
        execHelper = ExecHelper()
        
        str_update = "keyword__update"
        
        params = (model.id, model.term, model.definition, scheme_of_work_id, published, auth_user)
    
        execHelper.update(db, str_update, params, handle_log_info)

        return model
 

    @staticmethod
    def delete(db, id, auth_user):
        """ Delete the keyword by term """

        execHelper = ExecHelper()
        
        str_delete = "keyword__delete"
            
        params = (id, auth_user)

        rval = execHelper.delete(db, str_delete, params, handle_log_info)
        return rval
