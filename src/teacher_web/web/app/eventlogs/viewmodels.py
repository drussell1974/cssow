"""
View Models
"""
import io
from shared.models.core.basemodel import try_int
from shared.models.core.log import handle_log_exception
from shared.models.core.log_type import LOG_TYPE
from shared.viewmodels.baseviewmodel import BaseViewModel
from shared.models.enums.permissions import DEPARTMENT 
from shared.viewmodels.decorators.permissions import check_teacher_permission
from shared.view_model import ViewModel
from shared.models.cls_eventlog import EventLogModel, EventLogFilter


class EventLogIndexViewModel(BaseViewModel):
    
    @check_teacher_permission(DEPARTMENT.ADMIN)
    def __init__(self, db, request, scheme_of_work_id, settings, auth_user):

        self.db = db
        self.scheme_of_work_id = scheme_of_work_id
        self.settings = settings
        self.auth_user = auth_user

        self.model = []

        try:
            page = settings.PAGER["default"]["page"]
            pagesize = settings.PAGER["default"]["pagesize"]
            pagesize_options = settings.PAGER["default"]["pagesize_options"]
            page_direction = 0
            
            self.search_criteria = EventLogFilter(pagesize_options, page, pagesize, page_direction)
            
            if request.method == "POST":
                self.search_criteria.date_from = request.POST["date_from"]
                self.search_criteria.date_to = request.POST["date_to"]
                self.search_criteria.type = request.POST["event_type"]
                self.search_criteria.category = request.POST["category"]
                self.search_criteria.subcategory = request.POST["subcategory"]
                self.search_criteria.pager(request.POST["page"], request.POST["page_direction"])
                self.search_criteria.pagesize = try_int(request.POST["pagesize"], return_value=pagesize)

            self.search_criteria.validate()
            
            if self.search_criteria.is_valid == True:
                self.model = EventLogModel.get_all(self.db, self.scheme_of_work_id, self.search_criteria, self.auth_user)

        except Exception as e:
            self.error_message = str(e)
            #raise

    def view(self):
        
        data = { 
            "scheme_of_work_id": self.scheme_of_work_id
            "event_type_options": [
                {"key": "Error", "value": LOG_TYPE.Error },
                {"key": "Warning", "value": LOG_TYPE.Warning },
                {"key": "Information", "value": LOG_TYPE.Information },
                {"key": "Verbose", "value": LOG_TYPE.Verbose },
            ],
            "search_criteria": self.search_criteria,
            "event_logs": self.model,
            "settings": self.settings
        } 
        
        return ViewModel("", "Event Log", "view event logs", data=data, error_message=self.error_message)


class EventLogDeleteOldViewModel(BaseViewModel):
    
    @check_teacher_permission(DEPARTMENT.ADMIN)
    def __init__(self, db, request, scheme_of_work_id, settings, auth_user):
        """ delete event log on POST """
        
        self.model = []
        self._scheme_of_work_id = scheme_of_work_id
        self.settings = settings

        self.search_criteria = EventLogFilter(settings.PAGER["default"]["pagesize_options"])

        if request.method == "POST":
            try:
                older_than_n_days = try_int(request.POST["days"], return_value=0)
                
                if older_than_n_days < settings.MIN_NUMBER_OF_DAYS_TO_KEEP_LOGS:
                    raise Exception("events in the last %s days cannot be deleted" % settings.MIN_NUMBER_OF_DAYS_TO_KEEP_LOGS)

                rows_affected = EventLogModel.delete(db, scheme_of_work_id, older_than_n_days, auth_user)

                self.alert_message = "%s event logs deleted" % rows_affected

            except Exception as e:
                handle_log_exception(db, "Error deleting old event logs", e)
                self.error_message = str(e)


    def view(self):

        data = {
            "scheme_of_work_id": self._scheme_of_work_id
            "event_type_options": [
                {"key": "Error", "value": LOG_TYPE.Error },
                {"key": "Warning", "value": LOG_TYPE.Warning },
                {"key": "Information", "value": LOG_TYPE.Information },
                {"key": "Verbose", "value": LOG_TYPE.Verbose },
            ],
            "search_criteria": self.search_criteria,
            "event_logs": [],
            "settings": self.settings
        } 
        
        return ViewModel("", "Event Log", "view event logs", data=data, error_message=self.error_message, alert_message=self.alert_message)