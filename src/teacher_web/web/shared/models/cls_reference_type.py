# -*- coding: utf-8 -*-
from shared.models.core.db_helper import ExecHelper

def get_options(db):
    execHelper = ExecHelper()

    rows = []
    rows = execHelper.execSql(db, "SELECT id, name FROM sow_reference_type;", rows)

    data = []

    for row in rows:
        model = dict(id=row[0], name=row[1])
        data.append(model)

    return data
