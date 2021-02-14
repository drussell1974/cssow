from django.conf import settings
from shared.models.core.django_helper import on_not_found
import traceback

class BaseViewModel:
    model = None
    error_message = ""
    alert_message = ""
    saved = False
    stack_trace = ""

    def on_exception(self, ex):
        self.error_message = ex
        if int(settings.SHOW_STACK_TRACE) > 0:
            self.stack_trace = traceback.format_exc()
        

    def on_post_complete(self, saved = False):
        self.saved = saved  


    def on_not_found(self, model, *identifers):
        on_not_found(model, identifers)
