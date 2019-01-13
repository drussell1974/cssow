# -*- coding: utf-8 -*-

def get_options(db):

    rows = db.executesql("SELECT name FROM sow_key_word WHERE published = 1 ORDER BY name;")

    data = []

    for row in rows:
        data.append(row[0])
    print("get_options: %s" % data)
    return data


def save(db, key_words):
    """
    saves keywords not already in the database
    :param db: database context
    :param key_words: list of keywords to save
    """
    ' get all the keywords from the database '
    existing_keywords = get_options(db)

    ' insert the keywords not already in the database '
    for key_word in key_words:
        ' trim white space and set to lower case '
        key_word = key_word.lstrip(' ').rstrip(' ').lower()
        ' check if the key word exists and insert as necessary  '
        if key_word in existing_keywords or len(key_word) == 0:
            pass
        else:
            _insert(db, key_word)


def _insert(db, key_word):
    db.executesql("INSERT INTO sow_key_word (name) VALUES ('{name}');".format(name=key_word))

