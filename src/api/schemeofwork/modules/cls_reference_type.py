# -*- coding: utf-8 -*-

def get_options(db):

    rows = db.executesql("SELECT id, name FROM sow_reference_type;")

    data = [];

    for row in rows:
        model = dict(id=row[0], name=row[1])
        data.append(model)

    return data
