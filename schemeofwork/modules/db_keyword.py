# -*- coding: utf-8 -*-

def get_options(db, topic_id):
    select_sql = "SELECT name FROM sow_key_word kw WHERE published = 1 AND topic_id = {topic_id} OR {topic_id} = 0 ORDER BY name;"
    select_sql = select_sql.format(topic_id=topic_id)

    rows = db.executesql(select_sql)

    data = []

    for row in rows:
        data.append(row[0])

    return data


def save(db, key_words, topic_id):
    """
    Saves keywords not already in the database
    :param db: database context
    :param key_words: list of keywords to save
    """
    ' get all the keywords from the database '
    existing_keywords = get_options(db, topic_id)

    ' insert the keywords not already in the database '
    for key_word in key_words:
        ' trim white space and set to lower case '
        key_word = key_word.lstrip(' ').rstrip(' ').lower()
        ' check if the key word exists and insert as necessary  '
        if key_word in existing_keywords or len(key_word) == 0:
            pass
        else:
            _insert(db, key_word, topic_id)


def _insert(db, key_word, topic_id):
    db.executesql("INSERT INTO sow_key_word (name, topic_id) VALUES ('{name}', {topic_id});".format(name=key_word, topic_id=topic_id))

