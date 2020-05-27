# -*- coding: utf-8 -*-
from .core.basemodel import BaseModel

class ContentModel(BaseModel):
    def __init__(self, id_, description):
        self.id = id_
        self.description = description


    def _clean_up(self):
        """ clean up properties by removing by casting and ensuring safe for inserting etc """

        # id
        self.id = int(self.id)

        # trim description
        if self.description is not None:
            self.description = sql_safe(self.description)

"""
DAL
"""

from .core.db_helper import last_sql, sql_safe, execSql


def log_info(db, msg, is_enabled = False):
    from .core.log import Log
    logger = Log()
    logger.is_enabled = is_enabled
    logger.write(db, msg)
    
    
def handle_log_info(db, msg):
    log_info(db, msg, is_enabled=False)


def get_options(db, key_stage_id):

    str_select = "SELECT cnt.id as id, cnt.description as description FROM sow_content as cnt WHERE key_stage_id = {};".format(int(key_stage_id))

    data = []

    try:
        rows = []
        execSql(db, str_select, rows, handle_log_info)

        for row in rows:
            model = ContentModel(row[0], row[1])
            data.append(model)
    except Exception as e:
        last_sql = (str_select, "FAILED")
        raise Exception("Error getting content", e)

    last_sql = (str_select, "SUCCESS")

    return data
