from datetime import datetime, timedelta
from django.conf import settings
from .core.log import handle_log_info
from shared.models.core.db_helper import ExecHelper
from shared.models.core.basemodel import BaseModel, BaseDataAccess


class EventLogFilter:

    is_valid = False
    validation_errors = {}
    date_from = None
    date_to = None

    def __init__(self, date_from = None, date_to = None, event_type = 1, message="", details="", category = "", subcategory = ""):
        
        default_to_datetime = datetime.now()
        default_from_datetime = datetime.now() - timedelta(5)

        self.date_to = date_to if date_to is not None else default_to_datetime.strftime(settings.ISOFORMAT)
        self.date_from = date_from if date_from is not None else default_from_datetime.strftime(settings.ISOFORMAT)
        self.event_type = event_type
        self.message = message
        self.details = details
        self.category = category
        self.subcategory = subcategory

        self.validate()


    def validate(self):
        self.validation_errors.clear()

        if self.date_from > self.date_to:
            self.is_valid = False
            self.validation_errors["date_from"] = "date range invalid"
        else:
            self.is_valid = True
        


class EventLogModel(BaseModel):
    def __init__(self, id_, created, event_type, message, details, category, subcategory):
        self.id = id_
        self.created = created
        self.event_type = event_type
        self.message = message
        self.details=details
        self.category=category
        self.subcategory=subcategory
    

    @staticmethod
    def get_all(db, search_criteria, auth_user):

        rows = EventLogDataAccess.get_all(db, search_criteria.date_from, search_criteria.date_to, search_criteria.event_type, auth_user)
        data = []
        for row in rows:
            event = EventLogModel(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
            data.append(event)

        return data


    @staticmethod
    def delete(db, older_than_n_days, auth_user):
        res = EventLogDataAccess.delete(db, older_than_n_days, auth_user)
        return res


class EventLogDataAccess(BaseDataAccess):

    @staticmethod
    def get_all(db, date_from, date_to, event_type, auth_user):
        """ get event logs by criteria """

        execHelper = ExecHelper()
        stored_procedure = "logging__get_all"
        params = (date_from, date_to, event_type, auth_user)

        rows = []
        rows = execHelper.select(db, stored_procedure, params, rows)
    
        return rows


    @staticmethod
    def delete(db, older_than_n_days, auth_user):
        """ get event logs by criteria """

        execHelper = ExecHelper()
        
        params = (older_than_n_days, auth_user)
        
        rows = []
        rows = execHelper.delete(db, "logging__delete", params, handle_log_info)
        
        return rows
