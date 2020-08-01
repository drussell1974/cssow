# -*- coding: utf-8 -*-
from django.db import models
from .core.db_helper import ExecHelper, sql_safe
from .core.log import handle_log_info
from shared.models.core.basemodel import BaseModel


class TopicModel(models.Model):

    name = ""
    
    def __init__(self, id_, name, created = "", created_by = ""):
        self.id = id_
        self.name = name
        self.created = created
        self.created_by = created_by


    def _clean_up(self):
        """ clean up properties by removing by casting and ensuring safe for inserting etc """

        # id
        self.id = int(self.id)

        # name
        if self.name is not None:
            self.name = sql_safe(self.name)

"""
DAL
"""
"""
def log_info(db, msg, is_enabled = False):
    from .core.log import Log
    logger = Log()
    logger.is_enabled = is_enabled
    logger.write(db, msg)
    
    
def handle_log_info(db, msg):
    log_info(db, msg, is_enabled=False)
"""

def get_options(db, lvl, topic_id = 0):

    #TODO: #230 Move to DataAccess
    BaseModel.depreciation_notice("use TopicDataAccess.get_options()")

    execHelper = ExecHelper()

    str_select = "SELECT id, name, created, created_by FROM sow_topic WHERE lvl = {lvl} and parent_id = {topic_id};"
    str_select = str_select.format(lvl=int(lvl), topic_id=int(topic_id))

    data = []

    try:

        rows = []
        rows = execHelper.execSql(db, str_select, rows, handle_log_info)

        for row in rows:
            model = TopicModel(row[0], row[1], row[2], row[3])
    
            # TODO: remove __dict__ . The object should be serialised to json further up the stack
            data.append(model.__dict__)

    except Exception as e:
        raise Exception("Error getting topics", e)

        
    return data
