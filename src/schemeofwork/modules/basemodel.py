# -*- coding: utf-8 -*-
from datetime import datetime


class BaseModel:
    id = 0
    created = ""
    created_by = ""
    is_valid = False

    def is_new(this):
        if this.id == 0:
            return True
        else:
            return False


    def get_last_insert_row_id(this, db_):
        # get last inserted row id
        rows = db_.executesql("SELECT LAST_INSERT_ID();")

        rval = None # Should not be zero (handle has necessary)
        for row in rows:
            this.id = int(row[0])

        return this.id


    def date_created_ui(this):
        return datetime.strftime(this.created, "%d %B %Y")
