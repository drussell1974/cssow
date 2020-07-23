# -*- coding: utf-8 -*-
from datetime import datetime
import json
import re
from django.db import models
import warnings


class BaseModel(models.Model):
    id = 0
    created = ""
    created_by_id = 0
    created_by_name = ""
    is_valid = False
    # TODO: return dictionary with double quotes for json parsing
    validation_errors = {}
  
    def __init__(self, id_, created, created_by_id, created_by_name, published):
        self.id = int(id_)
        self.created = created
        self.created_by_id = created_by_id
        self.created_by_name = created_by_name
        self.published = True if published == 1 else 0


    #def from_dict(self, srl):
    #    self.id = srl["id"]
    #    self.term = srl["term"]
    #    self.definition = srl["definition"]   
        
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


    def get_ui_created(self, dt):
        return datetime.strftime(dt, "%d %B %Y")


    def set_is_recent(self):
        """ checks the created field and sets is_recent """
        if self.created is not None:
            date_format = "%Y-%m-%d %H:%M:%S"
            a = datetime.strptime(str(self.created), date_format)
            b = datetime.now()
            delta = b - a
            self.is_recent = False if delta.days > 3 else True


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
        elif len(value_to_validate) > max_value:
            self.validation_errors[name_of_property] = "is {} characters (cannot exceed {} characters)".format(len(value_to_validate), max_value)
            self.is_valid = False


    def _validate_optional_string(self, name_of_property, value_to_validate, max_value):
        if value_to_validate is not None:
            if len(value_to_validate) > max_value:
                self.validation_errors[name_of_property] = "is {} characters (cannot exceed {} characters)".format(
                    len(value_to_validate), max_value)
                self.is_valid = False


    def _validate_optional_list(self, name_of_property, list_to_validate, sep, max_items):
        if list_to_validate is not None:
            if len(list_to_validate.split(sep)) > max_items:
                self.validation_errors[name_of_property] = "has {} items (number of items cannot exceed {})".format(
                    len(list_to_validate.split(sep)), max_items)
                self.is_valid = False


    def _validate_required_integer(self, name_of_property, value_to_validate, min_value, max_value):
        if value_to_validate is None or value_to_validate < min_value or value_to_validate > max_value:
            self.validation_errors[name_of_property] = "{} is not a valid range".format(value_to_validate)
            self.is_valid = False


    def _validate_optional_integer(self, name_of_property, value_to_validate, min_value, max_value):
        if value_to_validate is not None:
            if value_to_validate < min_value or value_to_validate > max_value:
                self.validation_errors[name_of_property] = "{} is not a valid range".format(value_to_validate)
                self.is_valid = False


    def _validate_optional_uri(self, name_of_property, value_to_validate):
        # 1. check the string does not exceed the maximum for a url
        self._validate_optional_string(name_of_property, value_to_validate, 2083)
        # 2. check the string is a url
        if value_to_validate is not None:
            if len(value_to_validate) > 0:
                if re.search("^(http:\/\/www\.|https:\/\/www\.|http:\/\/|https:\/\/)?[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,20}(:[0-9]{1,5})?(\/.*)?$", value_to_validate) == None:
                    self.validation_errors[name_of_property] = "{} is not a valid url".format(value_to_validate)
                    self.is_valid = False


    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)


    def _validate_required_string_if(self, name_of_property, value_to_validate, min_value, max_value, func):
        if func(self) == True:
            if value_to_validate is None or len(value_to_validate) < min_value:
                self.validation_errors[name_of_property] = "required"
                self.is_valid = False
        self._validate_optional_string(name_of_property, value_to_validate, max_value)


    @staticmethod
    def depreciation_notice():
        warnings.warn("deprecated", DeprecationWarning)


"""
formatting members
"""

def try_int(val):
    """ convert value to int or None """
    try:
        val = int(val)
    except:
        val = None
    return val


