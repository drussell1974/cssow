# -*- coding: utf-8 -*-
from django.db import models
from shared.models.core.db_helper import ExecHelper, sql_safe

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

"""
DAL
"""
def get_options(db, key_stage_id):

    helper = ExecHelper()

    str_select = "SELECT id, name FROM sow_year WHERE key_stage_id = {key_stage_id};".format(key_stage_id=int(key_stage_id))
    rows = []
    rows = helper.execSql(db, str_select, rows)

    data = []

    for row in rows:
        model = YearModel(row[0], row[1])
        data.append(model)

    return data
