# -*- coding: utf-8 -*-
from django.db import models
from shared.models.core.log_handlers import handle_log_info
from shared.models.core.db_helper import ExecHelper, sql_safe
from shared.models.core.basemodel import BaseModel


class DeliveryTemplateModel(models.Model):
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
    def get_options(db):
        rows = DeliveryTemplateAccess.get_options(db)
        data = []
        for row in rows:
            #model = DeliveryTemplateModel(row[0], row[1])
            data.append((row[0], row[1]))
        return data


class DeliveryTemplateAccess:

    @staticmethod
    def get_options(db):
        helper = ExecHelper()

        str_select = "delivery_template__get_options"
        #params = ()

        rows = []
        rows = helper.select(db, str_select, rows, handle_log_info)

        return rows