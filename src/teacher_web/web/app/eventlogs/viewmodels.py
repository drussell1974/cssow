"""
View Models
"""
import io
from shared.models.core.basemodel import try_int
from shared.viewmodels.baseviewmodel import BaseViewModel
from shared.view_model import ViewModel
from shared.models.cls_eventlog import EventLogModel, EventLogFilter


class EventLogIndexViewModel(BaseViewModel):
    
    def __init__(self, db, request, auth_user):

        self.model = []
    
        search_criteria = EventLogFilter()
        
        if request.method == "POST":
            search_criteria.date_from = request.POST["date_from"]
            search_criteria.date_to = request.POST["date_to"]
            search_criteria.type = request.POST["type"]
            search_criteria.category = request.POST["category"]
            search_criteria.subcategory = request.POST["subcategory"]

        self.db = db
        self.auth_user = auth_user
        self.search_criteria = search_criteria

        self.search_criteria.validate()

        if search_criteria.is_valid == True:
            self.model = EventLogModel.get_all(self.db, self.search_criteria, self.auth_user)


    def view(self):
        
        data = { 
            "search_criteria": self.search_criteria,
            "event_logs": self.model
        } 
        
        return ViewModel("", "Event Log", "view event logs", data=data)