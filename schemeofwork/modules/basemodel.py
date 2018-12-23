# -*- coding: utf-8 -*-
from datetime import datetime

class BaseModel:
    id = 0
    created = ""
    created_by_id = 0
    created_by_name = ""
    is_valid = False
    validation_errors = {}

    def __init__(self, id_, created, created_by_id, created_by_name):
        self.id = int(id_)
        self.created = created
        self.created_by_id = created_by_id
        self.created_by_name = created_by_name


    def validate(self):
        pass


    def get_ui_title(self):
        pass


    def get_ui_sub_heading(self):
        pass


    def is_new(self):
        if self.id == 0:
            return True
        else:
            return False


    def get_ui_created(self):
        return datetime.strftime(self.created, "%d %B %Y")


    def _on_before_validate(self):
        self.is_valid = True
        self.validation_errors.clear()

