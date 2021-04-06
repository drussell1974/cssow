from datetime import datetime, timedelta
from django.conf import settings
from shared.models.core.log_handlers import handle_log_info
from shared.models.core.basemodel import BaseModel
from shared.models.core.db_helper import BaseDataAccess
from shared.models.utils.pager import Pager
from shared.models.core.log_type import LOG_TYPE
from shared.models.core.db_helper import ExecHelper


class EventLogFilter(Pager):

    date_from = None
    date_to = None

    def __init__(self, pagesize_options, page = 1, pagesize = 20, page_direction = 0, date_from = None, date_to = None, event_type = 1, message="", details="", category = "", subcategory = ""):
        # base
        super().__init__(pagesize_options, page, pagesize, page_direction)

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
        super().validate()

        if self.date_from > self.date_to:
            self.is_valid = False
            self.validation_errors["date_from"] = "date range invalid"
        else:
            self.is_valid = True
        

class EventLogModel(BaseModel):

    def __init__(self, id_, created, event_type, message, details="", category="", subcategory="", action="", notify_message=""):
        self.id = id_
        self.created = created
        self.event_type = event_type
        self.message = message
        self.details=details
        self.category=category
        self.subcategory=subcategory
        self.action = action
        self.notify_message = notify_message


    @staticmethod
    def get_all(db, scheme_of_work_id, search_criteria, auth_user):

        rows = EventLogDataAccess.get_all(
            db=db, 
            scheme_of_work_id=scheme_of_work_id, 
            page=search_criteria.page, 
            pagesize=search_criteria.pagesize, 
            date_from=search_criteria.date_from, 
            date_to=search_criteria.date_to, 
            event_type=search_criteria.event_type, 
            category=search_criteria.category, 
            subcategory=search_criteria.subcategory, 
            auth_user_id=auth_user.auth_user_id)
        
        data = []
        for row in rows:
            event = EventLogModel(row[0], row[1], LOG_TYPE.parse(row[2]), row[3], row[4], row[5], row[6])
            
            data.append(event)

        return data


    @staticmethod
    def delete(db, scheme_of_work_id, older_than_n_days, auth_user):
        res = EventLogDataAccess.delete(db, scheme_of_work_id, older_than_n_days, auth_user_id=auth_user.auth_user_id)
        return res


class EventLogDataAccess(BaseDataAccess):

    @staticmethod
    def get_all(db, scheme_of_work_id, page, pagesize, date_from, date_to, event_type, category, subcategory, auth_user_id):
        """ get event logs by criteria """

        execHelper = ExecHelper()
        stored_procedure = "logging__get_all"
        params = (scheme_of_work_id, page - 1, pagesize, date_from, date_to, event_type, category, subcategory, auth_user_id)
        
        rows = []
        rows = execHelper.select(db, stored_procedure, params, rows, handle_log_info)
    
        return rows


    @staticmethod
    def delete(db, scheme_of_work_id, older_than_n_days, auth_user_id):
        """ get event logs by criteria """

        execHelper = ExecHelper()
        
        params = (scheme_of_work_id, older_than_n_days, auth_user_id)
        
        rows = []
        rows = execHelper.delete(db, "logging__delete", params, handle_log_info)
        
        return rows
