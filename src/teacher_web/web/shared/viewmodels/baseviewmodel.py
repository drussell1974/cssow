from django.conf import settings
from shared.models.core.django_helper import on_not_found
import traceback

class BaseViewModel:
    model = None
    error_message = ""
    error_messages = []
    alert_message = ""
    alert_messages = []
    info_messages = []
    saved = False
    stack_trace = ""

    def __init__(self, ctx):
        
        # clear messages
        self.alert_messages = []
        self.error_messages = []
        self.info_messages = []

        self.return_url = "" # 

        if ctx is not None:
            self.department_id = ctx.department_id
            self.institute_id = ctx.institute_id #329 use auth_user context
        else:
            self.department_id = 0
            self.institute_id = 0 

    def on_exception(self, ex):
        self.error_message = ex
        if int(settings.SHOW_STACK_TRACE) > 0:
            self.stack_trace = traceback.format_exc()
        

    def on_post_complete(self, saved = False):
        self.saved = saved  


    def on_not_found(self, model, *identifers):
        on_not_found(model, identifers)
