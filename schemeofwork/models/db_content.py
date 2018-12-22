# -*- coding: utf-8 -*-
from gluon.contrib.appconfig import AppConfig
configuration = AppConfig(reload=True)
db = DAL(configuration.get('db.uri'),
     pool_size=configuration.get('db.pool_size'),
     migrate_enabled=configuration.get('db.migrate'),
     check_reserved=['all'])

from cls_content import ContentModel

def get_options(key_stage_id):

    rows = db.executesql("SELECT id, description FROM sow_content WHERE key_stage_id = {};".format(key_stage_id))

    data = [];

    for row in rows:
        model = ContentModel(row[0], row[1])
        data.append(model)

    return data
