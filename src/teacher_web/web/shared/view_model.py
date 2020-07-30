class ViewModel:
    active_model__id = 0
    active_model__display_name = ""

    def __init__(self, page_prefix, main_heading, sub_heading, data = None, active_model = None, alert_message = None):
        """ Create View Model """
        self.data = data
        
        if active_model is not None:
            self.active_model__id = active_model.id
            self.active_model__display_name = active_model.display_name

        self.content = {
            "page_title": "Dave Russell - Teach Computer Science", # TODO: "SoW Planner - {}".format(page_prefix),
            "content": {
                "main_heading": main_heading,
                "sub_heading": sub_heading,
                "data": self.data,
                "active_model": {
                    "id": self.active_model__id,
                    "display_name": self.active_model__display_name
                },
            },
            "auth": {
                "user":False,
                "settings": {
                    "actions_disabled":["register", "retrieve_password"],
                }
            },
            "session": {
                "alert_message": alert_message
            }
        }
