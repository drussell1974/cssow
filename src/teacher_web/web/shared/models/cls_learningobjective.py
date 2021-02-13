# -*- coding: utf-8 -*-
from datetime import datetime
from .core.db_helper import to_empty, sql_safe
from .core.basemodel import BaseModel, try_int
from .core.db_helper import ExecHelper, sql_safe
from shared.models.core.log_handlers import handle_log_info


class LearningObjectiveModel (BaseModel):

    def __init__(self, id_, description = "", notes = "", scheme_of_work_name = "", solo_taxonomy_id = 0, solo_taxonomy_name = "", solo_taxonomy_level = "", parent_topic_id = None, parent_topic_name = "", content_id = None, content_description = "", key_stage_id = 0, key_stage_name = "", lesson_id = 0, lesson_name = "", parent_id = None, key_words = "", group_name = "", is_key_objective = True, created = "", created_by_id = 0, created_by_name = "", published=1, is_from_db=False):
        #231: implement across all classes
        super().__init__(id_, description, created, created_by_id, created_by_name, published, is_from_db)
        
        self.id = int(id_)
        self.description = description
        self.notes = notes
        self.scheme_of_work_name = scheme_of_work_name
        self.solo_taxonomy_id = int(solo_taxonomy_id)
        self.solo_taxonomy_name = solo_taxonomy_name
        self.solo_taxonomy_level = solo_taxonomy_level
        self.parent_topic_id =  try_int(parent_topic_id)
        self.parent_topic_name = parent_topic_name
        self.content_id = try_int(content_id)
        self.content_description = content_description
        self.lesson_id = int(lesson_id)
        self.lesson_name = lesson_name
        self.key_stage_id = try_int(key_stage_id)
        self.key_stage_name = key_stage_name
        self.parent_id = try_int(parent_id)
        self.key_words = key_words
        self.group_name = group_name
        self.is_key_objective = True #TODO: calculate based on whether objective is a top level course objective

        self.set_published_state()  
            

    def validate(self, skip_validation = []):
        """ clean up and validate model """
        super().validate(skip_validation)

        # validate description
        self._validate_required_string("description", self.description, 1, 1000)

        # validate group_name
        self._validate_optional_string("group_name", self.group_name, 15)

        # validate notes
        self._validate_optional_string("notes", self.notes, 2500)

        # validate content_id
        self._validate_optional_integer("content_id", self.content_id, 1, 9999)

        # validate solo_taxonomy_id
        self._validate_required_integer("solo_taxonomy_id", self.solo_taxonomy_id, 1, 9999)

        # validate lesson_id
        self._validate_required_integer("lesson_id", self.lesson_id, 1, 9999)

        # validate parent_id
        self._validate_optional_integer("parent_id", self.parent_id, 1, 9999)

        # Validate key_words
        self._validate_optional_list("key_words", self.key_words, sep=",", max_items=15)


    def _clean_up(self):
        """ clean up properties by casting and ensuring safe for inserting etc """

        self.id = int(self.id)

        # trim description
        if self.description is not None:
            self.description = sql_safe(self.description)

        # trim notes
        if self.notes is not None:
            self.notes = sql_safe(self.notes)

        # trim parent_topic_name
        if self.parent_topic_name is not None:
            self.parent_topic_name = sql_safe(self.parent_topic_name)

        # trim content_description
        if self.content_description is not None:
            self.content_description = sql_safe(self.content_description)

        # trim lesson_name
        if self.lesson_name is not None:
            self.lesson_name = sql_safe(self.lesson_name)

        # trim key_stage_name
        if self.key_stage_name is not None:
            self.key_stage_name = sql_safe(self.key_stage_name)

        if self.key_words is not None:
            self.key_words = sql_safe(self.key_words).replace(', ',',')

        # trim group_name
        if self.group_name is not None:
            self.group_name = sql_safe(self.group_name)


    @staticmethod
    #248 Added parameters
    def get_model(db, learning_objective_id, lesson_id, scheme_of_work_id, auth_user):
        rows =  LearningObjectiveDataAccess.get_model(db, learning_objective_id, lesson_id, scheme_of_work_id, auth_user_id=auth_user.id)
        #TODO: return None
        model = LearningObjectiveModel(0)
        
        for row in rows:
            model = LearningObjectiveModel(
                id_ = row[0],
                description = row[1],
                solo_taxonomy_id = row[2],
                solo_taxonomy_name = row[3],
                solo_taxonomy_level = row[4],
                content_id = row[5],
                content_description = row[6],
                lesson_id = row[7],
                key_stage_id = row[8],
                key_stage_name = row[9],
                key_words=row[10],
                notes=row[11],
                group_name=row[12],
                created = row[13],
                created_by_id = row[14],
                created_by_name = row[15],
                published = row[16])
            model.on_fetched_from_db()

        return model


    @staticmethod
    def get_all(db, lesson_id, scheme_of_work_id, auth_user):
        rows = LearningObjectiveDataAccess.get_all(db, lesson_id, scheme_of_work_id, auth_user_id=auth_user.user_id)
        data = []
        for row in rows:
            model = LearningObjectiveModel(
                id_ = row[0],
                description = row[1],
                solo_taxonomy_id = row[2],
                solo_taxonomy_name = row[3],
                solo_taxonomy_level = row[4],
                content_id = row[5],
                content_description = row[6],
                key_stage_id = row[7],
                key_stage_name = row[8],
                lesson_id = row[9],
                lesson_name = row[10],
                key_words=row[11],
                notes=row[12],
                group_name=row[13],
                is_key_objective= row[14],
                created = row[15],
                created_by_id = row[16],
                created_by_name = row[17],
                published=row[18])
            # TODO: remove __dict__ . The object should be serialised to json further up the stack
            data.append(model.__dict__)
        return data


    @staticmethod
    def get_all_pathway_objectives(db, key_stage_id, key_words, auth_user):
        rows = LearningObjectiveDataAccess.get_all_pathway_objectives(db, key_stage_id, key_words, auth_user_id=auth_user.id)
        data = []
        for row in rows:
            if len(row[9]) > 0 and key_words is not None:
                for keyword in key_words.split(","):
                    if len(keyword) > 0 and keyword in row[9]:
                        model = LearningObjectiveModel(
                            id_ = row[0],
                            description = row[1],
                            solo_taxonomy_id = row[2],
                            solo_taxonomy_name = row[3],
                            solo_taxonomy_level = row[4],
                            content_id = row[5],
                            content_description = row[6],
                            key_stage_id = row[7],
                            key_stage_name = row[8],
                            key_words = row[9],
                            group_name = row[10],
                            created = row[11],
                            created_by_id = row[12],
                            created_by_name = row[13]
                            )

                        # TODO: remove __dict__ . The object should be serialised to json further up the stack      
                        data.append(model.__dict__)
                        break # only add objective once
        return data


    @staticmethod
    def get_linked_pathway_objectives(db, lesson_id, auth_user):
        # TODO: verify use
        return LearningObjectiveDataAccess.get_linked_pathway_objectives(db, lesson_id, auth_user_id=auth_user.id)


    @staticmethod
    def save(db, model, auth_user, published):

        if published == 2:
            LearningObjectiveDataAccess._delete(db, model, auth_user_id=auth_user.id)
        else:
            model.validate()

            if model.is_valid == True:
                if model.is_new() == True:
                    model = LearningObjectiveDataAccess._insert(db, model, published, auth_user_id=auth_user.id)
                else:
                    LearningObjectiveDataAccess._update(db, model, published, auth_user_id=auth_user.id)
        return model


    @staticmethod
    def publish_item(db, learning_objective_id, scheme_of_work_id, auth_user):
        return LearningObjectiveDataAccess.publish_item(db, learning_objective_id, scheme_of_work_id, auth_user_id=auth_user.id)


    @staticmethod
    def delete(db, model, auth_user):
        """ Delete learning objective """
        model = LearningObjectiveDataAccess._delete(db, model, auth_user_id=auth_user.id)
        return model


    @staticmethod
    def publish(db, model, scheme_of_work_id, auth_user):
        #TODO: verify usage
        return LearningObjectiveDataAccess._publish(db, model, scheme_of_work_id, auth_user_id=auth_user.id)


    @staticmethod
    def delete_unpublished(db, scheme_of_work_id, lesson_id, auth_user):
        return LearningObjectiveDataAccess.delete_unpublished(db, scheme_of_work_id, lesson_id, auth_user_id=auth_user.id)


class LearningObjectiveDataAccess:


    @staticmethod
    #248 Added parameters
    def get_model(db, id_, lesson_id, scheme_of_work_id, auth_user_id):

        execHelper = ExecHelper()
        
        #269 create lesson_learning_objective__get stored procedure

        select_sql = "lesson_learning_objective__get"

        params = (id_, auth_user_id)

        rows = []

        #271 Stored procedure
        rows = execHelper.select(db, select_sql, params, rows, handle_log_info)
        
        return rows


    @staticmethod
    def get_all(db, lesson_id, scheme_of_work_id, auth_user_id):

        execHelper = ExecHelper()

        #269 create lesson_learning_objective__get_all stored procedure

        select_sql = "lesson_learning_objective__get_all"

        params = (lesson_id, scheme_of_work_id, auth_user_id)

        rows = []
        
        #271 Stored procedure
        rows = execHelper.select(db, select_sql, params, rows, handle_log_info)

        return rows


    @staticmethod
    def get_all_pathway_objectives(db, key_stage_id, key_words, auth_user_id):

        execHelper = ExecHelper()

        #269 create learning_objective__get_all_pathway_objectives stored procedure

        select_sql = "lesson_learning_objective__get_all_pathway_objectives"
        
        params = (key_stage_id, auth_user_id)

        rows = []
        
        #271 Stored procedure
        rows = execHelper.select(db, select_sql, params, rows, handle_log_info)
        
        return rows


    @staticmethod
    def get_linked_pathway_objectives(db, lesson_id, auth_user_id):

        execHelper = ExecHelper()
    
        select_sql = "lesson_learning_objective__get_linked_pathway_objectives"
            
        params = (lesson_id, auth_user_id)
        
        rows = []

        #271 Stored procedure
        rows = execHelper.select(db, select_sql, params, rows, handle_log_info)

        data = []

        for row in rows:
            model = LearningObjectiveModel(
                id_ = row[0],
                description = row[1],
                solo_taxonomy_id = row[2],
                solo_taxonomy_name = row[3],
                solo_taxonomy_level = row[4],
                content_id = row[5],
                content_description = row[6],
                key_stage_id = row[7],
                key_stage_name = row[8],
                key_words = row[9],
                group_name = row[10],
                created = row[11],
                created_by_id = row[12],
                created_by_name = row[13]
                )
            
            data.append(model)

        return data


    @staticmethod
    def publish_item(db, id_, scheme_of_work_id, auth_user_id):
        #231: publish item
        model = LearningObjectiveModel(id_=id_)
        model.publish = True
        return LearningObjectiveDataAccess._publish(db, model, scheme_of_work_id, auth_user_id)


    @staticmethod
    def _delete(db, model, auth_user_id):

        execHelper = ExecHelper()

        #269 create lesson_learning_objective__delete stored procedure


        str_delete = "lesson_learning_objective__delete"

        params = (model.id, auth_user_id)

        rval = execHelper.delete(db, str_delete, params, handle_log_info)

        return rval


    @staticmethod
    def delete_unpublished(db, scheme_of_work_id, lesson_id, auth_user_id):
        """ Delete all unpublished learning objectives """

        execHelper = ExecHelper()

        str_delete = "lesson_learning_objective__delete_unpublished"

        params = (scheme_of_work_id, lesson_id, auth_user_id)
            
        row_count = execHelper.delete(db, str_delete, params, handle_log_info)        
        
        return row_count


    @staticmethod
    def _update(db, model, published, auth_user_id):
        execHelper = ExecHelper()
        rows = []
        
        # build update statement
        #269 create learning_objective__update stored procedure
        str_update = "lesson_learning_objective__update"
        
        params = (model.id, model.lesson_id, model.description, model.group_name, model.notes, model.key_words, model.solo_taxonomy_id, model.content_id, model.parent_id, published, auth_user_id)
        
        rows = execHelper.update(db, str_update, params, handle_log_info)

        return rows


    @staticmethod
    def _insert(db, model, published, auth_user_id):
        execHelper = ExecHelper()
        
        #TODO: #269 create learning_objective__insert stored procedure (1 of 2 insert sow_learning_objective)

        str_insert = "lesson_learning_objective__insert"
        
        params = (
            model.id,
            model.lesson_id,
            model.description,
            model.group_name,
            model.notes,
            model.key_words,
            model.solo_taxonomy_id,
            model.content_id,
            model.parent_id,
            model.created,
            model.created_by_id,
            published,
            auth_user_id
        )
        
        results = execHelper.insert(db, str_insert, params, handle_log_info)
    
        for res in results:
            model.id = res

        return model


    @staticmethod
    def _publish(db, model, scheme_of_work_id, auth_user_id):
    
        execHelper = ExecHelper()

        #269 create lesson_learning_objective__publish stored procedure

        str_publish = "lesson_learning_objective__publish_item"
        params = (model.id, model.lesson_id, scheme_of_work_id, 1 if model.published else 0, auth_user_id)

        rval = []
        rval = execHelper.update(db, str_publish, params)

        return rval
