
import io
from rest_framework import serializers, status
from rest_framework.parsers import JSONParser
from shared.models.cls_eventlog import EventLogFilter
from shared.models.cls_notification import NotifyModel
from shared.viewmodels.baseviewmodel import BaseViewModel
from shared.serializers.srl_eventlog import NotifyModelSerializer

class NotificationIndexViewModel(BaseViewModel):
    
    def __init__(self, db, settings, auth_user):

        page = settings.PAGER["notifications"]["page"]    
        pagesize = settings.PAGER["notifications"]["pagesize"]
        pagesize_options = settings.PAGER["notifications"]["pagesize_options"]
        page_direction = 0
        
        search_criteria = EventLogFilter(pagesize_options, page, pagesize, page_direction)
        
        data = NotifyModel.get_notifications(db, search_criteria=search_criteria, auth_user=auth_user)

        self.model = list(map(lambda m: NotifyModelSerializer(m).data, data))
