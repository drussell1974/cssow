# -*- coding: utf-8 -*-
from django.db import models
from .core.basemodel import BaseModel, try_int
from .core.db_helper import ExecHelper, BaseDataAccess, sql_safe, to_empty
from shared.models.core.log_handlers import handle_log_info
from shared.models.cls_keyword import KeywordModel
from shared.models.enums.permissions import SCHEMEOFWORK, LESSON, DEPARTMENT
from shared.models.enums.publlished import STATE

class SchemeOfWorkModel(BaseModel):

    name = ""
    description = ""
    number_of_lessons = 0
    number_of_learning_objectives = 0
    number_of_resources = 0
    number_of_keywords = 0
    key_words = []
    department_id = 0
    institute_id = 0
    

    @staticmethod
    def empty(ctx):
        return SchemeOfWorkModel(0, auth_user=ctx) # Default


    def __init__(self, id_, name="", description="", exam_board_id=0, exam_board_name="", key_stage_id=0, key_stage_name="", department_name="", school_name = "", created="", created_by_id=0, created_by_name="", is_recent = False, published = STATE.PUBLISH, is_from_db=False, auth_user=None):
        #231: implement across all classes
        
        #assert auth_user is not None

        super().__init__(id_, name, created, created_by_id, created_by_name, published, is_from_db, ctx=auth_user)

        self.name = name
        self.description = description
        self.exam_board_id = try_int(exam_board_id)
        self.exam_board_name = exam_board_name
        self.key_stage_id = try_int(key_stage_id)
        self.key_stage_name = key_stage_name
        self.department_name = department_name
        self.school_name = school_name
        self.is_recent = is_recent
        self.url = '/schemeofwork/{}/lessons'.format(self.id)
        self.number_of_keywords = 0
        self.teacher_permissions = []
        

    @property
    def key_words_str(self):
        key_word_map = map(lambda m: m.term, self.key_words)
        # assign as comma seperated list
        return ",".join(list(key_word_map))


    def validate(self, skip_validation = []):
        """ clean up and validate model """
        super().validate(skip_validation)

        # Validate name
        self._validate_required_string("name", self.name, 1, 40)
        # Validate description
        self._validate_required_string("description", self.description, 1, 1500)
        # Validate exam board
        self._validate_optional_integer("exam_board_id", self.exam_board_id, 1, 9999)
        # Validate key stage
        self._validate_required_integer("key_stage_id", self.key_stage_id, 1, 9999)
        # Validate department
        self._validate_required_integer("department_id", self.department_id, 1, BaseModel.MAX_INT)
        # Validate institute_id
        self._validate_required_integer("institute_id", self.institute_id, 1, BaseModel.MAX_INT)

        self.on_after_validate()

    def _clean_up(self):
        """ clean up properties by casting and ensuring safe for inserting etc """

        self.id = int(self.id)

        if self.name is not None:
            self.name = sql_safe(self.name)

        if self.description is not None:
            self.description = sql_safe(self.description)

        if self.key_stage_name is not None:
            self.key_stage_name = sql_safe(self.key_stage_name)

        if self.exam_board_name is not None:
            self.exam_board_name = sql_safe(self.exam_board_name)

        if self.department_name is not None:
            self.department_name = sql_safe(self.department_name)

        if self.school_name is not None:
            self.school_name = sql_safe(self.school_name)


    @staticmethod
    def get_all(db, auth_user, key_stage_id=0):
        
        rows = SchemeOfWorkDataAccess.get_all(db, department_id=auth_user.department_id, institute_id=auth_user.institute_id, auth_user_id=auth_user.auth_user_id, key_stage_id=key_stage_id)
        data = []
        for row in rows:
            model = SchemeOfWorkModel(id_=row[0],
                                    name=row[1],
                                    description=row[2],
                                    exam_board_id=row[3],
                                    exam_board_name=row[4],
                                    key_stage_id=row[5],
                                    key_stage_name=row[6],
                                    #department_id=row[7], # TODO: get from ctx/auth_user
                                    department_name=row[8],
                                    created=row[9],                                                                                                                                                                                                                         
                                    created_by_id=row[10],
                                    created_by_name=row[11],
                                    published=row[12],
                                    auth_user=auth_user)

            #model.institute_id = row[13]
            
            # TODO: #323 improve performance for the following calls
            
            model.number_of_lessons = SchemeOfWorkModel.get_number_of_lessons(db, model.id, auth_user)
            model.number_of_learning_objectives = SchemeOfWorkModel.get_number_of_learning_objectives(db, model.id, auth_user)
            model.number_of_resources = SchemeOfWorkModel.get_number_of_resources(db, model.id, auth_user)
            model.key_words = SchemeOfWorkModel.get_all_keywords(db, model.id, auth_user)
            model.number_of_keywords = len(model.key_words)

            # TODO: remove __dict__ . The object should be serialised to json further up the stack
            data.append(model.__dict__)
        return data


    @staticmethod
    def get_model(db, id, auth_user):   
        rows = SchemeOfWorkDataAccess.get_model(db, id, department_id=auth_user.department_id, institute_id=auth_user.institute_id, auth_user_id=auth_user.auth_user_id)
        
        # start as none None
        model = SchemeOfWorkModel(0, auth_user=auth_user)
        
        for row in rows:
            model = SchemeOfWorkModel(id_=row[0],
                                    name=row[1],
                                    description=row[2],
                                    exam_board_id=row[3],
                                    exam_board_name=row[4],
                                    key_stage_id=row[5],
                                    key_stage_name=row[6],
                                    #department_id=row[7],
                                    department_name=row[8], # TODO: get from ctx/auth_user
                                    created=row[9],
                                    created_by_id=row[10],
                                    created_by_name=row[11],
                                    published=row[12],
                                    auth_user=auth_user)

            #model.institute_id = row[13] # TODO: #329 use auth_user context
            
            # TODO: #323 improve performance for the following calls

            model.number_of_lessons = SchemeOfWorkModel.get_number_of_lessons(db, model.id, auth_user)
            model.number_of_learning_objectives = SchemeOfWorkModel.get_number_of_learning_objectives(db, model.id, auth_user)
            model.number_of_resources = SchemeOfWorkModel.get_number_of_resources(db, model.id, auth_user)
            model.key_words = SchemeOfWorkModel.get_all_keywords(db, model.id, auth_user)
            model.number_of_keywords = len(model.key_words)
            model.on_fetched_from_db()         
        return model


    @staticmethod
    def get_options(db, auth_user):
        rows = SchemeOfWorkDataAccess.get_options(db, department_id=auth_user.department_id, institute_id=auth_user.institute_id, auth_user_id=auth_user.auth_user_id)
        data = []

        for row in rows:
            model = SchemeOfWorkModel(id_ = row[0], name = row[1], key_stage_name = row[2], auth_user=auth_user)
            data.append(model)

        return data


    @staticmethod
    def get_latest_schemes_of_work(db, top, auth_user):
        rows = SchemeOfWorkDataAccess.get_latest_schemes_of_work(db, top, department_id=auth_user.department_id, institute_id=auth_user.institute_id, auth_user_id=auth_user.auth_user_id)
        data = []
        for row in rows:
            model = SchemeOfWorkModel(id_=row[0],
                                    name=row[1],
                                    description=row[2],
                                    exam_board_id=row[3],
                                    exam_board_name=row[4],
                                    key_stage_id=row[5],
                                    key_stage_name=row[6],
                                    created=row[7],
                                    created_by_id=row[8],
                                    created_by_name=row[9],
                                    published=row[10],
                                    auth_user=auth_user)

            model.department_id=row[11] 
            model.institute_id=row[12] 

            data.append(model)
        return data


    @staticmethod
    def get_schemeofwork_name_only(db, scheme_of_work_id, auth_user):
        rows = SchemeOfWorkDataAccess.get_schemeofwork_name_only(db, scheme_of_work_id, department_id=auth_user.department_id, institute_id=auth_user.institute_id, auth_user_id=auth_user.auth_user_id)
        scheme_of_work_name = ""
        for row in rows:
            scheme_of_work_name = row[0]

        return scheme_of_work_name


    @staticmethod
    def get_key_stage_id_only(db, scheme_of_work_id, auth_user):
        rows = SchemeOfWorkDataAccess.get_key_stage_id_only(db, scheme_of_work_id, department_id=auth_user.department_id, institute_id=auth_user.institute_id, auth_user_id=auth_user.auth_user_id)
        key_stage_id = 0
        for row in rows:
            key_stage_id = row[0]
        return key_stage_id


    @staticmethod
    def get_number_of_lessons(db, scheme_of_work_id, auth_user):
        number_of_lessons = 0
        rows = SchemeOfWorkDataAccess.get_number_of_lessons(db, scheme_of_work_id, department_id=auth_user.department_id, institute_id=auth_user.institute_id, auth_user_id=auth_user.auth_user_id)
        for row in rows:
            number_of_lessons = row[0]   
        return number_of_lessons


    @staticmethod
    def get_number_of_learning_objectives(db, scheme_of_work_id, auth_user):
        number_of_lessons = 0
        rows = SchemeOfWorkDataAccess.get_number_of_learning_objectives(db, scheme_of_work_id, department_id=auth_user.department_id, institute_id=auth_user.institute_id, auth_user_id=auth_user.auth_user_id)
        for row in rows:
            number_of_lessons = row[0]   
        return number_of_lessons


    @staticmethod
    def get_number_of_resources(db, scheme_of_work_id, auth_user):
        number_of_lessons = 0
        rows = SchemeOfWorkDataAccess.get_number_of_reources(db, scheme_of_work_id, department_id=auth_user.department_id, institute_id=auth_user.institute_id, auth_user_id=auth_user.auth_user_id)
        for row in rows:
            number_of_lessons = row[0]   
        return number_of_lessons


    @staticmethod
    def get_all_keywords(db, scheme_of_work_id, auth_user):
        rows = SchemeOfWorkDataAccess.get_all_keywords(db, scheme_of_work_id, department_id=auth_user.department_id, institute_id=auth_user.institute_id, auth_user_id=auth_user.auth_user_id)
        data = []
        for row in rows:
            model = KeywordModel(row[0], term=row[1], definition=to_empty(row[2]), scheme_of_work_id=row[3], published=row[4])
            model.created = row[5]
            data.append(model)
        return data


    @staticmethod
    def save(db, model, auth_user, published=STATE.PUBLISH):
        
        if try_int(published) == STATE.DELETE:
            rval = SchemeOfWorkDataAccess._delete(db, model, auth_user_id=auth_user.auth_user_id)
            model.published = STATE.DELETE
        else:
            if model.is_new() == True:
                model = SchemeOfWorkDataAccess._insert(db, model, published, auth_user_id=auth_user.auth_user_id)
                SchemeOfWorkDataAccess._insert_as__teacher(db, model, auth_user_id=auth_user.auth_user_id, is_authorised=True)
            else:
                model = SchemeOfWorkDataAccess._update(db, model, published, auth_user_id=auth_user.auth_user_id)

        return model


    @staticmethod
    def delete_unpublished(db, auth_user):
        rows = SchemeOfWorkDataAccess.delete_unpublished(db, auth_user_id=auth_user.auth_user_id)
        return rows


    @staticmethod
    def publish_by_id(db, id, auth_user):
        return SchemeOfWorkDataAccess.publish(db=db, auth_user=auth_user, id_=id)        


class SchemeOfWorkDataAccess:
    
    @staticmethod
    def get_model(db, id_, department_id, institute_id, auth_user_id):
        """
        get scheme of work

        :param db: database context
        :param id_: scheme of work identifier
        :param auth_user_id: the user executing the command
        """

        execHelper = ExecHelper()

        execHelper.begin(db)
        
        select_sql = "scheme_of_work__get"
        params = (id_, department_id, institute_id, auth_user_id)

        rows = []
        rows = execHelper.select(db, select_sql, params, rows, handle_log_info)
        return rows


    @staticmethod
    def get_all(db, department_id, institute_id, auth_user_id, key_stage_id=0, published_status = 1):
        """
        get all scheme of work
        """
    
        execHelper = ExecHelper()
        
        select_sql = "scheme_of_work__get_all" 
        params = (key_stage_id, department_id, institute_id, auth_user_id, published_status)

        rows = []
        rows = execHelper.select(db, select_sql, params, rows, handle_log_info)

        return rows


    @staticmethod
    def get_latest_schemes_of_work(db, top = 5, department_id = 0, institute_id = 0, auth_user_id = 0):
        """
        Gets the latest schemes of work with learning objectives
        :param db: the database context
        :param top: number of records to return
        :return: list of schemes of work models
        """
        execHelper = ExecHelper()
        
        select_sql = "scheme_of_work__get_latest"
        params = (top, department_id, institute_id, auth_user_id)

        rows = []
        rows = execHelper.select(db, select_sql, params, rows, handle_log_info)
 
        return rows
        

    @staticmethod
    def _update(db, model, published, auth_user_id):
        execHelper = ExecHelper()

        # 1. update scheme of work 

        str_update = "scheme_of_work__update"
        params = (
            model.id,
            model.name, 
            model.description,
            model.exam_board_id,
            model.key_stage_id,
            model.department_id,
            published,
            auth_user_id)

        execHelper.update(db, str_update, params, handle_log_info)

        return model


    @staticmethod
    def _insert(db, model, published, auth_user_id):
        execHelper = ExecHelper()

        # 1. insert scheme of work

        str_insert = "scheme_of_work__insert"      
        params = (
            model.id,
            model.name,
            model.description,
            model.exam_board_id,
            model.key_stage_id,
            model.department_id,
            model.created,
            model.created_by_id,
            published,
            auth_user_id)
    
        results = execHelper.insert(db, str_insert, params, handle_log_info)
        
        if len(results) > 0:
            model.id = results[0]

        return model


    @staticmethod
    def _insert_as__teacher(db, model, auth_user_id, is_authorised):
        execHelper = ExecHelper()
        
        str_insert = "scheme_of_work__has__teacher_permission__insert"
        
        params = (model.id, auth_user_id, int(DEPARTMENT.HEAD), int(SCHEMEOFWORK.OWNER), int(LESSON.OWNER), auth_user_id, is_authorised)
        
        execHelper.insert(db, str_insert, params, handle_log_info)
        

    @staticmethod
    def _delete(db, model, auth_user_id):
        execHelper = ExecHelper()
        
        str_delete = "scheme_of_work__delete"
        params = (model.id, auth_user_id)
        
        rval = execHelper.delete(db, str_delete, params, handle_log_info)

        return rval


    @staticmethod
    def get_key_stage_id_only(db, scheme_of_work_id, department_id, institute_id, auth_user_id):

        execHelper = ExecHelper()
        
        #271 Create StoredProcedure
        select_sql = "scheme_of_work__get_key_stage_id_only"
        params = (scheme_of_work_id, department_id, institute_id, auth_user_id)

        rows = []
        rows = execHelper.select(db, select_sql, params, rows, handle_log_info)

        return rows


    @staticmethod
    def delete_unpublished(db, auth_user_id):
        """ Delete all unpublished schemes of work """

        execHelper = ExecHelper()
        
        #271 Create StoredProcedure
        str_delete = "scheme_of_work__delete_unpublished"
        params = (0,auth_user_id)
            
        rval = execHelper.delete(db, str_delete, params, handle_log_info)
        return rval


    @staticmethod
    def publish(db, auth_user, id_):
        
        model = SchemeOfWorkModel(id_, auth_user=auth_user)
        model.publish = True

        execHelper = ExecHelper()
        #271 Create StoredProcedure
        str_update = "scheme_of_work__publish"
        params = (model.id, model.published, auth_user.auth_user_id)

        rval = []
        rval = execHelper.update(db, str_update, params, handle_log_info)

        return rval


    @staticmethod
    def get_options(db, department_id, institute_id, auth_user_id = 0):

        execHelper = ExecHelper()
        
        str_select = "scheme_of_work__get_options"
        params = (department_id, institute_id, auth_user_id,)
        
        rows = []
        rows = execHelper.select(db, str_select, params, rows, handle_log_info)

        return rows


    @staticmethod
    def get_schemeofwork_name_only(db, scheme_of_work_id, department_id, institute_id, auth_user_id):
        
        execHelper = ExecHelper()
        
        select_sql = "scheme_of_work__get_schemeofwork_name_only"
        params = (scheme_of_work_id, department_id, institute_id,  auth_user_id)
        
        rows = []
        rows = execHelper.select(db, select_sql, params, rows, handle_log_info)

        return rows


    @staticmethod
    def get_number_of_lessons(db, scheme_of_work_id, department_id, institute_id, auth_user_id):
        execHelper = ExecHelper()
        execHelper.begin(db)
        
        select_sql = "scheme_of_work__get_number_of_lessons"
        params = (scheme_of_work_id, auth_user_id)

        rows = []
        rows = execHelper.select(db, select_sql, params, rows, handle_log_info)
        
        execHelper.end()

        return rows


    @staticmethod
    def get_number_of_learning_objectives(db, scheme_of_work_id, department_id, institute_id, auth_user_id):
        execHelper = ExecHelper()
        execHelper.begin(db)
        
        select_sql = "scheme_of_work__get_number_of_learning_objectives"
        params = (scheme_of_work_id, auth_user_id)

        rows = []
        rows = execHelper.select(db, select_sql, params, rows, handle_log_info)
        
        return rows


    @staticmethod
    def get_number_of_reources(db, scheme_of_work_id, department_id, institute_id, auth_user_id):
        execHelper = ExecHelper()
        
        select_sql = "scheme_of_work__get_number_of_resources"
        params = (scheme_of_work_id, auth_user_id)

        rows = []
        rows = execHelper.select(db, select_sql, params, rows, handle_log_info)
        return rows


    @staticmethod
    def get_all_keywords(db, scheme_of_work_id, department_id, institute_id, auth_user_id):
        """
        Get a full list of terms and definitions

        :param db: database context
        :scheme_of_work: the scheme of work identifier
        :return: list of terms and defintion
        """

        execHelper = ExecHelper()

        select_sql = "scheme_of_work__get_all_keywords"
        params = (scheme_of_work_id, auth_user_id)
        rows = []
        rows = execHelper.select(db, select_sql, params, rows, handle_log_info)
        
        return rows
