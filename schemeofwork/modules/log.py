# -*- coding: utf-8 -*-
from datetime import datetime
from db_helper import add_escape_chars

class Log:

    def __init__(self):
        self.is_enabled = False

    def write(self, db, details):
        """ inserts the detail into the sow_logging table """
        if self.is_enabled == True:
            print(details)
            str_insert = "INSERT INTO sow_logging (details, created) VALUES ('%s', '%s');" % (add_escape_chars(details), datetime.utcnow())
            print(str_insert)
            db.executesql(str_insert)
