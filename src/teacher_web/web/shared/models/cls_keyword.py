# -*- coding: utf-8 -*-
from .core.basemodel import BaseModel
from .core.db_helper import ExecHelper, sql_safe, to_empty
from .core.log import handle_log_info


class KeywordModel(BaseModel):
    
    id = 0
    term = ""
    definition = ""

    def __init__(self, id_ = 0, term = "", definition = ""):
        self.id = id_
        self.term = term
        self.definition = definition


    def from_json(self, str_json, encoding="utf8"):

        # deserialise

        import json
        keypairs = json.loads(str_json, encoding=encoding)
    
        self.id = keypairs["id"]
        self.term = keypairs["term"]
        self.definition = keypairs["definition"]  

        # validate

        self.validate()

        if self.is_valid == False:
            return None
        
        return self 


    def validate(self):

        """ clean up and validate model """

        self._on_before_validate()

        # clean properties before validation
        self._clean_up()

        # validate title
        self._validate_required_string("term", self.term, 1, 100)

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

 
"""
DAL
"""

class KeywordDataAccess:


    @staticmethod
    def get_options(db):
        execHelper = ExecHelper()

        select_sql = "SELECT id, name, definition FROM sow_key_word kw WHERE published = 1 ORDER BY name;"

        rows = []
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
        rows = execHelper.execSql(db, select_sql, rows, log_info=handle_log_info)

        data = KeywordModel(0, "", "")

        for row in rows:
            data = KeywordModel(row[0], row[1], row[2])

        return data


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
        rows = execHelper.execSql(db, select_sql, rows, log_info=handle_log_info)

        data = []

        for row in rows:
            data.append(KeywordModel(row[0], row[1], row[2]))

        return data


    @staticmethod
    def save(db, model):
        """
        Saves keyword
        :param db: database context
        :param model: the KeywordModel
        """
        
        if model.is_new():
            model = _insert(db, model)
        else:
            _update(db, model)

        return model



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
    rows = execHelper.execSql(db, select_sql, rows, log_info=handle_log_info)

    data = []

    for row in rows:
        data.append(KeywordModel(row[0], row[1], to_empty(row[2])))

    return data


def save_keywords_only(db, key_words):
    """
    Saves keywords not already in the database
    :param db: database context
    :param key_words: list of keywords to save
    """
    ' get all the keywords from the database '
    existing_keywords = KeywordDataAccess.get_options(db)

    new_id = 0
    ' insert the keywords not already in the database '
    for key_word in key_words:
        ' trim white space '
        key_word = key_word.lstrip(' ').rstrip(' ')
        ' check if the keyword exists and insert as necessary  '
        if key_word in existing_keywords or len(key_word) == 0:
            pass
        else:
            new_id = _insert(db, KeywordModel(0, term=key_word, definition=""))

    return new_id


def delete(db, id):
    """
    Delete the keyword by term
    :param db: database context
    :param id: identify of the key term
    :return:
    """
    execHelper = ExecHelper()
    

    str_delete = "DELETE FROM sow_key_word WHERE id = '{id}'".format(id=int(id))
    return execHelper.execCRUDSql(db, str_delete, log_info=handle_log_info)


def _insert(db, model):
    """
    Inserts key word and definition
    :param db: database context
    :param key_word: key term
    :param definition: key definition
    :return:
    """

    execHelper = ExecHelper()

    rows = []
    
    rows = execHelper.execCRUDSql(db, 
        "INSERT INTO sow_key_word (name, definition) VALUES ('{key_word}', '{definition}');".format(key_word=sql_safe(model.term), definition=sql_safe(model.definition))
        , result=rows
        , log_info=handle_log_info
    )

    rows = []
    rows = execHelper.execSql(db, "SELECT LAST_INSERT_ID();", rows)

    for row in rows:
        model.id = int(row[0])

    return model.id


def _update(db, model):
    """
    Inserts key word and definition
    :param db: database context
    :param key_word: key term
    :param definition: key definition
    :return:
    """
    execHelper = ExecHelper()
    
    str_update = "UPDATE sow_key_word SET definition = '{definition}' WHERE id = {id};".format(definition=model.definition, id=model.id)

    return execHelper.execCRUDSql(db, str_update, log_info=handle_log_info)
