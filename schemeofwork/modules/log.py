# -*- coding: utf-8 -*-
from datetime import datetime
from db_helper import sql_safe

class Log:

    def __init__(self):
        self.is_enabled = False

    def write(self, db, details):
        """ inserts the detail into the sow_logging table """
        if self.is_enabled == True:
            str_insert = "INSERT INTO sow_logging (details, created) VALUES ('%s', '%s');" % (sql_safe(details), datetime.utcnow())
            print(str_insert)
            db.executesql(str_insert)
