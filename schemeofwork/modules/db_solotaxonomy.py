# -*- coding: utf-8 -*-
"""from gluon.contrib.appconfig import AppConfig
configuration = AppConfig(reload=True)
db = DAL(configuration.get('db.uri'),
     pool_size=configuration.get('db.pool_size'),
     migrate_enabled=configuration.get('db.migrate'),
     check_reserved=['all'])
"""

from cls_solotaxonomy import SoloTaxonomyModel

def get_options(db):

    rows = db.executesql("SELECT id, name, lvl FROM sow_solo_taxonomy;")

    data = [];

    for row in rows:
        model = SoloTaxonomyModel(row[0], row[1], row[2])
        data.append(model)

    return data
