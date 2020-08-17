# -*- coding: utf-8 -*-
from datetime import datetime
from .core.db_helper import to_db_null, to_empty, sql_safe, to_db_bool
from .core.basemodel import BaseModel, try_int
from .core.db_helper import ExecHelper, sql_safe, from_db_bool
from .core.log import handle_log_info


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
        self.is_key_objective = from_db_bool(is_key_objective)
    
        self.set_published_state()  
            

    def validate(self):

        """ clean up and validate model """

        self._on_before_validate()

        # clean properties before validation
        self._clean_up()

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
        rows =  LearningObjectiveDataAccess.get_model(db, learning_objective_id, lesson_id, scheme_of_work_id, auth_user)
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
        rows = LearningObjectiveDataAccess.get_all(db, lesson_id, scheme_of_work_id, auth_user)
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


    #@staticmethod
    #def get_lesson_learning_objective_ids(db, lesson_id, auth_user):
    #    return LearningObjectiveDataAccess.get_lesson_learning_objective_ids(db, lesson_id, auth_user)


    @staticmethod
    def get_all_pathway_objectives(db, key_stage_id, key_words):
        rows = LearningObjectiveDataAccess.get_all_pathway_objectives(db, key_stage_id, key_words)
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
    def get_linked_pathway_objectives(db, lesson_id):
        return LearningObjectiveDataAccess.get_linked_pathway_objectives(db, lesson_id)


    @staticmethod
    def save(db, model, auth_user, published):

        if published == 2:
            LearningObjectiveDataAccess._delete(db, model, auth_user)
        else:
            model.validate()

            if model.is_valid == True:
                if model.is_new() == True:
                    model = LearningObjectiveDataAccess._insert(db, model, published, auth_user)
                else:
                    LearningObjectiveDataAccess._update(db, model, published, auth_user)
        return model


    @staticmethod
    def publish_item(db, learning_objective_id, scheme_of_work_id, auth_user):
        return LearningObjectiveDataAccess.publish_item(db, learning_objective_id, scheme_of_work_id, auth_user)


    @staticmethod
    def delete(db, model, auth_user):
        """ Delete learning objective """
        model = LearningObjectiveDataAccess._delete(db, model, auth_user)
        return model


    @staticmethod
    def publish(db, model, scheme_of_work_id, auth_user):
        return LearningObjectiveDataAccess._publish(db, model, scheme_of_work_id, auth_user)


    @staticmethod
    def delete_unpublished(db, lesson_id, auth_user):
        return LearningObjectiveDataAccess.delete_unpublished(db, lesson_id, auth_user)


class LearningObjectiveDataAccess:


    @staticmethod
    #248 Added parameters
    def get_model(db, id_, lesson_id, scheme_of_work_id, auth_user):

        execHelper = ExecHelper()
        
        #269 create lesson_learning_objective__get stored procedure

        select_sql = "CALL lesson_learning_objective__get({learning_objective_id},{auth_user})"\
            .format(
                learning_objective_id=int(id_)
                , auth_user=to_db_null(auth_user)
            )

        rows = []
        rows = execHelper.execSql(db, select_sql, rows, log_info=handle_log_info)
        return rows


    @staticmethod
    def get_all(db, lesson_id, scheme_of_work_id, auth_user):

        execHelper = ExecHelper()

        #269 create lesson_learning_objective__get_all stored procedure

        select_sql = "CALL lesson_learning_objective__get_all({lesson_id},{scheme_of_work_id},{auth_user});"\
            .format(lesson_id=int(lesson_id), scheme_of_work_id=scheme_of_work_id, auth_user=to_db_null(auth_user))

        rows = []
        rows = execHelper.execSql(db, select_sql, rows)
        return rows

    @staticmethod
    def get_all_pathway_objectives(db, key_stage_id, key_words):

        execHelper = ExecHelper()

        #TODO: #269 create learning_objective__get_all_pathway_objectives stored procedure

        select_sql = "SELECT"\
                    " lob.id as id,"\
                    " lob.description as description,"\
                    " solo.id as solo_id,"\
                    " solo.name as solo_taxonomy_name,"\
                    " solo.lvl as solo_taxonomy_level,"\
                    " cnt.id as content_id,"\
                    " cnt.description as content_description,"\
                    " ks.id as key_stage_id,"\
                    " ks.name as key_stage_name,"\
                    " lob.key_words as key_words,"\
                    " lob.group_name as group_name,"\
                    " lob.created as created,"\
                    " lob.created_by as created_by_id,"\
                    " CONCAT_WS(' ', user.first_name, user.last_name) as created_by_name"\
                    " FROM sow_learning_objective as lob"\
                    " LEFT JOIN sow_topic as top ON top.id = lob.topic_id"\
                    " LEFT JOIN sow_topic as pnt_top ON pnt_top.id = top.parent_id"\
                    " LEFT JOIN sow_solo_taxonomy as solo ON solo.id = lob.solo_taxonomy_id"\
                    " LEFT JOIN sow_content as cnt ON cnt.id = lob.content_id"\
                    " LEFT JOIN sow_key_stage as ks ON ks.id = cnt.key_stage_id"\
                    " LEFT JOIN auth_user as user ON user.id = lob.created_by"\
                    " WHERE ks.id < {key_stage_id}" \
                    " ORDER BY ks.name DESC, solo.lvl;"

        select_sql = select_sql.format(key_stage_id=int(key_stage_id))

        rows = []
        rows = execHelper.execSql(db, select_sql, rows)
        return rows


    @staticmethod
    def publish_item(db, id_, scheme_of_work_id, auth_user):
        #231: publish item
        model = LearningObjectiveModel(id_=id_)
        model.publish = True
        return LearningObjectiveDataAccess._publish(db, model, scheme_of_work_id, auth_user)


    @staticmethod
    def _delete(db, model, auth_user):

        execHelper = ExecHelper()

        #269 create lesson_learning_objective__delete stored procedure


        str_delete = "CALL lesson_learning_objective__delete({learning_objective_id},{auth_user});"\
            .format(learning_objective_id=model.id, auth_user=auth_user)

        rval = execHelper.execCRUDSql(db, str_delete, log_info=handle_log_info)

        return rval


    @staticmethod
    def delete_unpublished(db, lesson_id, auth_user):
        """ Delete all unpublished learning objectives """

        execHelper = ExecHelper()

        str_delete = "CALL lesson_learning_objective__delete_unpublished({lesson_id},{auth_user});"\
            .format(lesson_id=lesson_id,auth_user=auth_user)
            
        execHelper.execCRUDSql(db, str_delete, log_info=handle_log_info)        
        

    @staticmethod
    def _update(db, model, published, auth_user):
        execHelper = ExecHelper()
        rows = []
        
        # build update statement
        #269 create learning_objective__update stored procedure
        str_update = "CALL lesson_learning_objective__update({learning_objective_id},{lesson_id},'{description}', '{group_name}','{notes}','{key_words}',{solo_taxonomy_id},{content_id},{parent_id},{published},{auth_user});"\
            .format(learning_objective_id=model.id, lesson_id=model.lesson_id, description=model.description, group_name=to_db_null(model.group_name), notes=to_db_null(model.notes), key_words=to_db_null(model.key_words), solo_taxonomy_id=model.solo_taxonomy_id, content_id=to_db_null(model.content_id), parent_id=to_db_null(model.parent_id), published=to_db_null(published), auth_user =auth_user)
        rows = execHelper.execCRUDSql(db, str_update, log_info=handle_log_info)
    
        #rows = LearningObjectiveDataAccess._update_lesson_lessonobjectives(db, model, rows)

        return rows


    @staticmethod
    def _insert(db, model, published, auth_user):
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
            auth_user
        )
        
        results = execHelper.insert(db, str_insert, params, log_info=handle_log_info)
    
        for res in results:
            model.id = res

        return model


    @staticmethod
    def _publish(db, model, scheme_of_work_id, auth_user):
    
        execHelper = ExecHelper()

        #269 create lesson_learning_objective__publish stored procedure

        str_publish = "lesson_learning_objective__publish_item"
        params = (model.id, model.lesson_id, scheme_of_work_id, 1 if model.published else 0, auth_user)

        rval = []
        rval = execHelper.update(db, str_publish, params)

        return rval

    '''
    @staticmethod
    def _insert_lesson_lessonobjectives(db, model, results):
        """ insert into linking table between objective and lesson """
        
        #TODO: #269 create lesson_learning_objective__insert stored procedure

        execHelper = ExecHelper()

        str_insert = "INSERT INTO sow_learning_objective__has__lesson (learning_objective_id, lesson_id) VALUES ({learning_objective_id}, {lesson_id});"
        str_insert = str_insert.format(learning_objective_id=model.id, lesson_id=model.lesson_id)
        
        results = execHelper.execCRUDSql(db, str_insert, log_info=handle_log_info)

        return results

    @staticmethod
    def _update_lesson_lessonobjectives(db, model, results):
        """ insert if entry in sow_learning_objective__has__lesson doesn't already map sow learning_objective and sow_lesson """

        #TODO: #269 create lesson_learning_objective__update stored procedure

        execHelper = ExecHelper()

        str_check_duplicate = "SELECT id FROM sow_learning_objective__has__lesson WHERE learning_objective_id = {learning_objective_id} AND lesson_id = {lesson_id};"
        str_check_duplicate = str_check_duplicate.format(learning_objective_id=model.id, lesson_id=model.lesson_id)
        
        duplicates = [] 
        duplicates = execHelper.execSql(db, str_check_duplicate, duplicates, handle_log_info)

        if(len(duplicates) == 0):
            str_insert2 = "INSERT INTO sow_learning_objective__has__lesson (learning_objective_id, lesson_id) VALUES ({learning_objective_id}, {lesson_id});"
            str_insert2 = str_insert2.format(learning_objective_id=model.id, lesson_id=model.lesson_id)
            results = execHelper.execCRUDSql(db, str_insert2, log_info=handle_log_info)
        
        return results
    '''

    @staticmethod
    def get_linked_pathway_objectives(db, lesson_id):

        execHelper = ExecHelper()

        select_sql = "SELECT"\
                    " lob.id as id,"\
                    " lob.description as description,"\
                    " solo.id as solo_id,"\
                    " solo.name as solo_taxonomy_name,"\
                    " solo.lvl as solo_taxonomy_level,"\
                    " cnt.id as content_id,"\
                    " cnt.description as content_description,"\
                    " ks.id as key_stage_id,"\
                    " ks.name as key_stage_name,"\
                    " lob.key_words as key_words,"\
                    " lob.group_name as group_name,"\
                    " lob.created as created,"\
                    " lob.created_by as created_by_id,"\
                    " CONCAT_WS(' ', user.first_name, user.last_name) as created_by_name"\
                    " FROM sow_learning_objective as lob"\
                    " INNER JOIN sow_lesson__has__pathway as pw ON pw.learning_objective_id = lob.id"\
                    " LEFT JOIN sow_solo_taxonomy as solo ON solo.id = lob.solo_taxonomy_id"\
                    " LEFT JOIN sow_content as cnt ON cnt.id = lob.content_id"\
                    " LEFT JOIN sow_key_stage as ks ON ks.id = cnt.key_stage_id"\
                    " LEFT JOIN auth_user as user ON user.id = lob.created_by"\
                    " WHERE pw.lesson_id = {lesson_id}" \
                    " ORDER BY ks.name DESC, solo.lvl;"

        select_sql = select_sql.format(lesson_id=int(lesson_id))
        
        rows = []
        rows = execHelper.execSql(db, select_sql, rows)

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


    # DEPRECATED
'''

    @staticmethod
    def sort_by_solo_taxonomy_level(unsorted_list):
        """
        Bubble sort by solo taxonomy level
        :param unsorted_list: the unsorted data
        :return: a sorted list
        """

        raise DeprecationWarning("No longer used.")

        staging_list = unsorted_list

        while True:
            swapped = False
            for i in range(len(staging_list)-1):
                if staging_list[i].solo_taxonomy_level > staging_list[i+1].solo_taxonomy_level:
                    """ put item in the correct position """
                    temp1 = staging_list[i]
                    temp2 = staging_list[i+1]

                    staging_list[i] = temp2
                    staging_list[i+1] = temp1
                    swapped = True

            if swapped == False:
                """ no more sorting required so finish """
                break

        return staging_list


    @staticmethod
    def update_is_key_objective(db, learning_objective_id, lesson_id, is_key_objective):
        
        raise DeprecationWarning("No longer used.")

        execHelper = ExecHelper()
        str_update = "UPDATE sow_learning_objective__has__lesson SET is_key_objective = {is_key_objective} WHERE learning_objective_id = {learning_objective_id};"
        str_update = str_update.format(learning_objective_id=int(learning_objective_id), lesson_id=int(lesson_id), is_key_objective=to_db_bool(is_key_objective))

        result = execHelper.execCRUDSql(db, str_update, log_info=handle_log_info)

        return result
'''