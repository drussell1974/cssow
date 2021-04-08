# -*- coding: utf-8 -*-
from datetime import datetime
from shared.models.core.db_helper import ExecHelper, sql_safe
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


    def __init__(self, db, log_level_setting = LOG_TYPE.NONE, notify = None):
        self.db = db
        self.logging_level = log_level_setting
        self.notify = notify
        self.sql_event_log_id = 0


    def write(self, scheme_of_work_id, msg, details, log_type, category = "", subcategory = ""):
        """ write to a log """
        
        if (self.logging_level % log_type) == 0 or self.notify is not None:
            
            # write to sql custom log table
            
            result = LogDataAccess._write_to_sql(self.db, msg=msg, event_type=log_type, scheme_of_work_id=scheme_of_work_id, details=details, category=category, subcategory=subcategory, notify=self.notify)
            
            if result is not None and len(result):
                self.sql_event_log_id = result[0]

            # write to the django log
            if (self.logging_level % log_type) > 0:
                LogDataAccess._write_to_django_log(msg, details)
                
                # write to console
                if log_type == LOG_TYPE.Error:
                    LogDataAccess._write_to_console(msg, details, CONSOLE_STYLE.FAIL)
                if log_type == LOG_TYPE.Warning:
                    LogDataAccess._write_to_console(msg, details, CONSOLE_STYLE.WARNING)
                if log_type == LOG_TYPE.Information:
                    LogDataAccess._write_to_console(msg, details, CONSOLE_STYLE.BOLD)
                if log_type == LOG_TYPE.Verbose:
                    LogDataAccess._write_to_console(msg, details, CONSOLE_STYLE.ENDC)


class LogDataAccess:

    @classmethod
    def _write_to_sql(cls, db, msg, scheme_of_work_id, event_type, details="", category = "", subcategory = "", notify=None):
        """ inserts the detail into the sow_logging table """
        if settings.LOG_TO_SQL == True or notify is not None:
            try:
                execHelper = ExecHelper()
                
                str_insert = "logging__insert"

                # NOTE: limit values to prevent stored proecudure failing
                
                params =  (scheme_of_work_id, msg[0:199], details, int(event_type), category[0:69], subcategory[0:69])
                
                result = execHelper.insert(db, str_insert, params)
                return result
                
            except Exception as e:
                print("***Error writing to sql event log - exception:'{}'......***".format(e))
                print(".... '{}' to sql event log - message:'{}' was not written to event logs".format(event_type, msg))
                pass # we'll swallow this up to prevent issues with normal operations


    @classmethod
    def _write_to_django_log(cls, msg, details=""):
        """ 
        Write to the django event log.
        View log when running django debug toolbar
        """
        if settings.LOG_TO_DJANGO_LOGS == True:
            # TODO: confirmation required whether this will show through debug panel
            logger = logging.getLogger(__name__)
            logger.info(details)

    @classmethod
    def _write_to_console(cls, msg, details="", style=CONSOLE_STYLE.OKBLUE):
        """ 
        Write to console using print.
        View log when running django debug toolbar
        """
        if settings.LOG_TO_CONSOLE == True:
            print("\n{}message:'{}', details: {}{}".format(style, msg, details, CONSOLE_STYLE.ENDC))
