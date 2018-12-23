# -*- coding: utf-8 -*-

"""from gluon.contrib.appconfig import AppConfig
configuration = AppConfig(reload=True)
db = DAL(configuration.get('db.uri'),
     pool_size=configuration.get('db.pool_size'),
     migrate_enabled=configuration.get('db.migrate'),
     check_reserved=['all'])
"""
from cls_topic import TopicModel

def get_options(db, topic_id = 0, parent_topic_id = 0):

    str_select = (" SELECT " +
                  "   top.id as id, " + #0
                  "   CONCAT_WS(' : ', prt_top.name, top.name) as name, " + #1
                  "   prt_top.id as parent_id, " + #2
                  "   prt_top.name as parent_name " + #3
                  "  FROM sow_topic as top" +
                  "  LEFT JOIN sow_topic as prt_top ON prt_top.id = top.parent_id" +
                  "  WHERE %s = 0 OR top.id = %s OR top.id = %s OR prt_top.id = %s" +
                  "  ORDER BY parent_name, name;");

    rows = db.executesql(str_select, (topic_id, topic_id, parent_topic_id, parent_topic_id))

    data = [];

    for row in rows:
        model = TopicModel(row[0], row[1], row[2], row[3])
        data.append(model)

    return data
