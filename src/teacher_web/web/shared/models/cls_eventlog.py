from datetime import datetime, timedelta
from .core.log import handle_log_info

from shared.models.core.db_helper import ExecHelper
from shared.models.core.basemodel import BaseModel, BaseDataAccess


class EventLogFilter:

    is_valid = False
    validation_errors = []
    date_from = None
    date_to = None

    def __init__(self, date_from = None, date_to = None, etype = "NONE", category = "", subcategory = ""):
        self.date_to = date_to if date_to is not None else datetime.now().date()
        self.date_from = date_from if date_from is not None else self.date_to - timedelta(5) 
        self.type = etype
        self.category = category
        self.subcategory = subcategory

        self.validate()


    def validate(self):
        self.validation_errors.clear()

        if self.date_from > self.date_to:
            self.is_valid = False
            self.validation_errors.append({"date_from", "date range invalid"})
            self.validation_errors.append({"date_to", "date range invalid"})
        else:
            self.is_valid = True
        


class EventLogModel(BaseModel):
    def __init__(self, id_, created, etype, message, detail, category, subcategory):
        self.id = id_
        self.created = created
        self.type = etype
        self.message = message
        self.detail=detail
        self.category=category
        self.subcategory=subcategory
    

    @staticmethod
    def get_all(db, search_criteria, auth_user):

        rows = EventLogDataAccess.get_all(db, search_criteria.date_from, search_criteria.date_to, auth_user)
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
    def get_all(db, date_from, date_to, auth_user):
        """ get event logs by criteria """

        execHelper = ExecHelper()
        
        params = (date_from, date_to, auth_user)

        rows = []
        rows = execHelper.select(db, "logging__get_all", params, rows)
        
        return rows


    @staticmethod
    def delete(db, older_than_n_days, auth_user):
        """ get event logs by criteria """

        execHelper = ExecHelper()
        
        params = (older_than_n_days, auth_user)

        rows = []
        rows = execHelper.delete(db, "logging__delete", params, handle_log_info)
        
        return rows
