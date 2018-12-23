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

    """
    State members
    """

    def is_new(self):
        if self.id == 0:
            return True
        else:
            return False

    """
    Friendly names
    """

    def get_ui_title(self):
        pass


    def get_ui_sub_heading(self):
        pass


    def get_ui_created(self):
        return datetime.strftime(self.created, "%d %B %Y")

    """
    formatting members
    """

    def _try_int(self, val):
        """ convert value to int or None """
        try:
            val = int(val)
        except:
            val = None
        return val

    """
    Validation members
    """

    def validate(self):
        pass


    def _on_before_validate(self):
        self.is_valid = True
        self.validation_errors.clear()


    def _validate_required_string(self, name_of_property, value_to_validate, min_value, max_value):
        if value_to_validate is None or len(value_to_validate) < min_value:
            self.validation_errors[name_of_property] = "required"
            self.is_valid = False
        elif len(value_to_validate) > 25:
            self.validation_errors[name_of_property] = "is {} characters (cannot exceed {} characters)".format(len(value_to_validate), max_value)
            self.is_valid = False
