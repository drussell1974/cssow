# -*- coding: utf-8 -*-
import json
from .core.basemodel import BaseModel
from .core.db_helper import ExecHelper, sql_safe, to_empty
from .core.log import handle_log_exception, handle_log_info, handle_log_warning, handle_log_error


class KeywordModel(BaseModel):
    
    id = 0
    term = ""
    definition = ""

    exception_handler=None
    warning_handler=None
    info_handler=None
    
    def __init__(self, id_ = 0, term = "", definition = ""):
        self.id = id_
        self.term = term
        self.definition = definition


    def from_dict(self, dict_obj):
        
        if type(dict_obj) is not dict:
            raise TypeError("dict_json Type is {}. Value <{}> must be type dictionary (dict).".format(type(dict_obj), dict_obj))

        self.id = dict_obj["id"]
        self.term = dict_obj["term"]
        self.definition = dict_obj["definition"]  

        # validate
        self.validate()
        

        return self 


    def from_json(self, str_json, encoding="utf8"):

        if type(str_json) is not str:
            raise TypeError("str_json Type is {}. Value <{}> must be type string (str).".format(type(str_json), str_json))
        
        dict_obj = json.loads(str_json)

        return self.from_dict(dict_obj)


    def validate(self):
        """ clean up and validate model """

        self._on_before_validate()

        # clean properties before validation
        self._clean_up()

        # validate title
        self._validate_required_string("term", self.term, 1, 100)
        self._validate_regular_expression("term", self.term, r"[^0-9,!-())]([A-Za-z0-9 ())]+)?", "value must be alphanumeric, but start with or be a number")

        # validate page_uri
        self._validate_optional_string("definition", self.definition, 250)


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
    def get_model(db, id, auth_user):
        rows = KeywordDataAccess.get_model(db, id, auth_user)
        
        data = KeywordModel(0, "", "")

        for row in rows:
            data = KeywordModel(row[0], row[1], row[2])

        return data


    @staticmethod
    def get_options(db):
        return KeywordDataAccess.get_options(db)


    @staticmethod
    def get_all(db, search_term = ""):
        rows = KeywordDataAccess.get_all(db, search_term)
        data = []
        for row in rows:
            data.append(KeywordModel(row[0], row[1], to_empty(row[2])))
        return data


    @staticmethod
    def get_by_terms(db, key_words_list, allow_all, auth_user):
        rows = KeywordDataAccess.get_by_terms(db, key_words_list, allow_all, auth_user)

        data = []

        for row in rows:
            data.append(KeywordModel(row[0], row[1], row[2]))

        return data


    @staticmethod
    def save(db, model):
        if model.is_new():
            data = KeywordDataAccess._insert(db, model)
            model.id = data[1]            
            model.published = 2
        else:
            data = KeywordDataAccess._update(db, model)

        return model


    @staticmethod
    def delete(db, id):
        return KeywordDataAccess.delete(db, id)


class KeywordDataAccess:


    @staticmethod
    def get_options(db):
        execHelper = ExecHelper()

        select_sql = "SELECT id, name, definition FROM sow_key_word kw WHERE published = 1 ORDER BY name;"

        rows = []
        #TODO: #271 Stored procedure (get_options)
        rows = execHelper.execSql(db, select_sql, rows)
        
        data = []
        for row in rows:
            item = KeywordModel(row[0], row[1], row[2])
            data.append(item)
            
        return data


    @staticmethod
    def get_model(db, id, auth_user):
        """
        Get a full list of terms and definitions
        :param db:
        :param id: keyword id
        :return: term and defintion
        """
        execHelper = ExecHelper()

        select_sql = "SELECT id as id, name as term, definition as definition FROM sow_key_word kw WHERE id = {id} AND published = 1;"
        select_sql = select_sql.format(id=int(id))

        rows = []
        #TODO: #271 Stored procedure
        rows = execHelper.execSql(db, select_sql, rows, log_info=handle_log_info)

        return rows


    @staticmethod
    def get_all(db, search_term = ""):
        """
        Get a full list of terms and definitions
        :param db: database context
        :return: list of terms and defintion
        """
        execHelper = ExecHelper()

        select_sql = "SELECT id as id, name as term, definition as definition FROM sow_key_word kw WHERE published = 1"

        if len(search_term) > 0:
            select_sql = select_sql + " AND name LIKE '%{search_term}%'".format(search_term=sql_safe(search_term))

        select_sql = select_sql + " ORDER BY name;"
        
        rows = []
        #TODO: #271 Stored procedure
        rows = execHelper.execSql(db, select_sql, rows, log_info=handle_log_info)

        return rows


    @staticmethod
    def get_by_terms(db, key_words_list, allow_all, auth_user):
        """
        Get a full list of terms and definitions
        :param db:
        :param key_words_list: not seperated keywords
        :return: list of terms and defintion
        """
        execHelper = ExecHelper()
    
        if len(key_words_list) == 0 and allow_all == False:
            return []
    

        select_sql = "SELECT id as id, name as term, definition as definition FROM sow_key_word kw"

        ' remove whitespace and use upper'
        key_words_list = key_words_list.replace(' , ', ',').replace(', ', ',').replace(' ,', ',').lower()

        if len(key_words_list) > 0:
            select_sql = select_sql + " WHERE LOWER(name) IN ('{key_words}') AND published = 1".format(key_words="','".join(sql_safe(key_words_list).split(',')))

        select_sql = select_sql + " ORDER BY name;"

        rows = []
        #TODO: #271 Stored procedure
        rows = execHelper.execSql(db, select_sql, rows, log_info=handle_log_info)

        return rows


    @staticmethod
    def _insert(db, model):
        """ Inserts key word and definition """

        execHelper = ExecHelper()

        rows = []
        
        rows, new_id = execHelper.execCRUDSql(db, 
            "INSERT INTO sow_key_word (name, definition) VALUES ('{key_word}', '{definition}');".format(key_word=sql_safe(model.term), definition=sql_safe(model.definition))
            , result=rows
            , log_info=handle_log_info
        )
        
        return rows, new_id


    @staticmethod
    def _update(db, model):
        """ Inserts key word and definition """
        
        execHelper = ExecHelper()
        
        str_update = "UPDATE sow_key_word SET name = '{name}', definition = '{definition}' WHERE id = {id};".format(name=model.term, definition=model.definition, id=model.id)

        execHelper.execCRUDSql(db, str_update, log_info=handle_log_info)

        return model
 

    @staticmethod
    def delete(db, id):
        """ Delete the keyword by term """

        execHelper = ExecHelper()
        
        str_delete = "DELETE FROM sow_key_word WHERE id = '{id}'".format(id=int(id))
        rval = execHelper.execCRUDSql(db, str_delete, log_info=handle_log_info)
        return rval
