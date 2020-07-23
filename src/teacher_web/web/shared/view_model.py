class ViewModel:
    def __init__(self, page_prefix, main_heading, sub_heading, data = None, alert_message = None):
        self.data = data
        self.content = {
            "page_title": "Dave Russell - Teach Computer Science", # TODO: "SoW Planner - {}".format(page_prefix),
            "content": {
                "main_heading": main_heading,
                "sub_heading": sub_heading,
                "data": self.data
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
