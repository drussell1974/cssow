# -*- coding: utf-8 -*-
from datetime import datetime
import json
import re
from django.db import models
import warnings

class BaseModel(models.Model):
    id = 0
    display_name = ""
    created = ""
    created_by_id = 0
    created_by_name = ""
    is_valid = False
    # TODO: return dictionary with double quotes for json parsing
    validation_errors = {}
    error_message = ""
    published = 0
    is_from_db = False
    skip_validation = []

    def __init__(self, id_, display_name, created, created_by_id, created_by_name, published, is_from_db):
        self.id = try_int(id_)
        self.display_name = display_name
        self.created = created
        self.created_by_id = try_int(created_by_id)
        self.created_by_name = created_by_name
        self.published = published
        self.set_published_state()
        self.is_from_db = is_from_db
        self.skip_validation = []


    def __repr__(self):
        return "{} (id={})".format(self.display_name, self.id)


    def from_dict(self, dict_obj):
        raise NotImplementedError("from_dict not implemented")        


    def on__from_post(self, dict_obj):
        if type(dict_obj) is not dict:
            raise TypeError("dict_json Type is {}. Value <{}> must be type dictionary (dict).".format(type(dict_obj), dict_obj))


    """
    State members
    """

    def set_published_state(self):
        if self.published == 0:
            self.published_state = "unpublished"
        elif self.published == 1:
            self.published_state = "published"
        elif self.published == 2:
            self.published_state = "deleting"
        else:
            self.published_state = "unknown"    
            

    def is_new(self):
        if self.id == 0:
            return True
        else:
            return False


    def on_fetched_from_db(self):
        """ event to use when instances has been retreived from the data """
        self.is_from_db = True

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

    def validate(self, skip_validation):
        self._on_before_validate(skip_validation)


    def _on_before_validate(self, skip_validation = []):
        # clean properties before validation
        self._clean_up()
        self.is_valid = True
        self.skip_validation = skip_validation
        self.validation_errors.clear()


    def _clean_up(self):
        pass


    def on_after_validate(self):
        self.skip_validation = []
        if any(self.validation_errors.values()):
            self.error_message = next(iter(self.validation_errors.values()))


    def _validate_required_string(self, name_of_property, value_to_validate, min_value, max_value, match_regular_expression=(None,None)):
        if name_of_property not in self.skip_validation:
            if value_to_validate is None or len(value_to_validate) < min_value:
                self.validation_errors[name_of_property] = "required"
                self.is_valid = False
            elif len(value_to_validate) > max_value:
                self.validation_errors[name_of_property] = "is {} characters (cannot exceed {} characters)".format(len(value_to_validate), max_value)
                self.is_valid = False
        

    def _validate_optional_string(self, name_of_property, value_to_validate, max_value, match_regular_expression=(None,None)):
        if name_of_property not in self.skip_validation:
            if value_to_validate is not None:
                if len(value_to_validate) > max_value:
                    self.validation_errors[name_of_property] = "is {} characters (cannot exceed {} characters)".format(len(value_to_validate), max_value)
                    self.is_valid = False


    def _validate_optional_list(self, name_of_property, list_to_validate, sep, max_items):
        if name_of_property not in self.skip_validation:
            if list_to_validate is not None:
                test = list_to_validate
                
                if sep is not None:
                    test = list_to_validate.split(sep)
                
                if len(test) > max_items:
                    self.validation_errors[name_of_property] = "has {} items (number of items cannot exceed {})".format(len(test), max_items)
                    self.is_valid = False


    def _validate_required_integer(self, name_of_property, value_to_validate, min_value, max_value):
        if name_of_property not in self.skip_validation:
            if value_to_validate is None or value_to_validate < min_value or value_to_validate > max_value:
                self.validation_errors[name_of_property] = "{} is not a valid range".format(value_to_validate)
                self.is_valid = False


    def _validate_optional_integer(self, name_of_property, value_to_validate, min_value, max_value):
        if name_of_property not in self.skip_validation:
            if value_to_validate is not None:
                if value_to_validate < min_value or value_to_validate > max_value:
                    self.validation_errors[name_of_property] = "{} is not a valid range".format(value_to_validate)
                    self.is_valid = False


    def _validate_optional_uri(self, name_of_property, value_to_validate):
        if name_of_property not in self.skip_validation:
            # 1. check the string does not exceed the maximum for a url
            self._validate_optional_string(name_of_property, value_to_validate, 2083)
            # 2. check the string is a url
            if value_to_validate is not None:
                if len(value_to_validate) > 0:
                    if re.search("^(http:\/\/www\.|https:\/\/www\.|http:\/\/|https:\/\/)?[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,20}(:[0-9]{1,5})?(\/.*)?$", value_to_validate) == None:
                        self.validation_errors[name_of_property] = "{} is not a valid url".format(value_to_validate)
                        self.is_valid = False


    def _validate_children(self, name_of_property, parent, children_to_validate, skip_validation=[]):
        if name_of_property not in self.skip_validation:
            if parent.is_valid and children_to_validate is not None:
                all_errors = ""
                for value in children_to_validate:
                    value.validate(skip_validation)
                    if value.is_valid == False:
                        all_errors = all_errors + "|{}(id:{}):{}|".format(name_of_property, value.id, value.validation_errors)
                        self.is_valid = False
                # add errors to property only if there are errors
                if len(all_errors) > 0:
                    self.validation_errors[name_of_property] = all_errors


    # TODO: 299 prevent duplicate values
    def _validate_duplicate(self, name_of_property, value_to_validate, duplicate_checklist, friendly_message):
        """ check if a value already exists in the duplicate_checklist property """
        if name_of_property not in self.skip_validation:
            if self.is_new() == True:
                for value in duplicate_checklist:
                    # add errors to property only if there are errors
                    if value == value_to_validate:
                        self.validation_errors[name_of_property] = "{} already exists. {}".format(value_to_validate, friendly_message)
                        self.is_valid = False


    def _validate_regular_expression(self, name_of_property, value_to_validate, pattern_to_match, friendly_message):
        if name_of_property not in self.skip_validation:
            if value_to_validate is not None and len(value_to_validate) > 0:
                if re.fullmatch(pattern_to_match, value_to_validate) is None:
                    self.validation_errors[name_of_property] = "{} is not valid. {}".format(value_to_validate, friendly_message)
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
    def depreciation_notice(msg="Deprecated"):
        warnings.warn(msg, DeprecationWarning)


    @staticmethod
    def upsert(db, model, auth_user, published, DataAccess):
        """ Determine update, insert or delete 

            :param db: the database

            :param model: object instance

            :param auth_user : the authorised user id

            :param published: model state

            :param DataAccess: the data access model with _insert, _update and _delete functions
        
            :return: the instance of the model being inserted/updated/deleted
        """
        model.published = int(published)
        if model.published == 2:
            DataAccess._delete(db, model, auth_user)
            model.published = 2
        else:
            if model.is_new() == True:
                rows, new_id = DataAccess._insert(db, model, auth_user)
                model.id = new_id
            else:
                DataAccess._update(db, model, auth_user)
        return model


"""
formatting members
"""

def try_int(val, return_value=None):
    """ convert value to int or None """
    try:
        val = int(val)
    except:
        val = return_value
    return val



from shared.models.core.db_helper import ExecHelper
from shared.models.core.log import handle_log_info

class BaseDataAccess:

    @staticmethod
    def _insert(db, insert_sql_statement, params, rows = []):
        """ Insert into the database

            :param db: database
            
            :param insert_sql_statement: the INSERT INTO sql statement
            
            :param rows: previous returned rows
            
            :return: updated_rows, last_inserted_id the updated rows and the last inserted id
        """

        execHelper = ExecHelper()

        updated_rows = []
    
        rows, last_inserted_id = execHelper.insert(db, insert_sql_statement, params, handle_log_info)
        
        return updated_rows, last_inserted_id


    @staticmethod
    def _update(db, update_sql_statement, params):

        execHelper = ExecHelper()

        result = execHelper.update(db, update_sql_statement, params, handle_log_info)
        
        return result # updated rows


    @staticmethod
    def _delete(db, delete_sql_statement, params):
        
        execHelper = ExecHelper()

        result = execHelper.delete(db, delete_sql_statement, params, handle_log_info)

        return result # delete rows