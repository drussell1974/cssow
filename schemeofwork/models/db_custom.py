# -*- coding: utf-8 -*-
from gluon.custom_import import track_changes; track_changes(True)


# -------------------------------------------------------------------------
# Define your tables below (or better in another model file) for example
#
# >>> db.define_table('mytable', Field('myfield', 'string'))
#
# Fields can be 'string','text','password','integer','double','boolean'
#       'date','time','datetime','blob','upload', 'reference TABLENAME'
# There is an implicit 'id integer autoincrement' field
# Consult manual for more options, validators, etc.
#
# More API examples for controllers:
#
# >>> db.mytable.insert(myfield='value')
# >>> rows = db(db.mytable.myfield == 'value').select(db.mytable.ALL)
# >>> for row in rows: print row.id, row.myfield
# -------------------------------------------------------------------------

# sow_content

db.define_table("sow_content",
                Field("description", "string", length=500, notnull=True),
                Field("letter", "string", length=1, notnull=True),
                Field("key_stage_id", "integer", notnull=True),
                Field("created", "datetime", notnull=True, default="0000-00-00 00:00:00"),
                Field("created_by", "integer", notnull=True, default=1),
                Field("published", "integer", notnull=True, default=1),
                migrate = False
               )

# sow_cs_concept

db.define_table("sow_cs_concept",
                Field("name", "string", length=20, notnull=True),
                Field("abbr", "string", length=2, notnull=True),
                Field("created", "datetime", notnull=True, default="0000-00-00 00:00:00"),
                Field("created_by", "integer", notnull=True, default=1),
                Field("published", "integer", notnull=True, default=1),
                migrate = False
               )

# sow_exam_board

db.define_table("sow_exam_board",
                Field("name", "string", length=15, notnull=True),
                Field("created", "datetime", notnull=True, default="0000-00-00 00:00:00"),
                Field("created_by", "integer", notnull=True, default=1),
                Field("published", "integer", notnull=True, default=1),
                migrate = False
               )


# sow_key_stage

db.define_table("sow_key_stage",
                Field("name", "string", length=3, notnull=True),
                Field("created", "datetime", notnull=True, default="0000-00-00 00:00:00"),
                Field("created_by", "integer", notnull=True, default=1),
                Field("published", "integer", notnull=True, default=1),
                migrate = False
               )

# sow_key_word

db.define_table("sow_key_word",
                Field("name", "string", length=100, notnull=True),
                Field("definition", "text", notnull=False),
                Field("created", "datetime", notnull=True, default="0000-00-00 00:00:00"),
                Field("created_by", "integer", notnull=True, default=1),
                Field("published", "integer", notnull=True, default=1),
                migrate = False
               )

# sow_ks123_pathway

db.define_table("sow_ks123_pathway",
                Field("objective", "string", length=1000, notnull=True),
                Field("year_id", "integer", notnull=True),
                Field("topic_id", "integer", notnull=True),
                Field("subject_purpose_id", "integer", notnull=True),
                Field("Abstraction", "string", length=5, notnull=False),
                Field("Decomposition", "string", length=5, notnull=False),
                Field("AlgorithmicThinking", "string", length=5, notnull=False),
                Field("Evaluation", "string", length=5, notnull=False),
                Field("Generalisation", "string", length=5, notnull=False),
                Field("created", "datetime", notnull=True, default="0000-00-00 00:00:00"),
                Field("created_by", "integer", notnull=True, default=1),
                Field("published", "integer", notnull=True, default=1),
                migrate = False
                )

# sow_learning_episode

db.define_table("sow_learning_episode",
                Field("title", "string", length=45, notnull=True, default=""),
                Field("order_of_delivery_id", "integer", notnull=False, default=None),
                Field("scheme_of_work_id", "integer", notnull=False, default=None),
                Field("topic_id", "integer", notnull=False, default="76"),
                Field("related_topic_ids", "string", length=100, default=""),
                Field("summary", "string", length=100, default=""),
                Field("key_words", "string",length=1000, default=""),
                Field("created", "datetime", notnull=True, default="0000-00-00 00:00:00"),
                Field("created_by", "integer", notnull=True, default=1),
                Field("published", "integer", notnull=True, default=1),
                migrate = False
                )

# sow_learning_episode__has__ks123_pathway

db.define_table("sow_learning_episode__has__ks123_pathway",
                Field("learning_episode_id", "integer", notnull=True),
                Field("ks123_pathway_id", "integer", notnull=True)
                )

# sow_learning_episode__has__pathway

db.define_table("sow_learning_episode__has__pathway",
                Field("learning_episode_id", "integer", notnull=False, default=None),
                Field("learning_episode_id", "integer", notnull=False, default=None),
                migrate = False
                )

# sow_learning_episode__has__references

db.define_table("sow_learning_episode__has__references",
                Field("reference_id", "integer",notnull=True),
                Field("learning_episode_id", "integer", notnull=True),
                Field("page_notes", length=250, notnull=False, default=None),
                Field("page_url", length=2083, notnull=False, default=""),
                Field("task_icon", length=80, notnull=False, default=""),
                migrate = False
                )

# sow_learning_episode__has__topics

db.define_table("sow_learning_episode__has__topics",
                Field("learning_episode_id", "integer", notnull=True),
                Field("topic_id", "integer", notnull=True),
                migrate = False
                )
"""
# sow_learning_episode_references

db.define_table("sow_learning_episode_references",
                Field("reference_id", "integer",notnull=True),
                Field("learning_episode_id", "integer", notnull=True),
                Field("pages", length=30, notnull=False, default=None),
                Field("url", length=2083, notnull=False, default=""),
                migrate = False
                )
"""

# sow_learning_objective

db.define_table("sow_learning_objective",
                Field("description", "string", length=1000, notnull=True),
                Field("notes", "string", length=4000, notnull=False, default=""),
                Field("key_words", "string", length=4000, notnull=False, default=""),
                Field("solo_taxonomy_id", "integer", notnull=False, default=None),
                Field("topic_id", "integer", notnull=False, default=None),
                Field("content_id", "integer", notnull=False, default=None),
                Field("exam_board_id", "integer", notnull=False, default=None),
                Field("parent_id", "integer", notnull=False, default=None),
                Field("group_name", "string", length=15, notnull=False, default=None),
                Field("created", "datetime", notnull=True, default="0000-00-00 00:00:00"),
                Field("created_by", "integer", notnull=True, default=1),
                Field("published", "integer", notnull=True, default=1),
                migrate = False
                )

# sow_learning_objective__has__learning_episode

db.define_table("sow_learning_objective__has__learning_episode",
                Field("learning_objective_id", "integer", notnull=False, default=None),
                Field("learning_episode_id", "integer", notnull=False, default=None),
                migrate = False
                )

# sow_logging

db.define_table("sow_logging",
                Field("details", "text"),
                Field("created", "datetime", notnull=True, default="0000-00-00 00:00:00"),
                migrate = False
                )

# sow_play_based

db.define_table("sow_play_based",
                Field("name", "string", length=100, notnull=True),
                Field("created", "datetime", notnull=True, default="0000-00-00 00:00:00"),
                Field("created_by", "integer", notnull=True, default=1),
                Field("published", "integer", notnull=True, default=1),
                migrate = False
               )

# sow_reference

db.define_table("sow_reference",
                Field("reference_type_id", "integer", notnull=True),
                Field("title", "string", length=300, notnull=True),
                Field("authors", "string", length=200, notnull=False, default=""),
                Field("publisher", "string", length=70, notnull=True),
                Field("year_published", "integer", notnull=True),
                Field("url", "string", length=2083, notnull=False, default=""),
                Field("last_accessed", "datetime", notnull=False, default="0000-00-00 00:00:00"),
                Field("scheme_of_work_id", "integer", notnull=True),
                Field("created", "datetime", notnull=True, default="0000-00-00 00:00:00"),
                Field("created_by", "integer", notnull=True, default=1),
                Field("published", "integer", notnull=True, default=1),
                migrate = False
               )

# sow_reference_type

db.define_table("sow_reference_type",
                Field("name", "string", length=15, notnull=True),
                Field("created", "datetime", notnull=True, default="0000-00-00 00:00:00"),
                Field("created_by", "integer", notnull=True, default=1),
                Field("published", "integer", notnull=True, default=1),
                migrate = False
               )

# sow_scheme_of_work

db.define_table("sow_scheme_of_work",
                Field("name", "string", length=40, notnull=True),
                Field("description", "text"),
                Field("key_stage_id", "integer", notnull=True),
                Field("exam_board_id", "integer", notnull=False, default=None),
                Field("created", "datetime", notnull=True, default="0000-00-00 00:00:00"),
                Field("created_by", "integer", notnull=True, default=1),
                Field("published", "integer", notnull=True, default=1),
                migrate = False
               )

# sow_solo_taxonomy

db.define_table("sow_solo_taxonomy",
                Field("name", "string", length=100, notnull=True),
                Field("lvl", "string", length=1, notnull=True, default="A"),
                Field("created", "datetime", notnull=True, default="0000-00-00 00:00:00"),
                Field("created_by", "integer", notnull=True, default=1),
                Field("published", "integer", notnull=True, default=1),
                migrate = False
               )

# sow_subject_purpose

db.define_table("sow_subject_purpose",
                Field("name", "string", length=20, notnull=True),
                Field("created", "datetime", notnull=True, default="0000-00-00 00:00:00"),
                Field("created_by", "integer", notnull=True, default=1),
                Field("published", "integer", notnull=True, default=1),
                migrate = False
               )


# sow_topic

db.define_table("sow_topic",
                Field("name", "string", length=20, notnull=True),
                Field("parent_id", "integer", notnull=False, default=None),
                Field("lvl", "integer", notnull=False, default=None),
                Field("created", "datetime", notnull=True, default="0000-00-00 00:00:00"),
                Field("created_by", "integer", notnull=True, default=1),
                Field("published", "integer", notnull=True, default=1),
                migrate = False
               )

# sow_year

db.define_table("sow_year",
                Field("name", "string", length=20, notnull=True),
                Field("key_stage_id", "integer", notnull=True),
                Field("created", "datetime", notnull=True, default="0000-00-00 00:00:00"),
                Field("created_by", "integer", notnull=True, default=1),
                Field("published", "integer", notnull=True, default=1),
                migrate = False
               )

#
#
# -------------------------------------------------------------------------
# after defining tables, uncomment below to enable auditing
# -------------------------------------------------------------------------
# auth.enable_record_versioning(db)
