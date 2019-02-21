# -*- coding: utf-8 -*-
from datetime import datetime

def is_enabled():
    return False

def write(db, details):
    """ inserts the detail into the sow_logging table """
    if is_enabled() == True:
        str_insert = "INSERT INTO sow_logging (details, created) VALUES ('{details}', '{created}');"
        str_insert = str_insert.format(
            details = details,
            created=datetime.utcnow())

        db.executesql(str_insert)
