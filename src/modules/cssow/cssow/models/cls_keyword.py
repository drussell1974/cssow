# -*- coding: utf-8 -*-
from .core.basemodel import BaseModel
from .core.db_helper import sql_safe, execSql

class KeywordModel(BaseModel):
    def __init__(self, id_, term, definition):
        self.id = id_
        self.term = term
        self.definition = definition


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

from .core.db_helper import to_empty, sql_safe

def get_options(db):
    select_sql = "SELECT name FROM sow_key_word kw WHERE published = 1 ORDER BY name;"

    rows = []
    execSql(db, select_sql, rows)

    data = []

    for row in rows:
        data.append(row[0])

    return data


def get_all(db, search_term = ""):
    """
    Get a full list of terms and definitions
    :param db: database context
    :return: list of terms and defintion
    """
    select_sql = "SELECT id as id, name as term, definition as definition FROM sow_key_word kw WHERE published = 1"

    if len(search_term) > 0:
        select_sql = select_sql + " AND name LIKE '%{search_term}%'".format(search_term=sql_safe(search_term))

    select_sql = select_sql + " ORDER BY name;"

    rows = db.executesql(select_sql)

    data = []

    for row in rows:
        data.append(KeywordModel(row[0], row[1], to_empty(row[2])))

    return data


def get_by_terms(db, key_words_list, allow_all):
    """
    Get a full list of terms and definitions
    :param db:
    :param key_words_list: not seperated keywords
    :return: list of terms and defintion
    """
    if len(key_words_list) == 0 and allow_all == False:
        return []


    select_sql = "SELECT id as id, name as term, definition as definition FROM sow_key_word kw"

    ' remove whitespace and use upper'
    key_words_list = key_words_list.replace(' , ', ',').replace(', ', ',').replace(' ,', ',').lower()

    if len(key_words_list) > 0:
        select_sql = select_sql + " WHERE LOWER(name) IN ('{key_words}') AND published = 1".format(key_words="','".join(sql_safe(key_words_list).split(',')))

    select_sql = select_sql + " ORDER BY name;"

    rows = db.executesql(select_sql)

    data = []

    for row in rows:
        data.append(KeywordModel(row[0], row[1], row[2]))

    return data


def get_by_id(db, id):
    """
    Get a full list of terms and definitions
    :param db:
    :param id: keyword id
    :return: term and defintion
    """

    select_sql = "SELECT id as id, name as term, definition as definition FROM sow_key_word kw WHERE id = {id} AND published = 1;"
    select_sql = select_sql.format(id=int(id))

    rows = db.executesql(select_sql)

    data = KeywordModel(0, "", "")

    for row in rows:
        data = KeywordModel(row[0], row[1], row[2])

    return data


def save(db, model):
    """
    Saves keyword
    :param db: database context
    :param model: the KeywordModel
    """
    if model.is_new():
        pass
    else:
        _update(db, model)


def save_keywords_only(db, key_words):
    """
    Saves keywords not already in the database
    :param db: database context
    :param key_words: list of keywords to save
    """
    ' get all the keywords from the database '
    existing_keywords = get_options(db)

    new_id = 0

    ' insert the keywords not already in the database '
    for key_word in key_words:
        ' trim white space '
        key_word = key_word.lstrip(' ').rstrip(' ')
        ' check if the keyword exists and insert as necessary  '
        if key_word in existing_keywords or len(key_word) == 0:
            pass
        else:
            new_id = _insert(db, key_word, "")

    return new_id

def delete(db, id):
    """
    Delete the keyword by term
    :param db: database context
    :param id: identify of the key term
    :return:
    """

    str_delete = "DELETE FROM sow_key_word WHERE id = '{id}'".format(id=int(id))
    db.executesql(str_delete)


def _insert(db, key_word, definition):
    """
    Inserts key word and definition
    :param db: database context
    :param key_word: key term
    :param definition: key definition
    :return:
    """
    db.executesql("INSERT INTO sow_key_word (name, definition) VALUES ('{key_word}', '{definition}');".format(key_word=sql_safe(key_word), definition=sql_safe(definition)))

    rows = db.executesql("SELECT LAST_INSERT_ID();")
    new_id = 0
    for row in rows:
        new_id = int(row[0])
    return new_id


def _update(db, model):
    """
    Inserts key word and definition
    :param db: database context
    :param key_word: key term
    :param definition: key definition
    :return:
    """
    str_update = "UPDATE sow_key_word SET definition = '{definition}' WHERE id = {id};".format(definition=model.definition, id=model.id)

    db.executesql(str_update)
