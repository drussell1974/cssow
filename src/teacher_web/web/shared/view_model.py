from datetime import datetime
from django.conf import settings

class ViewModel:
    active_model__id = 0
    active_model__display_name = ""
    active_model__validation_errors = {}
    active_model__published_state = "unknown-state"

    def __init__(self, page_prefix, main_heading, sub_heading, ctx, data = None, active_model = None, error_message = "", stack_trace = "", alert_message = "", delete_dialog_message = "", cancel_dialog_message = "", wizard = None):
        """ Create View Model """
        self.data = data
        self.ctx = ctx

        ui_messages = { 
            "alert_message": alert_message if len(alert_message) > 0 else None,
            "error_message": error_message if len(str(error_message)) > 0 else None,
            "delete_dialog_message": delete_dialog_message if len(delete_dialog_message) > 0 else None,
            "cancel_dialog_message": cancel_dialog_message if len(cancel_dialog_message) > 0 else None
        }

        if active_model is not None:
            self.active_model__id = active_model.id
            self.active_model__display_name = active_model.display_name
            self.active_model__validation_errors = active_model.validation_errors
            self.active_model__published_state = active_model.published_state
        
        self.content = {
            "page_title": "Dave Russell - Teach Computer Science", # TODO: "SoW Planner - {}".format(page_prefix),
            "content": {
                "main_heading": main_heading,
                "sub_heading": sub_heading,
                "data": self.data,
                "validation_errors": self.active_model__validation_errors,
                "active_model": {
                    "id": self.active_model__id,
                    "display_name": self.active_model__display_name,
                    "published_state": self.active_model__published_state
                },
                "ctx": ctx,
                "alert_message": ui_messages,
                "stack_trace": stack_trace,
                "wizard": wizard,        
                "display_date": datetime.now(),
            },
            "auth": {
                "user":False,
                "settings": {
                    "actions_disabled": settings.ACTIONS_DISABLED
                }
            }
        }
        