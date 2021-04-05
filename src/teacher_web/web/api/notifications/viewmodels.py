
import io
from rest_framework import serializers, status
from rest_framework.parsers import JSONParser
from shared.models.cls_eventlog import EventLogModel, EventLogFilter
from shared.viewmodels.baseviewmodel import BaseViewModel
from shared.serializers.srl_eventlog import EventLogModelSerializer

class NotificationIndexViewModel(BaseViewModel):
    
    def __init__(self, db, settings, auth_user):

        page = settings.PAGER["default"]["page"]    
        pagesize = settings.PAGER["default"]["pagesize"]
        pagesize_options = settings.PAGER["default"]["pagesize_options"]
        page_direction = 0
        
        search_criteria = EventLogFilter(pagesize_options, page, pagesize, page_direction)
        
        data = EventLogModel.get_notifications(db, search_criteria=search_criteria, auth_user=auth_user)

        self.model = list(map(lambda m: EventLogModelSerializer(m).data, data))
