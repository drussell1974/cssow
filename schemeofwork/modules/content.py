# -*- coding: utf-8 -*-
from datetime import datetime
from gluon.contrib.appconfig import AppConfig

configuration = AppConfig(reload=True)

db = DAL(configuration.get('db.uri'),
     pool_size=configuration.get('db.pool_size'),
     migrate_enabled=configuration.get('db.migrate'),
     check_reserved=['all'])


class ContentModel:
    def __init__(this, id_, description):
        this.id = id_
        this.description = description
    id = 0
    description = ""


def get_options(db, key_stage_id):

    rows = db.executesql("SELECT id, description FROM sow_content WHERE key_stage_id = {};".format(key_stage_id))

    data = [];

    for row in rows:
        model = ContentModel(row[0], row[1])
        data.append(model)

    return data
