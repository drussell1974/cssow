# -*- coding: utf-8 -*-
from cls_keyword import KeywordModel
from db_helper import to_empty

def get_options(db):
    select_sql = "SELECT name FROM sow_key_word kw WHERE published = 1 ORDER BY name;"

    rows = db.executesql(select_sql)

    data = []

    for row in rows:
        data.append(row[0])

    return data


def get_all(db):
    """
    Get a full list of terms and definitions
    :param db: database context
    :return: list of terms and defintion
    """
    select_sql = "SELECT id as id, name as term, definition as definition FROM sow_key_word kw WHERE published = 1 ORDER BY name;"

    rows = db.executesql(select_sql)

    data = []

    for row in rows:
        data.append(KeywordModel(row[0], row[1], to_empty(row[2])))

    return data


def get_by_terms(db, key_words_list):
    """
    Get a full list of terms and definitions
    :param db:
    :param key_words_list: not seperated keywords
    :return: list of terms and defintion
    """
    ' remove whitespace and use upper'
    key_words_list = key_words_list.replace(' , ', ',').replace(', ', ',').replace(' ,', ',').lower()


    select_sql = "SELECT id as id, name as term, definition as definition FROM sow_key_word kw WHERE LOWER(name) IN ('%s') AND published = 1 ORDER BY name;"
    select_sql = select_sql % "','".join(key_words_list.split(','))

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

    select_sql = "SELECT id as id, name as term, definition as definition FROM sow_key_word kw WHERE id = %s AND published = 1;"
    select_sql = select_sql % id

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

    ' insert the keywords not already in the database '
    for key_word in key_words:
        ' trim white space '
        key_word = key_word.lstrip(' ').rstrip(' ')
        ' check if the keyword exists and insert as necessary  '
        if key_word in existing_keywords or len(key_word) == 0:
            pass
        else:
            _insert(db, key_word, "")


def delete(db, key_word):
    """
    Delete the keyword by term
    :param db: database context
    :param key_word:
    :return:
    """

    str_delete = "DELETE FROM sow_key_word WHERE name = '%s'" % key_word
    db.executesql(str_delete)


def _insert(db, key_word, definition):
    """
    Inserts key word and definition
    :param db: database context
    :param key_word: key term
    :param definition: key definition
    :return:
    """
    db.executesql("INSERT INTO sow_key_word (name, definition) VALUES ('%s', '%s');" % (key_word, definition))


def _update(db, model):
    """
    Inserts key word and definition
    :param db: database context
    :param key_word: key term
    :param definition: key definition
    :return:
    """
    db.executesql("UPDATE sow_key_word SET definition = '{definition}' WHERE id = {id};".format(definition=model.definition, id=model.id))

