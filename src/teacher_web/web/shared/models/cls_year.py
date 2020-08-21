# -*- coding: utf-8 -*-
from django.db import models
from shared.models.core.db_helper import ExecHelper, sql_safe
from shared.models.core.basemodel import BaseModel


class YearModel(models.Model):
    def __init__(self, id_, name):
        self.id = id_
        self.name = name


    def _clean_up(self):
        """ clean up properties by removing by casting and ensuring safe for inserting etc """

        # id
        self.id = int(self.id)

        # name
        if self.name is not None:
            self.name = sql_safe(self.name)


    @staticmethod
    def get_options(db, key_stage_id, auth_user):
        rows = YearDataAccess.get_options(db, key_stage_id, auth_user)
        data = []
        for row in rows:
            model = YearModel(row[0], row[1])
            data.append(model)
        return data


class YearDataAccess:

    @staticmethod
    def get_options(db, key_stage_id, auth_user):
        helper = ExecHelper()

        str_select = "year__get_options"
        params = (key_stage_id, auth_user)

        rows = []
        rows = helper.select(db, str_select, params, rows)

        return rows