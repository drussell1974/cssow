# -*- coding: utf-8 -*-
from .core.basemodel import BaseModel, try_int
from .core.db_helper import ExecHelper, sql_safe
from shared.models.core.log_handlers import handle_log_info
from shared.models.enums.publlished import STATE
from shared.models.cls_topic import TopicModel
from shared.models.cls_year import YearModel


class KS123PathwayModel(BaseModel):
    def __init__(self, id_, objective, ctx, year_id=0, topic_id=0, created = "", created_by_id = 0, created_by_name = "", published=STATE.PUBLISH, is_from_db=False):
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

        if self.ctx is None:
            raise Exception("missing context")

        # do not validate deleted items
        if self.published == STATE.DELETE:
            self.is_valid = True;
            self.on_after_validate()
            return

        # validate objective
        self._validate_required_string("objective", self.objective, 1, 500)
        # validate year_id
        self._validate_required_integer("year_id", self.year_id, min_value=1, max_value=KS123PathwayModel.MAX_INT)
        # validate topic_id
        self._validate_required_integer("topic_id", self.topic_id, min_value=1, max_value=KS123PathwayModel.MAX_INT)
        
        self.on_after_validate()


    def _clean_up(self):
        """ clean up properties by removing by casting and ensuring safe for inserting etc """

        # id
        self.id = try_int(self.id)
        # objective
        if self.objective is not None:
            self.objective = sql_safe(self.objective)
        # topic id
        self.topic_id = try_int(self.topic_id)
        # year id
        self.year_id = try_int(self.year_id)
    
    
    @staticmethod
    def get_options(db, key_stage_id, topic_id, auth_user):
        rows = KS123PathwayDataAccess.get_options(db, auth_user.department_id, key_stage_id, topic_id, auth_user_id=auth_user.auth_user_id, show_published_state=auth_user.can_view)
        data = []
        for row in rows:
            model = KS123PathwayModel(row[0], row[1], ctx=auth_user)
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
    def get_model(cls, db, pathway_item_id, auth_ctx):

        rows = KS123PathwayDataAccess.get_model(db, pathway_item_id=pathway_item_id, department_id=auth_ctx.department_id, auth_user_id=auth_ctx.auth_user_id, show_published_state=auth_ctx.can_view)
        model = None
        for row in rows:
            model = KS123PathwayModel(row[0], row[1], year_id=row[2], topic_id=row[4], published = row[6], ctx=auth_ctx)
            model.year = YearModel(row[2], row[3])
            model.topic = TopicModel(row[4], name=row[5], auth_ctx=auth_ctx)
            
            return model        
        return model


    @classmethod
    def get_all(cls, db, department_id, auth_ctx):

        rows = KS123PathwayDataAccess.get_all(db, department_id=department_id, auth_user_id=auth_ctx.auth_user_id, show_published_state=auth_ctx.can_view)
        data = []
        for row in rows:
            model = KS123PathwayModel(row[0], row[1], year_id=row[2], topic_id=row[4], published = row[6], ctx=auth_ctx)
            model.year = YearModel(row[2], row[3])
            model.topic = TopicModel(row[4], row[5], auth_ctx=auth_ctx.department_id)

            data.append(model)
        
        return data


    @staticmethod
    def save(db, model, auth_ctx):
        """ save model """
        if model.published == STATE.DELETE:
            data = KS123PathwayDataAccess.delete(db, model.id, auth_ctx.department_id, auth_user_id=auth_ctx.auth_user_id)
        else:
            if model.is_new():
                data = KS123PathwayDataAccess._insert(db, model, auth_user_id=auth_ctx.auth_user_id)
                model.id = data[0]
            else:
                data = KS123PathwayDataAccess._update(db, model, auth_user_id=auth_ctx.auth_user_id)
            
        return model


class KS123PathwayDataAccess:

    @staticmethod
    def get_options(db, department_id, key_stage_id, topic_id, auth_user_id, show_published_state=STATE.PUBLISH):

        execHelper = ExecHelper()

        str_select = "ks123_pathway__get_options$2"
        params = (department_id, key_stage_id, topic_id, int(show_published_state), auth_user_id)
        
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
    def get_model(db, pathway_item_id, department_id, auth_user_id, show_published_state=STATE.PUBLISH):
        
        execHelper = ExecHelper()

        str_select = "ks123_pathway__get_model"
        params = (pathway_item_id, department_id, int(show_published_state), auth_user_id)
        
        rows = []

        rows = execHelper.select(db, str_select, params, rows, handle_log_info)

        return rows


    @staticmethod
    def get_all(db, department_id, auth_user_id, show_published_state=STATE.PUBLISH):
        
        execHelper = ExecHelper()

        str_select = "ks123_pathway__get_all"
        params = (department_id, int(show_published_state), auth_user_id)
        
        rows = []

        rows = execHelper.select(db, str_select, params, rows, handle_log_info)

        return rows


    @staticmethod
    def _insert(db, model, auth_user_id):
        """ Inserts pathway """
        
        execHelper = ExecHelper()

        stored_procedure = "ks123_pathway__insert"

        params = (model.id, model.objective, model.department_id, model.year_id, model.topic_id, try_int(model.published), auth_user_id)    
    
        new_id = execHelper.insert(db,
            stored_procedure
            , params
            , handle_log_info
        )
        
        return new_id


    @staticmethod
    def _update(db, model, auth_user_id):
        """ Updates pathway """
        
        execHelper = ExecHelper()
        
        str_update = "ks123_pathway__update"
        
        params = (model.id, model.objective, model.department_id, model.year_id, model.topic_id, try_int(model.published), auth_user_id)
        
        execHelper.update(db, str_update, params, handle_log_info)

        return model
 

    @staticmethod
    def delete(db, id, department_id, auth_user_id):
        """ Delete the keyword by term """

        execHelper = ExecHelper()
        
        str_delete = "ks123_pathway__delete"
        
        params = (id, department_id, auth_user_id)

        rval = execHelper.delete(db, str_delete, params, handle_log_info)
        return rval
      