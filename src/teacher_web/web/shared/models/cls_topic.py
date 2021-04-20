# -*- coding: utf-8 -*-
from .core.db_helper import ExecHelper, sql_safe
from shared.models.core.log_handlers import handle_log_info
from shared.models.enums.publlished import STATE
from shared.models.core.basemodel import BaseModel, try_int


class TopicModel(BaseModel):

    name = ""
    department_id = 0
    parent_id = None

    def __init__(self, id_, name, lvl=0, all_topic_names=[], created = "", created_by = "", created_by_id = 0, created_by_name = "", published=STATE.PUBLISH, is_from_db=False, auth_ctx=None):
        super().__init__(id_, display_name=name, created=created, created_by_id=created_by_id, created_by_name=created_by_name, published=published, is_from_db=is_from_db, ctx=auth_ctx)

        self.id = id_
        self.name = name
        self.lvl = lvl
        self.parent = None
        self.all_topic_names = all_topic_names # not implemented
        self.created = created
        self.created_by = created_by


    def _clean_up(self):
        """ clean up properties by removing by casting and ensuring safe for inserting etc """

        # id
        self.id = int(self.id)

        # name
        if self.name is not None:
            self.name = sql_safe(self.name)


    def validate(self, skip_validation = []):
        """ clean up and validate model """
        super().validate(skip_validation)

        # validate name
        self._validate_required_string("name", self.name, 1, 45)
        
        self.on_after_validate()


    @staticmethod
    def get_model(db, topic_id, auth_ctx):
        rows = TopicDataAccess.get_model(db, topic_id=topic_id, department_id=auth_ctx.department_id, auth_user_id=auth_ctx.auth_user_id, show_published_state=STATE.PUBLISH)
        model = None
        
        for row in rows:
            model = TopicModel(row[0], name=row[1], lvl=row[2], created=row[3], created_by=row[4], published=row[5], auth_ctx=auth_ctx)
            if row[6] is not None: # if parent row
                model.parent = TopicModel(row[6], name=row[7], lvl=row[8], created=row[9], created_by=row[10], auth_ctx=auth_ctx)
                model.parent_id = model.parent.id
                model.lvl = model.parent.lvl + 1
            model.on_fetched_from_db()
            return model
        return model


    @staticmethod
    def get_all(db, auth_ctx):
        rows = TopicDataAccess.get_all(db, department_id=auth_ctx.department_id, auth_user_id=auth_ctx.auth_user_id, show_published_state=STATE.PUBLISH)
        data = []
        
        for row in rows:
            model = TopicModel(row[0], name=row[1], lvl=row[2], created=row[3], created_by=row[4], published=row[5], auth_ctx=auth_ctx)
            if row[6] is not None: # if parent row
                model.parent = TopicModel(row[6], name=row[7], lvl=row[8], created=row[9], created_by=row[10], auth_ctx=auth_ctx)
                model.parent_id = model.parent.id
                model.lvl = model.parent.lvl + 1
            data.append(model)
        return data


    @staticmethod
    def get_options(db, lvl, auth_ctx, topic_id = 0):
        rows = TopicDataAccess.get_options(db, lvl, department_id=auth_ctx.department_id, auth_user_id=auth_ctx.auth_user_id, topic_id=topic_id, show_published_state=STATE.PUBLISH)
        data = []
        
        for row in rows:
            model = TopicModel(row[0], name=row[1], lvl=row[2], created=row[3], created_by=row[4], published=row[5], auth_ctx=auth_ctx)
            if row[6] is not None: # if parent row
                model.parent = TopicModel(row[6], name=row[7], lvl=row[8], created=row[9], created_by=row[10], auth_ctx=auth_ctx)
                model.parent_id = model.parent.id
                model.lvl = model.parent.lvl + 1
            # TODO: remove __dict__ . The object should be serialised to json further up the stack
            data.append(model.__dict__)
        return data


    @staticmethod
    def save(db, model, auth_ctx, published=STATE.PUBLISH):
        if try_int(model.published) == STATE.DELETE or try_int(published) == STATE.DELETE:
            TopicDataAccess._delete(db, model, auth_ctx.auth_user_id)
            model.published = STATE.DELETE
        else:
            if model.is_new() == True:
                new_id = TopicDataAccess._insert(db, model, published, auth_user_id=auth_ctx.auth_user_id)
                model.id = new_id[0]
            else:
                TopicDataAccess._update(db, model, published, auth_user_id=auth_ctx.auth_user_id)

        return model


    @staticmethod
    def delete_unpublished(db, auth_user):
        rows = TopicDataAccess.delete_unpublished(db, department_id=auth_user.department_id, auth_user_id=auth_user.auth_user_id)
        return rows


class TopicDataAccess:
    
    @staticmethod
    def get_model(db, topic_id, department_id, auth_user_id, show_published_state=STATE.PUBLISH):
        
        execHelper = ExecHelper()

        str_select = "topic__get_model"
        params = (topic_id, department_id, int(show_published_state), auth_user_id)

        try:
            rows = []
            rows = execHelper.select(db, str_select, params, rows, handle_log_info)
            
            return rows

        except Exception as e:
            raise Exception("Error getting topic {}".format(topic_id), e)


    @staticmethod
    def get_all(db, department_id, auth_user_id, show_published_state=STATE.PUBLISH):
        
        execHelper = ExecHelper()

        str_select = "topic__get_all"
        params = (department_id, int(show_published_state), auth_user_id)

        rows = []
        
        rows = execHelper.select(db, str_select, params, rows, handle_log_info)
        
        return rows


    @staticmethod
    def get_options(db, lvl, department_id, auth_user_id, show_published_state=STATE.PUBLISH, topic_id = 0):
        
        execHelper = ExecHelper()

        str_select = "topic__get_options$2"
        params = (topic_id, department_id, lvl, int(show_published_state), auth_user_id)

        rows = []
        
        rows = execHelper.select(db, str_select, params, rows, handle_log_info)
        
        return rows


    @staticmethod
    def _insert(db, model, published, auth_user_id):
        """ inserts the sow_topic """
        execHelper = ExecHelper()

        sql_insert_statement = "topic__insert"
        params = (
            model.id,
            model.name,
            model.department_id,
            model.parent_id, # if model.parent is not None else 0,
            model.lvl,
            int(published),
            auth_user_id
        )
        
        result = execHelper.insert(db, sql_insert_statement, params, handle_log_info)

        return result


    @staticmethod
    def _update(db, model, published, auth_user_id):
        """ updatss the topic"""
        
        execHelper = ExecHelper()
        
        str_update = "topic__update"
        params = (
            model.id,
            model.name,
            model.department_id,
            model.parent_id, # if model.parent is not None else 0,
            model.lvl,
            int(model.published),
            auth_user_id
        )
        
        result = execHelper.update(db, str_update, params, handle_log_info)

        return result


    @staticmethod
    def _delete(db, model, auth_user_id):

        execHelper = ExecHelper()

        sql = "topic__delete"
        params = (model.id, try_int(model.published), auth_user_id)
    
        rows = execHelper.delete(db, sql, params, handle_log_info)
        
        return rows


    @staticmethod
    def delete_unpublished(db, department_id, auth_user_id):
        """ Delete all unpublished keywords for the scheme of work"""

        execHelper = ExecHelper()
        
        str_delete = "topic__delete_unpublished"
        params = (department_id, auth_user_id)
        
        rval = execHelper.delete(db, str_delete, params, handle_log_info)
        return rval
