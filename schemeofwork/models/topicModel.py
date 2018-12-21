# -*- coding: utf-8 -*-
from datetime import datetime
from gluon.contrib.appconfig import AppConfig

configuration = AppConfig(reload=True)

db = DAL(configuration.get('db.uri'),
     pool_size=configuration.get('db.pool_size'),
     migrate_enabled=configuration.get('db.migrate'),
     check_reserved=['all'])


class ExamBoardModel:
    def __init__(this, id_, name, parent_id, parent_name):
        this.id = id_
        this.name = name
        this.parent_id = parent_id
        this.parent_name = parent_name
    id = 0
    name = ""
    parent_id = 0
    parent_name = ""


def get_options(parent_topic_id = 0):

    str_select = (" SELECT " +
                  "   top.id as id, " +
                  "   CONCAT_WS(' : ', prt_top.name, top.name) as name, " +
                  "   prt_top.id as parent_id, " +
                  "   prt_top.name as parent_name " +
                  "  FROM sow_topic as top" +
                  "  LEFT JOIN sow_topic as prt_top ON prt_top.id = top.parent_id" +
                  "  WHERE top.parent_id = %s OR %s = 0" +
                  "  ORDER BY parent_name, name;");

    rows = db.executesql(str_select, (parent_topic_id, parent_topic_id))

    data = [];

    for row in rows:
        model = ExamBoardModel(row[0], row[1], row[2], row[3])
        data.append(model)

    return data
