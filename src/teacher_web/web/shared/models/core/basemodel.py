import sys
from datetime import datetime
import json
import re
from django.db import models
import warnings
from shared.models.core.db_helper import ExecHelper, sql_safe
from shared.models.enums.publlished import STATE

class BaseModel(models.Model):
    id = 0
    display_name = ""
    created = ""
    created_by_id = 0
    created_by_name = ""
    is_valid = False
    validation_errors = {}
    error_message = ""
    stack_trace = ""
    published = STATE.DRAFT
    is_from_db = False
    skip_validation = []
    department_id = 0
    institute_id = 0

    # Data type ranges
    MAX_INT = sys.maxsize

    def __init__(self, id_, display_name, created, created_by_id, created_by_name, published, is_from_db, ctx=None):
        self.id = try_int(id_)
        self.display_name = display_name
        self.created = created if len(str(created)) > 0 else str(datetime.now())
        self.created_by_id = try_int(created_by_id)
        self.created_by_name = created_by_name
        self.published = published
        self.set_published_state()
        self.is_from_db = is_from_db
        self.skip_validation = []
        self.auth_user_id = 0
        self.department_id = 0
        self.institute_id = 0
        
        self.ctx = None
        if ctx is not None:
            self.ctx = ctx
            self.department_id = ctx.department_id #329 use auth_user context
            self.institute_id = ctx.institute_id #329 use auth_user context


    def __repr__(self):
        return f"{self.display_name} (id={self.id}, is_from_db={self.is_from_db}"
    

    def set_published_state(self):
        if self.published == STATE.DRAFT:
            self.published_state = "unpublished"
        elif self.published == STATE.PUBLISH or self.published == STATE.PUBLISH_INTERNAL:
            self.published_state = "published"
        elif self.published == STATE.DELETE:
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


    def _validate_duplicate(self, name_of_property, value_to_validate, duplicate_checklist, friendly_message):
        """ check if a value already exists in the duplicate_checklist property """
        if name_of_property not in self.skip_validation:
            if len(list(filter(lambda x: x == value_to_validate, duplicate_checklist))) > 0:
                self.validation_errors[name_of_property] = "{} already exists. {}".format(value_to_validate, friendly_message)
                self.is_valid = False


    def _validate_regular_expression(self, name_of_property, value_to_validate, pattern_to_match, friendly_message):
        if name_of_property not in self.skip_validation:
            if value_to_validate is not None and len(value_to_validate) > 0:
                if re.fullmatch(pattern_to_match, value_to_validate) is None:
                    self.validation_errors[name_of_property] = "{} is not valid. {}".format(value_to_validate, friendly_message)
                    self.is_valid = False


    def _validate_required_string_if(self, name_of_property, value_to_validate, min_value, max_value, func):
        if func(self) == True:
            if value_to_validate is None or len(value_to_validate) < min_value:
                self.validation_errors[name_of_property] = "required"
                self.is_valid = False
        self._validate_optional_string(name_of_property, value_to_validate, max_value)


    def _validate_enum(self, name_of_property, value_to_validate, enum_values):
        if name_of_property not in self.skip_validation:
            if value_to_validate is None or value_to_validate not in list(enum_values):
                self.validation_errors[name_of_property] = "{} is not a valid value".format(value_to_validate)
                self.is_valid = False


    @staticmethod
    def depreciation_notice(msg="Deprecated"):
        raise DeprecationWarning()
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
        if model.published == STATE.DELETE:
            DataAccess._delete(db, model, auth_user)
            model.published = STATE.DELETE
        else:
            if model.is_new() == True:
                rows, new_id = DataAccess._insert(db, model, auth_user)
                model.id = new_id
            else:
                DataAccess._update(db, model, auth_user)
        return model
        

    @staticmethod
    def start_study_in_year_options():
        return  list(map(lambda x:{ "id": x+1, "name": f"Year {x+1}"}, range(13)))


class BaseContextModel(BaseModel):
    
    def __init__(self, id_, display_name, created, created_by_id, created_by_name, published, is_from_db, ctx=None):
        super().__init__(id_=id_, display_name=display_name, created=created, created_by_id=created_by_id, created_by_name=created_by_name, published=published, is_from_db=is_from_db, ctx=ctx)
    
    
    def from_dict(self, dict_obj):
        
        if type(dict_obj) is not dict:
            raise TypeError(f"Value must be type dictionary (dict).{type(dict_obj)}")

        self.id = dict_obj.get("id")
        self.name = dict_obj.get("name")
        self.display_name = dict_obj.get("display_name")
        self.created = dict_obj.get("created")
        self.created_by_id = dict_obj.get("created_by_id")
        self.created_by_name = dict_obj.get("created_by_name")
        self.published = dict_obj.get("published")
        self.set_published_state() # = dict_obj.get("published_state")
        self.auth_user_id = dict_obj.get("auth_user_id")
        self.department_id = dict_obj.get("department_id", 0)
        self.institute_id = dict_obj.get("institute_id", 0)
        self.is_from_db = dict_obj.get("is_from_db")

    # TODO: move to DataModel
    @staticmethod
    def get_context_model(db, default_or_empty_context_model, get_context_model_sp_name, handle_log_info, *lookup_args):
        ''' Call stored procedure get_context_model_sp_name with parameters to include unique identifiers and auth_user_id '''
        execHelper = ExecHelper()

        # return a default or empty        
        model = default_or_empty_context_model
        
        # TODO: could raise outer exception

        result = execHelper.select(db, get_context_model_sp_name, lookup_args, None, handle_log_info)
        if result is not None and len(result) > 1:
            # NOTE: must have 1 or none.....................
            raise Exception(f"{get_context_model_sp_name} must return a single row.")
        else:
            for row in result:
                # NOTE: should return first item only
                model.id = row[0]
                model.name = row[1]
                #model.parent_id = row[2] # TODO: create @property setter
                model.created_by_id = row[3]
                model.published = row[4]
                model.set_published_state()
                model.is_from_db = True
        return model


    # TODO: move to DataModel
    @staticmethod
    def get_context_array(db, default_or_empty_context_model, get_context_model_sp_name, handle_log_info, *lookup_args):
        ''' Call stored procedure get_context_model_sp_name with parameters to include unique identifiers and auth_user_id '''
        execHelper = ExecHelper()

        # return a default or empty        
        array = []
        # TODO: could raise outer exception

        result = execHelper.select(db, get_context_model_sp_name, lookup_args, None, handle_log_info)
        model = default_or_empty_context_model
        for row in result:
            # NOTE: should return first item only
            model.id = row[0]
            model.name = row[1]
            #model.parent_id = row[2] # TODO: create @property setter
            model.created_by_id = row[3]
            model.published = row[4]
            model.set_published_state()
            model.is_from_db = True
            array.append(model.__dict__)
        
        return array


def try_int(val, return_value=None):
    """ convert value to int or None """
    try:
        val = int(val)
    except:
        val = return_value
    return val
