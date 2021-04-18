# -*- coding: utf-8 -*-
from .core.db_helper import ExecHelper, sql_safe
from shared.models.core.log_handlers import handle_log_info
from shared.models.enums.publlished import STATE
from shared.models.core.basemodel import BaseModel


class TopicModel(BaseModel):

    name = ""
    department_id = 0

    def __init__(self, id_, name, lvl=1, all_topic_names=[], created = "", created_by = "", created_by_id = 0, created_by_name = "", published=STATE.PUBLISH, is_from_db=False, auth_ctx=None):
        super().__init__(id_, display_name=name, created=created, created_by_id=created_by_id, created_by_name=created_by_name, published=published, is_from_db=is_from_db, ctx=auth_ctx)

        self.id = id_
        self.name = name
        self.lvl = lvl
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
            model = TopicModel(row[0], name=row[1], created=row[2], created_by=row[3], auth_ctx=auth_ctx)
            model.on_fetched_from_db()
            return model
        return model


    @staticmethod
    def get_options(db, lvl, auth_ctx, topic_id = 0):
        rows = TopicDataAccess.get_options(db, lvl, department_id=auth_ctx.department_id, auth_user_id=auth_ctx.auth_user_id, topic_id=topic_id, show_published_state=STATE.PUBLISH)
        data = []
        
        for row in rows:
            model = TopicModel(row[0], name=row[1], created=row[2], created_by=row[3], auth_ctx=auth_ctx)
            # TODO: remove __dict__ . The object should be serialised to json further up the stack
            data.append(model.__dict__)
        return data


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
    def get_options(db, lvl, department_id, auth_user_id, show_published_state=STATE.PUBLISH, topic_id = 0):
        
        execHelper = ExecHelper()

        str_select = "topic__get_options$2"
        params = (topic_id, department_id, lvl, int(show_published_state), auth_user_id)

        try:
            rows = []
            #271 Stored procedure (get_options)
            rows = execHelper.select(db, str_select, params, rows, handle_log_info)
            
            return rows

        except Exception as e:
            raise Exception("Error getting topics", e)
