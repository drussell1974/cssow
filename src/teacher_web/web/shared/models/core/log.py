# -*- coding: utf-8 -*-
from datetime import datetime
from .db_helper import ExecHelper, sql_safe
import logging # django logging
from django.conf import settings

class LOG_TYPE:
    Verbose = 8
    Information = 4
    Warning = 2
    Error = 1
    NONE = 7


class Log:


    def __init__(self, db, log_level_setting = LOG_TYPE.NONE):
        self.db = db
        self.logging_level = log_level_setting


    def write(self, details, log_type):
        """ write to a log """

        if (self.logging_level % log_type) == 0:
            self._write_to_sql(details)
            self._write_to_django_log(details)


    def _write_to_sql(self, details):
        """ inserts the detail into the sow_logging table """


        execHelper = ExecHelper()
        
        str_insert = "INSERT INTO sow_logging (details, created) VALUES ('%s', '%s');" % (sql_safe(details), datetime.utcnow())

        execHelper.execCRUDSql(self.db, str_insert)


    def _write_to_django_log(self, details):
        """ 
        Write to the django event log.
        View log when running django debug toolbar
        """
        logger = logging.getLogger(__name__)
        logger.info(details)
        
    
def handle_log_info(db, msg, log_type = LOG_TYPE.Information):
    logger = Log(db, settings.LOGGING_LEVEL)
    logger.write(msg, log_type)
    

def handle_log_warning(db, msg, log_type = LOG_TYPE.Warning):
    logger = Log(db, settings.LOGGING_LEVEL)
    logger.write(msg, log_type)

    
def handle_log_error(db, msg, log_type = LOG_TYPE.Error):
    logger = Log(db, settings.LOGGING_LEVEL)
    logger.write(msg, log_type)