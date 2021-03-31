# -*- coding: utf-8 -*-
from .core.basemodel import BaseModel
from .core.db_helper import ExecHelper, sql_safe
from shared.models.core.log_handlers import handle_log_info
from shared.models.enums.publlished import STATE
from shared.models.cls_topic import TopicModel
from shared.models.cls_year import YearModel


class KS123PathwayModel(BaseModel):
    def __init__(self, id_, objective, year_id=0, topic_id=0, created = "", created_by_id = 0, created_by_name = "", published=STATE.PUBLISH, is_from_db=False, ctx=None):
        super().__init__(id_, objective, created, created_by_id, created_by_name, published, is_from_db, ctx=ctx)

        self.id = id_
        self.objective = objective
        self.year_id = year_id
        self.year = None
        self.topic_id = topic_id
        self.topic = None
        self.is_checked = False


    def validate(self, skip_validation = []):
        """ clean up and validate model """
        super().validate(skip_validation)

        # do not validate deleted items
        if self.published == STATE.DELETE:
            self.is_valid = True;
            self.on_after_validate()
            return

        # validate objective
        self._validate_optional_string("objective", self.objective, 500)
        # validate year_id
        self._validate_required_integer("year_id", self.year_id, min_value=1, max_value=KS123PathwayModel.MAX_INT)
        # validate topic_id
        self._validate_required_integer("topic_id", self.topic_id, min_value=1, max_value=KS123PathwayModel.MAX_INT)

        self.on_after_validate()


    def _clean_up(self):
        """ clean up properties by removing by casting and ensuring safe for inserting etc """

        # id
        self.id = int(self.id)

        # objective
        if self.objective is not None:
            self.objective = sql_safe(self.objective)
    
    
    @staticmethod
    def get_options(db, key_stage_id, topic_id, auth_user):
        rows = KS123PathwayDataAccess.get_options(db, key_stage_id, topic_id, auth_user_id=auth_user.auth_user_id, show_published_state=auth_user.can_view)
        data = []
        for row in rows:
            model = KS123PathwayModel(row[0], row[1])
            data.append(model)
        return data


    @staticmethod
    def get_linked_pathway_ks123(db, lesson_id, auth_user):
        rows = KS123PathwayDataAccess.get_linked_pathway_ks123(db, lesson_id, auth_user_id=auth_user.auth_user_id)
        data = []
        for row in rows:
            data.append([int(row[0]), row[1]])
        return data


    @classmethod
    def get_all(cls, db, department_id, auth_ctx):

        rows = KS123PathwayDataAccess.get_all(db, department_id=department_id, auth_user_id=auth_ctx.auth_user_id, show_published_state=auth_ctx.can_view)
        data = []
        for row in rows:
            model = KS123PathwayModel(row[0], row[1], year_id=row[2], topic_id=row[4])
            model.year = YearModel(row[2], row[3])
            model.topic = TopicModel(row[4], row[5])
            data.append(model)
        
        return data


class KS123PathwayDataAccess:

    @staticmethod
    def get_options(db, key_stage_id, topic_id, auth_user_id, show_published_state=STATE.PUBLISH):

        execHelper = ExecHelper()

        str_select = "ks123_pathway__get_options"
        params = (key_stage_id, topic_id, int(show_published_state), auth_user_id)
        
        rows = []

        #271 Stored procedure (get_options)
        rows = execHelper.select(db, str_select, params, rows, handle_log_info)

        return rows


    @staticmethod
    def get_linked_pathway_ks123(db, lesson_id, auth_user_id):

        execHelper = ExecHelper()
        

        select_sql = "ks123_pathway__get_linked_pathway"

        params = (lesson_id, auth_user_id)

        rows = []
        #271 Stored procedure
        rows = execHelper.select(db, select_sql, params, rows, handle_log_info)
        return rows

    @staticmethod
    def get_all(db, department_id, auth_user_id, show_published_state=STATE.PUBLISH):
        
        execHelper = ExecHelper()

        str_select = "ks123_pathway__get_all"
        params = (department_id, int(show_published_state), auth_user_id)
        
        rows = []

        rows = execHelper.select(db, str_select, params, rows, handle_log_info)

        return rows
        