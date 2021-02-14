# -*- coding: utf-8 -*-
from django.db import models
from .core.basemodel import BaseModel, try_int
from .core.db_helper import ExecHelper, sql_safe, to_empty, TRANSACTION_STATE
from shared.models.core.log_handlers import handle_log_info, handle_log_error
from .utils.pager import Pager
from .cls_schemeofwork import SchemeOfWorkDataAccess
from .cls_learningobjective import LearningObjectiveModel
from .cls_resource import ResourceDataAccess, ResourceModel
from .cls_keyword import KeywordDataAccess, KeywordModel
from .cls_topic import TopicModel
from .cls_year import YearModel
from .cls_ks123pathway import KS123PathwayModel

class LessonFilter(Pager):

    def __init__(self, keyword_search, pagesize_options, page = 1, pagesize = 20, page_direction = 0):
        # base
        super().__init__(pagesize_options, page, pagesize, page_direction)
        self.keyword_search = keyword_search

    def valiidate(self):
        super().validate()


class LessonModel (BaseModel):
    class Meta:
        permissions = [
            ('view_whiteboard_lessonmodel', 'Can view whiteboard for this Lesson')
        ]
        
    title = ""
    summary = ""
    order_of_delivery_id = 0
    scheme_of_work_id = 0
    content_id = 0
    content_description = ""
    topic_id = None
    year_id = None
    key_stage_id = None
    published = 1
    key_words = []  
    resources = []
    learning_objectives = []
    number_of_resources = 0
    number_of_learning_objectives = 0
    number_of_keywords = 0

    def __init__(self, id_ = 0, title="", orig_id = 0, order_of_delivery_id = 1, scheme_of_work_id = 0, scheme_of_work_name = "", content_id = 0, content_description = "", topic_id = 0, topic_name = "", related_topic_ids = "", parent_topic_id = 0, parent_topic_name = "", key_stage_id = 0, key_stage_name = "", year_id = 0, year_name = "", summary = "", created = "", created_by_id = 0, created_by_name = "", published=1, is_from_db=False):
        #231: implement across all classes
        super().__init__(id_, title, created, created_by_id, created_by_name, published, is_from_db)
        self.title = title
        self.order_of_delivery_id = int(order_of_delivery_id)
        self.scheme_of_work_id = int(scheme_of_work_id)
        self.scheme_of_work_name = scheme_of_work_name
        self.content_id = int(content_id)
        self.content_description = content_description
        self.topic_id = try_int(topic_id, return_value=0)
        self.topic_name = topic_name
        self.parent_topic_id = None if parent_topic_id is None else int(parent_topic_id)
        self.parent_topic_name = parent_topic_name
        self.related_topic_ids = related_topic_ids
        self.key_stage_id = int(key_stage_id)
        self.key_stage_name = key_stage_name
        self.year_id = int(year_id)
        self.year_name = year_name
        self.key_words = []
        self.summary = summary
        self.pathway_objective_ids = []
        self.pathway_ks123_ids = []
        #self.created=created
        #self.created_by_id=try_int(created_by_id)
        #self.created_by_name=created_by_name
        #self.published=published
        self.orig_id = orig_id
        self.url = "/schemeofwork/{}/lessons/{}".format(self.scheme_of_work_id, self.id)

        
    def from_json(self, str_json, encoding="utf8"):
        try:
            import json
            keypairs = json.loads(str_json, encoding=encoding)        

            self.id = int(keypairs["id"])
            self.title = keypairs["title"]
            self.summary = keypairs["summary"]
            self.order_of_delivery_id = int(keypairs["order_of_delivery_id"])
            self.scheme_of_work_id = int(keypairs["scheme_of_work_id"])
            self.content_id = int(keypairs["content_id"])
            self.topic_id = int(keypairs["topic_id"])
            self.key_stage_id = int(keypairs["key_stage_id"])
            self.year_id = int(keypairs["year_id"])
            self.published=keypairs["published"]

            self.validate()

            if self.is_valid == False:
                return None
        except Exception as e:
            self.validation_errors["title"] = "invalid json" 
            raise e

        return self


    def copy(self):
        self.orig_id = self.id


    def is_copy(self):
        if self.orig_id > 0:
            return True
        else:
            return False


    def validate(self, skip_validation = []):
        """ clean up and validate model """
        super().validate(skip_validation)

        # Validate summary
        self._validate_required_string("title", self.title, 1, 45)


        # Validate order_of_delivery_id
        if self.order_of_delivery_id is None or self.order_of_delivery_id < 1 or self.order_of_delivery_id > 9999:
            self.validation_errors["order_of_delivery_id"] = "{} is not a valid selection".format(self.order_of_delivery_id)
            self.is_valid = False

        # Validate scheme_of_work_id
        if self.scheme_of_work_id is None or self.scheme_of_work_id < 1 or self.scheme_of_work_id > 9999:
            self.validation_errors["scheme_of_work_id"] = "{} is not a valid selection for lesson".format(self.scheme_of_work_id)
            self.is_valid = False

        # Validate content_id
        if self.content_id is None or self.content_id < 1 or self.content_id > 99999:
            self.validation_errors["content_id"] = "{} is not a valid selection for lesson".format(self.content_id)
            self.is_valid = False

        # Validate topic_id
        if self.topic_id is None or self.topic_id < 1 or self.topic_id > 9999:
            self.validation_errors["topic_id"] = "{} is not a valid selection for lesson".format(self.topic_id)
            self.is_valid = False

        # Validate key_stage_id
        if self.key_stage_id is None or self.key_stage_id < 1 or self.key_stage_id > 9999:
            self.validation_errors["key_stage_id"] = "{} is not a valid selection".format(self.key_stage_id)
            self.is_valid = False

        # Validate year_id
        if self.year_id is None or self.year_id < 1 or self.year_id > 1000:
            self.validation_errors["year_id"] = "{} is not a valid selection".format(self.year_id)
            self.is_valid = False

        # Validate summary
        self._validate_optional_string("summary", self.summary, 80)

        return self.is_valid


    def _clean_up(self):
        """ clean up properties by casting and ensuring safe for inserting etc """

        self.id = int(self.id)
    
        if self.title is not None:
            self.title = sql_safe(self.title)

        if self.scheme_of_work_name is not None:
            self.scheme_of_work_name = sql_safe(self.scheme_of_work_name)

        if self.key_stage_name is not None:
            self.key_stage_name = sql_safe(self.key_stage_name)

        if self.topic_name is not None:
            self.topic_name = sql_safe(self.topic_name)

        if self.parent_topic_name is not None:
            self.parent_topic_name = sql_safe(self.parent_topic_name)

        if self.summary is not None:
            self.summary = sql_safe(self.summary)

        if self.pathway_objective_ids is not None:
            """ remove duplicates """
            staging_list = []
            for ob in self.pathway_objective_ids:
                if ob not in staging_list:
                    staging_list.append(sql_safe(ob))
            self.pathway_objective_ids = staging_list


    @staticmethod
    def get_options(db, scheme_of_work_id, auth_user):
        rows = LessonDataAccess.get_options(db, scheme_of_work_id, auth_user_id=auth_user.auth_user_id)
        data = []
        for row in rows:
            model = LessonModel(id_=row[0], title=row[1], order_of_delivery_id=row[2], topic_id=row[3], topic_name=row[4], year_id=row[5], year_name=row[6], scheme_of_work_id=scheme_of_work_id)
            model.related_topic_ids = LessonModel.get_related_topic_ids(db, model.id, model.topic_id, auth_user)
            data.append(model)
        
        return data


    @staticmethod
    def get_model(db, lesson_id, scheme_of_work_id, auth_user, resource_type_id=0):
        rows = LessonDataAccess.get_model(db, lesson_id, scheme_of_work_id, auth_user_id=auth_user.auth_user_id, resource_type_id=resource_type_id)
        model = None
        for row in rows:
            model = LessonModel(
                id_=row[0],
                title = row[1],
                order_of_delivery_id=row[2],
                scheme_of_work_id=row[3],
                scheme_of_work_name=row[4],
                content_id=row[5],
                content_description=row[6],
                topic_id=row[7],
                topic_name=row[8],
                parent_topic_id=row[9],
                parent_topic_name=row[10],
                key_stage_id=row[11],
                year_id=row[12],
                summary = row[13],
                created=row[14],
                created_by_id=row[15],
                created_by_name=row[16],
                published=row[17])
            model.key_words = LessonModel.get_all_keywords(db, model.id, auth_user)
            model.learning_objectives = LearningObjectiveModel.get_all(db, model.id, scheme_of_work_id, auth_user)
            model.resources = ResourceModel.get_all(db, model.scheme_of_work_id, model.id, auth_user, resource_type_id)
            model.pathway_ks123_ids = LessonModel.get_ks123_pathway_objective_ids(db, model.id, auth_user)
            #248 Mark instance from database
            model.on_fetched_from_db()
        return model


    @staticmethod
    def get_all(db, scheme_of_work_id, auth_user):
        rows = LessonDataAccess.get_all(db, 
            scheme_of_work_id, 
            auth_user_id=auth_user.auth_user_id)

        data = []
        for row in rows:
            model = LessonModel(
                id_=row[0],
                title = row[1],
                order_of_delivery_id=row[2],
                scheme_of_work_id=row[3],
                scheme_of_work_name=row[4],
                content_id=row[5],
                content_description=row[6],
                topic_id=row[7],
                topic_name=row[8],
                parent_topic_id=row[9],
                parent_topic_name=row[10],
                key_stage_id=row[11],
                year_id=row[12],
                year_name=row[13],
                summary=row[14],
                created=row[15],
                created_by_id=row[16],
                created_by_name=row[17],
                published = row[18]
            )
            
            ' get the key words from the learning objectives '
            model.key_words = LessonModel.get_all_keywords(db, model.id, auth_user)
            ' get the number of learning objectives ' 
            model.learning_objectives = LearningObjectiveModel.get_all(db, model.id, scheme_of_work_id, auth_user)
            ' get number of learning objectives for this lesson '
            model.number_of_learning_objectives = LessonModel.get_number_of_learning_objectives(db, model.id, auth_user)
            ' get number of resources for this lesson '
            model.number_of_resources = ResourceModel.get_number_of_resources(db, model.id, auth_user)
            ' get number of keywords for this lesson '
            model.number_of_keywords = len(model.key_words)
            ' get related topics '
            model.related_topic_ids = LessonModel.get_related_topic_ids(db, model.id, model.topic_id, auth_user)
            ' get ks123 pathways '
            model.pathway_ks123_ids = LessonModel.get_ks123_pathway_objective_ids(db, model.id, auth_user)
            
            # TODO: remove __dict__ . The object should be serialised to json further up the stack
            data.append(model.__dict__)
        return data


    @staticmethod
    def get_filtered(db, scheme_of_work_id, search_criteria, auth_user):
        rows = LessonDataAccess.get_filtered(db, 
            scheme_of_work_id, 
            search_criteria.keyword_search,
            search_criteria.page,
            search_criteria.pagesize,
            auth_user_id=auth_user.user_id)

        data = []
        for row in rows:
            model = LessonModel(
                id_=row[0],
                title = row[1],
                order_of_delivery_id=row[2],
                scheme_of_work_id=row[3],
                scheme_of_work_name=row[4],
                content_id=row[5],
                content_description=row[6],
                topic_id=row[7],
                topic_name=row[8],
                parent_topic_id=row[9],
                parent_topic_name=row[10],
                key_stage_id=row[11],
                year_id=row[12],
                year_name=row[13],
                summary=row[14],
                created=row[15],
                created_by_id=row[16],
                created_by_name=row[17],
                published = row[18]
            )
            
            ' get the key words from the learning objectives '
            model.key_words = LessonModel.get_all_keywords(db, model.id, auth_user)
            ' get the number of learning objectives ' 
            model.learning_objectives = LearningObjectiveModel.get_all(db, model.id, scheme_of_work_id, auth_user)
            ' get number of learning objectives for this lesson '
            model.number_of_learning_objectives = LessonModel.get_number_of_learning_objectives(db, model.id, auth_user)
            ' get number of resources for this lesson '
            model.number_of_resources = ResourceModel.get_number_of_resources(db, model.id, auth_user)
            ' get number of keywords for this lesson '
            model.number_of_keywords = len(model.key_words)
            ' get related topics '
            model.related_topic_ids = LessonModel.get_related_topic_ids(db, model.id, model.topic_id, auth_user)
            ' get ks123 pathways '
            model.pathway_ks123_ids = LessonModel.get_ks123_pathway_objective_ids(db, model.id, auth_user)
            
            # TODO: remove __dict__ . The object should be serialised to json further up the stack
            data.append(model.__dict__)
        return data


    @staticmethod
    def get_by_keyword(db, keyword_id, scheme_of_work_id, auth_user, parent_only = True):
        rows = LessonDataAccess.get_by_keyword(db, 
            keyword_id,
            scheme_of_work_id, 
            auth_user_id=auth_user.user_id)

        data = []
        for row in rows:
            model = LessonModel(
                id_=row[0],
                title = row[1],
                order_of_delivery_id=row[2],
                scheme_of_work_id=row[3],
                scheme_of_work_name=row[4],
                content_id=row[5],
                content_description=row[6],
                topic_id=row[7],
                topic_name=row[8],
                parent_topic_id=row[9],
                parent_topic_name=row[10],
                key_stage_id=row[11],
                year_id=row[12],
                year_name=row[13],
                summary=row[14],
                created=row[15],
                created_by_id=row[16],
                created_by_name=row[17],
                published = row[18]
            )
            
            if parent_only == False:
                ' get the key words from the learning objectives '
                model.key_words = LessonModel.get_all_keywords(db, model.id, auth_user)
                ' get the number of learning objectives ' 
                model.learning_objectives = LearningObjectiveModel.get_all(db, model.id, scheme_of_work_id, auth_user)
                ' get number of learning objectives for this lesson '
                model.number_of_learning_objectives = LessonModel.get_number_of_learning_objectives(db, model.id, auth_user)
                ' get number of resources for this lesson '
                model.number_of_resources = ResourceModel.get_number_of_resources(db, model.id, auth_user)
                ' get number of keywords for this lesson '
                model.number_of_keywords = len(model.key_words)
                ' get related topics '
                model.related_topic_ids = LessonModel.get_related_topic_ids(db, model.id, model.topic_id, auth_user)
                ' get ks123 pathways '
                model.pathway_ks123_ids = LessonModel.get_ks123_pathway_objective_ids(db, model.id, auth_user)
            
            data.append(model)
        return data


    @staticmethod
    def get_all_keywords(db, lesson_id, auth_user):
        rows = LessonDataAccess.get_all_keywords(db, lesson_id, auth_user_id=auth_user.user_id)
        data = []
        for row in rows:
            data.append(KeywordModel(row[0], term=row[1], definition=to_empty(row[2]), scheme_of_work_id=row[3], published=row[4], created=row[5]))
        return data


    @staticmethod
    def get_ks123_pathway_objective_ids(db, lesson_id, auth_user):
        rows = LessonDataAccess.get_ks123_pathway_objective_ids(db, lesson_id, auth_user_id=auth_user.user_id)
        data = []
        for row in rows:
            data.append(try_int(row[0]))
        return data


    @staticmethod
    def get_related_topic_ids(db, lesson_id, parent_topic_id, auth_user):
        rows = LessonDataAccess.get_related_topic_ids(db, lesson_id, parent_topic_id, auth_user_id=auth_user.user_id)
        serializable_list = []
        for row in rows:
            serializable_list.append({"id":row[0], "name":row[1], "checked":row[2] is not None, "disabled":int(row[3]) > 0})
        return serializable_list


    @staticmethod
    def get_number_of_learning_objectives(db, lesson_id, auth_user):
        rows = LessonDataAccess.get_number_of_learning_objectives(db, lesson_id, auth_user_id=auth_user.user_id)
        
        return rows[0][0]

    
    @staticmethod
    def get_pathway_objective_ids(db, lesson_id, auth_user):
        rows = LessonDataAccess.get_pathway_objective_ids(db, lesson_id, auth_user_id=auth_user.auth_user_id)
        data = []
        for row in rows:
            data.append(int(row[0]))
        return data


    @staticmethod
    def save(db, model, auth_user, published):
        """ Save Lesson """
        try:     
            if model.is_new() == True:
                model = LessonDataAccess._insert(db, model, published, auth_user_id=auth_user.auth_user_id)
            elif published == 2:
                model = LessonDataAccess._delete(db, auth_user.auth_user_id, model)
            else:
                model = LessonDataAccess._update(db, model, published, auth_user_id=auth_user.auth_user_id)
            return model
        except:
            handle_log_error(db, 0, "error saving lesson")
            raise


    @staticmethod
    def save_keywords(db, model, auth_user):
        
        results = []

        LessonDataAccess._delete_keywords(db, model, results, auth_user.auth_user_id)
        
        return LessonDataAccess._upsert_key_words(db, model, results, auth_user_id=auth_user.auth_user_id)


    @staticmethod
    def publish(db, auth_user, lesson_id, scheme_of_work_id):
        return LessonDataAccess.publish(db, lesson_id, scheme_of_work_id, auth_user_id=auth_user.auth_user_id)
    

    @staticmethod
    def delete_unpublished(db, scheme_of_work_id, auth_user):
        return LessonDataAccess.delete_unpublished(db, scheme_of_work_id, auth_user_id=auth_user.auth_user_id)


    @staticmethod
    def delete(db, auth_user, lesson_id):
        model = LessonModel(lesson_id)
        LessonDataAccess._delete(db, auth_user_id=auth_user.auth_user_id, model=model)
        return model


class LessonDataAccess:

    @staticmethod
    def get_model(db, id_, scheme_of_work_id, auth_user_id, resource_type_id = 0):
        """
        get lesson for scheme of work

        :param db:database context
        :param id_: the lesson identifier
        :param scheme_of_work_id: the scheme of work identifier
        :param auth_user_id: the user executing the command
        :return: the lesson
        """
        
        execHelper = ExecHelper()
        select_sql = "lesson__get"
        params = (id_,scheme_of_work_id,auth_user_id)
        
        rows = []
        rows = execHelper.select(db, select_sql, params, rows, handle_log_info)
        
        return rows


    @staticmethod
    def get_all(db, scheme_of_work_id, auth_user_id):
        """
        get lessons for the scheme of work

        :param db:database context
        :param scheme_of_work_id: the scheme of work identifier
        :return: list of lessons for the scheme of work
        """

        execHelper = ExecHelper()

        select_sql = "lesson__get_all"
        params = (scheme_of_work_id, auth_user_id); 

        rows = []    
        rows = execHelper.select(db, select_sql, params, rows, handle_log_info)
        
        return rows


    @staticmethod
    def get_filtered(db, scheme_of_work_id, keyword_search, page, pagesize, auth_user_id):
        """
        get lessons for the scheme of work

        :param db:database context
        :param scheme_of_work_id: the scheme of work identifier
        :return: list of lessons for the scheme of work
        """
        
        execHelper = ExecHelper()

        select_sql = "lesson__get_filtered"
        params = (scheme_of_work_id, keyword_search, page - 1, pagesize, auth_user_id); 

        rows = []    
        rows = execHelper.select(db, select_sql, params, rows, handle_log_info)
        
        return rows


    @staticmethod
    def get_all_keywords(db, lesson_id, auth_user_id):
        """
        Get a full list of terms and definitions

        :param db: database context
        :lesson_id: the lesson identifier
        :return: list of terms and defintion
        """

        execHelper = ExecHelper()

        select_sql = "lesson__get_all_keywords"
        params = (lesson_id, auth_user_id)

        rows = []
        rows = execHelper.select(db, select_sql, params, rows, handle_log_info)
        
        return rows

    
    @staticmethod
    def get_pathway_objective_ids(db, lesson_id, auth_user_id):
        """
        Get the learning objectives ids for the lesson

        :param db: the database context
        :param lesson_id: the lesson identifier
        :return: serialized learning objective ids
        """

        execHelper = ExecHelper()
        

        str_select = "lesson__get_pathway_objective_ids"
        params = (lesson_id, auth_user_id)

        rows = []
        rows = execHelper.select(db, str_select, params, rows, handle_log_info)

        return rows

    
    @staticmethod
    def get_ks123_pathway_objective_ids(db, lesson_id, auth_user_id):
        """
        Get the ks123 pathways for the lesson

        :param db: the database context
        :param lesson_id:
        :return: serialized ks123 pathway ids
        """

        execHelper = ExecHelper()
        

        str_select = "lesson__get_ks123_pathway_objective_ids"
        params = (lesson_id, auth_user_id)

        rows = []
        rows = execHelper.select(db, str_select, params, rows, handle_log_info)

        return rows

    
    @staticmethod
    def get_number_of_learning_objectives(db, lesson_id, auth_user_id):
        """
        get the number of learning objective for the lessons

        :param db: the database context
        :param lesson_id: the lesson identifier
        :param auth_user_id: the user executing the command
        :return: the number of learning objectives for the lesson
        """

        execHelper = ExecHelper()

        select_sql = "lesson__get_number_of_learning_objectives"
        params = (lesson_id, auth_user_id)
        
        rows = []
        rows = execHelper.select(db, select_sql, params, rows, handle_log_info)

        return rows


    @staticmethod
    def get_related_topic_ids(db, lesson_id, parent_topic_id, auth_user_id):
        """
        gets the related topic ids for the lesson and whether they are selected or should be disabled

        :param db: the database context
        :param lesson_id: the lesson identifier
        :param parent_topic_id: the top level topic identifier
        :param auth_user_id: the user executing the command
        :return: all topics and child topics
        """

        execHelper = ExecHelper()
        
        str_select = "lesson__get_related_topic_ids"
        params = (lesson_id, parent_topic_id, auth_user_id)

        rows = []
        rows = execHelper.select(db, str_select, params, rows, handle_log_info)
        
        return rows


    @staticmethod
    def get_options(db, scheme_of_work_id, auth_user_id):
        """
        get a list lessons

        :param db: the database context
        :param scheme_of_work_id: the scheme of work identifier
        :param auth_user_id: the user executing the command
        :return: light-weight list of lessons for the scheme of work
        """
        execHelper = ExecHelper()
        
        str_select = "lesson__get_options"

        params = (scheme_of_work_id, auth_user_id)
        
        rows = []
        rows = execHelper.select(db, str_select, params, rows, handle_log_info)
        
        return rows


    @staticmethod
    def get_by_keyword(db, keyword_id, scheme_of_work_id, auth_user_id):
        """
        get lessons using this key word

        :param db:database context
        :param keyword_id: the key word identifier
        :param scheme_of_work_id: the scheme of work identifier
        :return: list of lessons for the key word
        """

        execHelper = ExecHelper()

        select_sql = "lesson__get_by_keyword"
        params = (keyword_id, scheme_of_work_id, auth_user_id); 

        rows = []    
        rows = execHelper.select(db, select_sql, params, rows, handle_log_info)
        
        return rows


    @staticmethod
    def _update(db, model, published, auth_user_id):
        """ 
        updates the sow_lesson and related data

        :param db: the database context
        :param model: the lesson model
        :param published: the published status id
        :param auth_user_id: the user executing the command
        :return: the updated model
        """

        execHelper = ExecHelper()
        
        # 1. Update the lesson
        str_update = "lesson__update"
        params = (
            model.id,
            model.title,
            model.summary,
            model.order_of_delivery_id,
            model.scheme_of_work_id,
            model.content_id,
            model.topic_id,
            model.year_id,
            published,
            auth_user_id
        )

        rows = []
        rows = execHelper.update(db, str_update, params, handle_log_info)

        # 2. upsert related topics
        
        LessonDataAccess._upsert_related_topic_ids(db, model, rows, auth_user_id=auth_user_id)

        # 3. insert pathway objectives

        LessonDataAccess._upsert_pathway_objective_ids(db, model, rows, auth_user_id=auth_user_id)

        # 4. insert pathway ks123

        LessonDataAccess._upsert_pathway_ks123_ids(db, model, rows, auth_user_id=auth_user_id)

        return model


    @staticmethod
    def _insert(db, model, published, auth_user_id):
        """ 
        inserts the sow_lesson and related data 

        :param db: the database context
        :param model: the lesson model
        :param published: the published status id
        :param auth_user_id: the user executing the command
        :return: the model with new identifier
        """

        execHelper = ExecHelper()

        # 1. Insert the lesson

        str_insert = "lesson__insert"
        params = (
            model.id,
            model.title,
            model.summary,
            model.order_of_delivery_id,
            model.scheme_of_work_id,
            model.content_id,
            model.topic_id,
            model.year_id,
            published,
            model.created_by_id,
            model.created,
        )
    

        rows = []
        result = execHelper.insert(db, str_insert, params, handle_log_info)
    
        model.id = result[0]

        # 2. insert related topics

        LessonDataAccess._upsert_related_topic_ids(db, model, rows, auth_user_id)

        # 3. insert pathway objectives

        LessonDataAccess._upsert_pathway_objective_ids(db, model, rows, auth_user_id)

        # 4. insert pathway ks123

        LessonDataAccess._upsert_pathway_ks123_ids(db, model, rows, auth_user_id)

        # 6. insert objectives
        if model.is_copy():
            LessonDataAccess._copy_objective_ids(db, model, rows, auth_user_id)

        return model


    @staticmethod
    def _delete(db, auth_user_id, model):
        """ 
        Delete Lesson 

        :param db: the database context
        :param model: the lesson model
        :param auth_user_id: the user executing the command
        :return: the deleted model
        """
        
        execHelper = ExecHelper()
        
        str_delete = "lesson__delete"
        params = (model.id, auth_user_id)
        
        rval = execHelper.delete(db, str_delete, params, handle_log_info)

        return model


    @staticmethod
    def delete_unpublished(db, scheme_of_work_id, auth_user_id):
        """ 
        Delete all unpublished lessons 

        :param db: the database context
        :param scheme_of_work_id: the scheme of work identifier
        :param auth_user_id: the user executing the command
        :return: the rows
        """

        execHelper = ExecHelper()
        
        str_delete = "lesson__delete_unpublished"
        params = (scheme_of_work_id,auth_user_id)
        
        rows = []
        rows = execHelper.delete(db, str_delete, params, handle_log_info)
        
        return rows


    @staticmethod
    def _upsert_related_topic_ids(db, model, results, auth_user_id):
        """ 
        inserts sow_lesson__has__topics if topic_id does not exist in table 

        :param db: the database context
        :param model: the lesson model
        :param results: results to be appended
        :param auth_user_id: the user executing the command
        :return: appended results
        """

        execHelper = ExecHelper()

        str_insert = "lesson__insert_related_topic"

        for topic_id in model.related_topic_ids:
            if topic_id.isdigit():
                params = (model.id, topic_id, auth_user_id)
                results = execHelper.insert(db, str_insert, params, handle_log_info)
        
        return results


    @staticmethod
    def _upsert_pathway_objective_ids(db, model, results, auth_user_id):
        """ 
        inserts sow_lesson__has__pathway if learing_objective_id does not exist in table

        :param db: the database context
        :param model: the lesson model
        :param results: results to be appended
        :param auth_user_id: the user executing the command
        :return: appended results
        """

        execHelper = ExecHelper()
        
        str_insert = "lesson__insert_pathway"

        for learning_objective_id in model.pathway_objective_ids:
            if learning_objective_id.isdigit():
                params = (model.id, learning_objective_id, auth_user_id)
                results = execHelper.insert(db, str_insert, params, handle_log_info)
        
        return results


    @staticmethod
    def _copy_objective_ids(db, model, results, auth_user_id):
        """ 
        inserts copy of sow_learning_objective__has__lesson from existing lesson 

        :param db: the database context
        :param model: the lesson model
        :param results: results to be appended
        :param auth_user_id: the user executing the command
        :return: appended results
        """

        execHelper = ExecHelper()
        

        str_insert = "lesson__copy_learning_objectives"
        params = ( model.id, model.orig_id, auth_user_id)

        execHelper.insert(db, str_insert, params, handle_log_info)
        
        return results


    @staticmethod
    def _upsert_pathway_ks123_ids(db, model, results, auth_user_id):
        """ 
        inserts sow_lesson__has__ks123pathway if ks123_pathway_id does not exist in table
        """

        execHelper = ExecHelper()
        
        str_insert = "lesson__insert_ks123_pathway"

        for pathway_id in model.pathway_ks123_ids:
            if pathway_id.isdigit():
                params = (model.id, pathway_id, auth_user_id)
                results = execHelper.insert(db, str_insert, params, handle_log_info)
        
        return results


    @staticmethod
    def _upsert_key_words(db, model, results, auth_user_id):
        """ 
        inserts sow_lesson__has__keywords if keyword_id does not exist in table
        :param db: the database context
        :param model: the lesson model
        :param results: results to be appended
        :param auth_user_id: the user executing the command
        :return: appended results
        """

        execHelper = ExecHelper()

        for key_word in model.key_words:
            
            str_insert = "lesson__insert_keywords"
        
            params = (key_word.id, model.id, model.scheme_of_work_id, auth_user_id)

            results = execHelper.insert(db, str_insert, params, handle_log_info)
                  
        return results


    @staticmethod
    def _delete_keywords(db, model, results, auth_user_id):
        
        execHelper = ExecHelper()
        execHelper.begin(db, TRANSACTION_STATE.OPEN)

        try:
            str_delete = "lesson__delete_keywords"
            params = (model.id, auth_user_id)

            results = execHelper.delete(db, str_delete, params, handle_log_info)
            
            execHelper.end_transaction()
            execHelper.commit()
            
        except:
            execHelper.rollback()
            raise
        finally:
            execHelper.end()
            
        return results


    @staticmethod
    def publish(db, lesson_id, scheme_of_work_id, auth_user_id):
        """ 
        set the lesson to published state

        :param db: the database context
        :param id_: the lesson identifier
        :param auth_user_id: the user executing the command
        :return: updated rows
        """
        execHelper = ExecHelper()

        str_publish = "lesson__publish"
        params = (lesson_id, 1, auth_user_id)
        
        rval = []
        rval = execHelper.update(db, str_publish, params, rval)

        return rval

