from datetime import datetime, timedelta
from django.conf import settings
from shared.models.core.basemodel import BaseModel
from shared.models.core.db_helper import BaseDataAccess
from shared.models.utils.pager import Pager
from shared.models.core.log_type import LOG_TYPE
from shared.models.core.db_helper import ExecHelper

class NotifyModel(BaseModel):
    
    notify_message = ""
    action = ""
    
    def __init__(self, id_, notify_message, message="", action="", reminder="", event_type=LOG_TYPE.Information, event_log_id=0, auth_user_id=0, created=None):
        self.id = id_
        self.message = message
        self.notify_message = notify_message[0:145] # max 30 characters TODO: add to clean function
        self.action = action
        self.reminder = reminder
        self.event_type = event_type
        self.event_log_id = event_log_id
        self.auth_user_id = auth_user_id
        self.created = created

    
    @classmethod
    def get_notifications(self, db, search_criteria, auth_user):
        # TODO: return as EventLogModel collection
        
        rows = NotifyModelDataAccess.get_notifications(
            db=db, 
            start_date=search_criteria.date_to,
            page=search_criteria.page, 
            pagesize=search_criteria.pagesize, 
            auth_user_id=auth_user.auth_user_id)
        
        data = []
        for row in rows:
            event = NotifyModel(row[0], reminder=row[1], created=row[2], event_type=LOG_TYPE.parse(row[3]), message=row[4], action=row[5], notify_message=row[6])
            
            data.append(event)

        return data


    @classmethod
    def save(cls, db, notify):
        NotifyModelDataAccess.insert_notification(db, notify)


    @classmethod
    def delete(cls, db, event_log_id, auth_ctx):
        result = NotifyModelDataAccess.delete(db, event_log_id=event_log_id, auth_user_id=auth_ctx.auth_user_id)
        return result


    @classmethod
    def create(cls, db, title, message, action_url, auth_ctx, handle_log_info, notify_dt = None):
        notify = NotifyModel(0, 
            auth_user_id=auth_ctx.auth_user_id, 
            notify_message=message,
            #message=notify_message, 
            action=action_url, 
            reminder=notify_dt if notify_dt is not None else datetime.now(),
            event_type=LOG_TYPE.Information)

        handle_log_info(db, 0, msg=title, notify=notify)


class NotifyModelDataAccess:

    @classmethod
    def get_notifications(cls, db, start_date, page, pagesize, auth_user_id):
        """ get notifications from event logs for user """

        execHelper = ExecHelper()
        stored_procedure = "logging__get_notifications"
        params = (start_date, page - 1, pagesize, auth_user_id)
        
        rows = []
        rows = execHelper.select(db, stored_procedure, params, rows)
    
        return rows


    @classmethod
    def insert_notification(cls, db, notify):
        """ inserts the detail into the sow_logging_notification table """

        try:
            execHelper = ExecHelper()
            
            str_insert = "logging_notification__insert"
            
            params =  (notify.notify_message, notify.action, notify.reminder, notify.event_log_id, notify.auth_user_id)
            
            execHelper.insert(db, str_insert, params)

        except Exception as e:
            print("***Error writing to sql event log - exception:'{}'......***".format(e))
            pass # we'll swallow this up to prevent issues with normal operations

    
    @classmethod
    def delete(cls, db, event_log_id, auth_user_id):
        """ delete notifications from sow_logging_notification for user """

        execHelper = ExecHelper()
        stored_procedure = "logging_notification__delete"
        params = (event_log_id, auth_user_id)
        
        result = execHelper.delete(db, stored_procedure, params)
    
        return result