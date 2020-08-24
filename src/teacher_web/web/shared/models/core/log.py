# -*- coding: utf-8 -*-
from datetime import datetime
from .db_helper import ExecHelper, sql_safe
import logging # django logging
from django.conf import settings
from .log_type import LOG_TYPE

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
            
            # write to sql custom log table
            
            self._write_to_sql(msg, log_type, details, category, subcategory)
            
            # write to the django log
            
            self._write_to_django_log(msg, details)
            
            # write to console
            if log_type == LOG_TYPE.Error:
                self._write_to_console(msg, details, CONSOLE_STYLE.FAIL)
            if log_type == LOG_TYPE.Warning:
                self._write_to_console(msg, details, CONSOLE_STYLE.WARNING)
            if log_type == LOG_TYPE.Information:
                self._write_to_console(msg, details, CONSOLE_STYLE.BOLD)
            if log_type == LOG_TYPE.Verbose:
                self._write_to_console(msg, details, CONSOLE_STYLE.ENDC)


    def _write_to_sql(self, msg, event_type, details="", category = "", subcategory = ""):
        """ inserts the detail into the sow_logging table """
        if settings.LOG_TO_SQL == True:
            try:
                execHelper = ExecHelper()
                
                str_insert = "logging__insert"

                # NOTE: limit values to prevent stored proecudure failing

                params =  (msg[0:199], details, event_type, category[0:49], subcategory[0:49])
                
                execHelper.insert(self.db, str_insert, params)

            except Exception as e:
                print("***Error writing to sql event log - exception:'{}'......***".format(e))
                print(".... '{}' to sql event log - message:'{}' was not written to event logs".format(event_type, msg))
                pass # we'll swallow this up to prevent issues with normal operations
        

    def _write_to_django_log(self, msg, details=""):
        """ 
        Write to the django event log.
        View log when running django debug toolbar
        """
        if settings.LOG_TO_DJANGO_LOGS == True:
            # TODO: confirmation required whether this will show through debug panel
            logger = logging.getLogger(__name__)
            logger.info(details)


    def _write_to_console(self, msg, details="", style=CONSOLE_STYLE.OKBLUE):
        """ 
        Write to console using print.
        View log when running django debug toolbar
        """
        if settings.LOG_TO_CONSOLE == True:
            print("\n{}message:'{}', details: {}{}".format(style, msg, details, CONSOLE_STYLE.ENDC))


def handle_log_verbose(db, msg, details = "", log_type = LOG_TYPE.Verbose):
    logger = Log(db, settings.LOGGING_LEVEL)
    logger.write(msg, details, log_type)
    
    
def handle_log_info(db, msg, details = "", log_type = LOG_TYPE.Information):
    logger = Log(db, settings.LOGGING_LEVEL)
    logger.write(msg=msg, details=details, log_type=log_type)
    

def handle_log_warning(db, msg, details = "", log_type = LOG_TYPE.Warning):
    logger = Log(db, settings.LOGGING_LEVEL)
    logger.write(msg, details, log_type)

    
def handle_log_error(db, msg, details = "", log_type = LOG_TYPE.Error):
    logger = Log(db, settings.LOGGING_LEVEL)
    logger.write(msg, details, log_type)


def handle_log_exception(db, msg, ex, log_type = LOG_TYPE.Error):
    logger = Log(db, settings.LOGGING_LEVEL)
    logger.write(msg, "{}".format(ex), log_type)