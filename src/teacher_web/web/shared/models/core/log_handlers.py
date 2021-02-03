from .log import Log
from django.conf import settings
from .log_type import LOG_TYPE


def handle_log_verbose(db, scheme_of_work_id, msg, details = "", log_type = LOG_TYPE.Verbose):
    logger = Log(db, settings.LOGGING_LEVEL)
    logger.write(scheme_of_work_id, msg, details, log_type)
    
    
def handle_log_info(db, scheme_of_work_id, msg, details = "", log_type = LOG_TYPE.Information):
    logger = Log(db, settings.LOGGING_LEVEL)
    logger.write(scheme_of_work_id, msg, details, log_type)
    

def handle_log_warning(db, scheme_of_work_id, msg, details = "", log_type = LOG_TYPE.Warning):
    logger = Log(db, settings.LOGGING_LEVEL)
    logger.write(scheme_of_work_id, msg, details, log_type)

    
def handle_log_error(db, scheme_of_work_id, msg, details = "", log_type = LOG_TYPE.Error):
    logger = Log(db, settings.LOGGING_LEVEL)
    logger.write(scheme_of_work_id, msg, details, log_type)


def handle_log_exception(db, scheme_of_work_id, msg, ex, log_type = LOG_TYPE.Error):
    logger = Log(db, settings.LOGGING_LEVEL)
    logger.write(scheme_of_work_id, msg, "{}".format(ex), log_type)