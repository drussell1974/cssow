# -*- coding: utf-8 -*-

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
# sow_menu
db.define_table('sow_menu',
                Field('name', 'string'),
                migrate = False
               )

# sow_play_based
db.define_table('sow_play_based',
                Field('name', 'string'),
                migrate = False
               )

# sow_solo_taxonomy
db.define_table('sow_solo_taxonomy',
                Field('name', 'string'),
                Field('lvl', 'string'),
                migrate = False
               )

# sow_cs_concept
db.define_table('sow_cs_concept',
                Field('name', 'string'),
                Field('abbr', 'string'),
                migrate = False
               )

# sow_exam_board
db.define_table('sow_exam_board',
                Field('name', 'string'),
                migrate = False
               )

# sow_key_stage
db.define_table('sow_key_stage',
                Field('name', 'string'),
                migrate = False
               )


# sow_scheme_of_work
db.define_table('sow_scheme_of_work',
                Field('name', 'string'),
                Field('description', 'string'),
                Field('key_stage_id', 'reference sow_key_stage', required=True),
                Field('exam_board_id', 'reference sow_exam_board', required=True),
                Field('created', 'date'),
                Field('created_by', 'integer'),
                migrate = False
                )

# sow_content
db.define_table('sow_learning_episode',
                Field('order_of_delivery_id', 'integer'),
                Field('scheme_of_work_id', 'reference sow_scheme_of_work', required=True),
                Field('topic_id', 'reference sow_topic', required=True),
                migrate = False
               )

# sow_content
db.define_table('sow_content',
                Field('description', 'string'),
                Field('letter', 'string'),
                Field('key_stage_id', 'reference sow_key_stage'),
                migrate = False
               )


# sow_subject_purpose
db.define_table('sow_subject_purpose', 
                Field('name', 'string'),
                migrate = False
               )

# sow_topic
db.define_table('sow_topic',
                Field('name', 'string'),
                Field('parent_id', 'reference sow_topic'),
                migrate = False
               )

# sow_year
db.define_table('sow_year', 
                Field('name', 'string'),
                Field('key_stage_id', 'reference sow_key_stage'),
                migrate = False
               )


# sow_ks123_pathway
db.define_table('sow_ks123_pathway', 
                Field('objective', 'string'),
                Field('year_id', 'reference sow_year'),
                Field('topic_id', 'reference sow_topic'),
                Field('subject_purpose_id', 'reference sow_subject_purpose'),
                migrate = False
               )

# sow_learning_objective
db.define_table('sow_learning_objective', 
                Field('description', 'string'),
                Field('solo_taxonomy_id', 'reference sow_solo_taxonomy'),
                Field('topic_id', 'reference sow_topic'),
                Field('content_id', 'reference sow_content'),
                Field('exam_board_id', 'reference sow_exam_board'),
                migrate = False
               )

# sow_learning_objective__has__learning_episode
db.define_table('sow_learning_objective__has__learning_episode',
                Field('learning_objective_id', 'reference sow_learning_objective'),
                Field('learning_episode_id', 'reference sow_learning_episode'),
                migrate = False
                )

# sow_learning_objective_has_ks123_pathway
db.define_table('sow_learning_objective__has__ks123_pathway', 
                Field('description', 'string'),
                Field('learning_objective_id', 'reference sow_learning_objective'),
                Field('ks123_pathway_id', 'reference sow_ks123_pathway'),
                migrate = False
               )
# -------------------------------------------------------------------------
# after defining tables, uncomment below to enable auditing
# -------------------------------------------------------------------------
# auth.enable_record_versioning(db)
