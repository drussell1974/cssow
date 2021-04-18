# -*- coding: utf-8 -*-
from .core.db_helper import ExecHelper, sql_safe
from shared.models.core.log_handlers import handle_log_info
from shared.models.enums.publlished import STATE
from shared.models.core.basemodel import BaseModel


class TopicModel(BaseModel):

    name = ""
    department_id = 0

    def __init__(self, id_, name, department_id, lvl=1, created = "", created_by = ""):
        self.id = id_
        self.name = name
        self.department_id = department_id
        self.lvl = lvl
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
        #self._validate_required_string("name", self.name, 1, 45)
        
        self.on_after_validate()


    @staticmethod
    def get_options(db, lvl, auth_user, topic_id = 0):
        rows = TopicDataAccess.get_options(db, lvl, auth_user_id=auth_user.auth_user_id, topic_id=topic_id, show_published_state=STATE.PUBLISH)
        data = []
        
        for row in rows:
            model = TopicModel(row[0], name=row[1], department_id=row[2], created=row[3], created_by=row[4])
            # TODO: remove __dict__ . The object should be serialised to json further up the stack
            data.append(model.__dict__)
        return data


class TopicDataAccess:
    
    @staticmethod
    def get_options(db, lvl, auth_user_id, show_published_state=STATE.PUBLISH, topic_id = 0):
        
        execHelper = ExecHelper()

        str_select = "topic__get_options$2"
        params = (topic_id, lvl, int(show_published_state), auth_user_id)

        try:
            rows = []
            #271 Stored procedure (get_options)
            rows = execHelper.select(db, str_select, params, rows, handle_log_info)
            
            return rows

        except Exception as e:
            raise Exception("Error getting topics", e)
