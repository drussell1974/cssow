# -*- coding: utf-8 -*-
from datetime import datetime

class BaseModel:
    id = 0
    created = ""
    created_by = ""
    is_valid = False

    def is_new(self):
        if self.id == 0:
            return True
        else:
            return False


    def date_created_ui(self):
        return datetime.strftime(self.created, "%d %B %Y")
