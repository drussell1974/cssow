# -*- coding: utf-8 -*-
from shared.models.core.db_helper import ExecHelper
from shared.models.core.basemodel import BaseModel


def get_options(db):
    execHelper = ExecHelper()
    
    raise DeprecationWarning("No longer used.")

    rows = []
    #TODO: #271 Stored procedure (get_options)
    rows = execHelper.execSql(db, "SELECT id, name FROM sow_reference_type;", rows)

    data = []

    for row in rows:
        model = dict(id=row[0], name=row[1])
        data.append(model)

    return data
