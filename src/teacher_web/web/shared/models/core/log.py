# -*- coding: utf-8 -*-
from datetime import datetime
from .db_helper import ExecHelper, sql_safe
import logging # django logging
from django.conf import settings

class Log:

    def __init__(self):
        self.is_enabled = False

    def write(self, db, details):
        """ write to a log """
        self.write_to_sql(db, details)
        self.write_to_django_log(db, details)


    def write_to_sql(self, db, details):
        """ inserts the detail into the sow_logging table """
        execHelper = ExecHelper()
        
        if self.is_enabled == True:
            str_insert = "INSERT INTO sow_logging (details, created) VALUES ('%s', '%s');" % (sql_safe(details), datetime.utcnow())

            execHelper.execCRUDSql(db, str_insert)

    def write_to_django_log(self, db, details):
        """ 
        Write to the django event log.
        View log when running django debug toolbar
        """
        logger = logging.getLogger(__name__)
        logger.info(details)
        

def log_info(db, msg, is_enabled = False):
    logger = Log()
    logger.is_enabled = is_enabled
    logger.write(db, msg)
    
    
def handle_log_info(db, msg):
    log_info(db, msg, is_enabled=False)