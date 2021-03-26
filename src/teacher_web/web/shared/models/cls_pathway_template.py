# -*- coding: utf-8 -*-
from django.db import models
from shared.models.core.log_handlers import handle_log_info
from shared.models.core.db_helper import ExecHelper, sql_safe
from shared.models.core.basemodel import BaseModel, try_int
from shared.models.enums.publlished import STATE

class PathwayTemplateModel(BaseModel):
    """ Creates current pathway (e.g. KS4) and past stages for pathway """

    def __init__(self, id_, name, department_id=0, created = "", created_by_id = 0, created_by_name = "", published=STATE.PUBLISH, is_from_db=False, ctx=None):
        super().__init__(id_, display_name=name, created=created, created_by_id=created_by_id, created_by_name=created_by_name, published=published, is_from_db=is_from_db, ctx=ctx)
        self.id = id_
        self.name = name
        self.key_stage_id = 0
        self.department_id = department_id


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

        # Validate department
        self._validate_required_integer("department_id", self.department_id, 1, BaseModel.MAX_INT)

        self.on_after_validate()


    @staticmethod
    def get_options(db):
        rows = PathwayTemplateAccess.get_options(db)
        data = []
        for row in rows:
            model = PathwayTemplateModel(row[0], row[1])
            data.append((model.id, model.name))
        return data


    @staticmethod
    def save(db, model, auth_user):
        """ save model """
        result = PathwayTemplateAccess._insert(db, model, department_id=model.department_id, auth_user_id=auth_user.auth_user_id)
        #model.key_stage_id = result[0]
        return model


class PathwayTemplateAccess:

    @staticmethod
    def get_options(db):
        helper = ExecHelper()

        str_select = "pathway_template__get_options"
        #params = ()

        rows = []
        rows = helper.select(db, str_select, rows, handle_log_info)

        return rows


    @staticmethod
    def _insert(db, model, department_id, auth_user_id):
        """ inserts the pathway option to create key stages """
        execHelper = ExecHelper()
        
        sql_insert_statement = "keystage__insert_from_pathway_template"
        params = (
            model.id,
            department_id,
            model.created,
            auth_user_id,
            int(model.published)
        )
        
        result = execHelper.insert(db, sql_insert_statement, params, handle_log_info)

        return result
