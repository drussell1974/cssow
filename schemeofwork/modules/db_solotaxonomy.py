# -*- coding: utf-8 -*-
from cls_solotaxonomy import SoloTaxonomyModel

def get_options(db):

    rows = db.executesql("SELECT id, name, lvl FROM sow_solo_taxonomy;")

    data = [];

    for row in rows:
        model = SoloTaxonomyModel(row[0], row[1], row[2])
        data.append(model)

    return data
