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

class CONSOLE_STYLE:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Log:


    def __init__(self, db, log_level_setting = LOG_TYPE.NONE):
        self.db = db
        self.logging_level = log_level_setting


    def write(self, msg, details, log_type, category = "", subcategory = ""):
        """ write to a log """
        
        if (self.logging_level % log_type) == 0:
            self._write_to_sql(msg, details, category, subcategory)
            self._write_to_django_log(msg, details)
            if log_type == LOG_TYPE.Error:
                self._write_to_console(msg, details, CONSOLE_STYLE.FAIL)
            if log_type == LOG_TYPE.Warning:
                self._write_to_console(msg, details, CONSOLE_STYLE.WARNING)
            if log_type == LOG_TYPE.Information:
                self._write_to_console(msg, details, CONSOLE_STYLE.BOLD)
            if log_type == LOG_TYPE.Verbose:
                self._write_to_console(msg, details, CONSOLE_STYLE.ENDC)


    def _write_to_sql(self, msg, details="", category = "", subcategory = ""):
        """ inserts the detail into the sow_logging table """
    

        execHelper = ExecHelper()
        
        str_insert = "INSERT INTO sow_logging (message, details, category, subcategory, created) VALUES ('%s', '%s', '%s', '%s', '%s');" % (sql_safe(msg), sql_safe(details), sql_safe(category), sql_safe(subcategory), datetime.utcnow())
        return

        execHelper.execCRUDSql(self.db, str_insert)


    def _write_to_django_log(self, msg, details=""):
        """ 
        Write to the django event log.
        View log when running django debug toolbar
        """
        logger = logging.getLogger(__name__)
        logger.info(details)


    def _write_to_console(self, msg, details="", style=CONSOLE_STYLE.OKBLUE):
        """ 
        Write to console using print.
        View log when running django debug toolbar
        """
        print("\n{}message:'{}', details: {}{}".format(style, msg, details, CONSOLE_STYLE.ENDC))


def handle_log_verbose(db, msg, details = "", log_type = LOG_TYPE.Verbose):
    logger = Log(db, settings.LOGGING_LEVEL)
    logger.write(msg, details, log_type)
    
    
def handle_log_info(db, msg, details = "", log_type = LOG_TYPE.Information):
    logger = Log(db, settings.LOGGING_LEVEL)
    logger.write(msg, details, log_type)
    

def handle_log_warning(db, msg, details = "", log_type = LOG_TYPE.Warning):
    logger = Log(db, settings.LOGGING_LEVEL)
    logger.write(msg, details, log_type)

    
def handle_log_error(db, msg, details = "", log_type = LOG_TYPE.Error):
    logger = Log(db, settings.LOGGING_LEVEL)
    logger.write(msg, details, log_type)


def handle_log_exception(db, msg, ex, log_type = LOG_TYPE.Error):
    return
    logger = Log(db, settings.LOGGING_LEVEL)
    logger.write(msg, "{}".format(ex), log_type)