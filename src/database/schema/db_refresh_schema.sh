# tables
mysql -u $1 -p$2 -h $3 $4 < tables/sow_scheme_of_work__has__teacher.sql
mysql -u $1 -p$2 -h $3 $4 < tables/alter_table__sow_learning_objective__has__lesson.sql
mysql -u $1 -p$2 -h $3 $4 < tables/alter_table__sow_lesson.sql

# views
mysql -u $1 -p$2 -h $3 $4 < views/sow_teacher.sql

# stored procedures

## sow_lesson

echo lesson__copy_learning_objectives
mysql -u $1 -p$2 -h $3 $4 < storedprocedures/lesson__copy_learning_objectives.sql

echo lesson__delete
mysql -u $1 -p$2 -h $3 $4 < storedprocedures/lesson__delete.sql

echo lesson__delete_unpublished
mysql -u $1 -p$2 -h $3 $4 < storedprocedures/lesson__delete_unpublished.sql

echo lesson__get
mysql -u $1 -p$2 -h $3 $4 < storedprocedures/lesson__get.sql

echo lesson__get_all
mysql -u $1 -p$2 -h $3 $4 < storedprocedures/lesson__get_all.sql

echo lesson__get_all_keywords
mysql -u $1 -p$2 -h $3 $4 < storedprocedures/lesson__get_all_keywords.sql

echo lesson__get_ks123_pathway_objective_ids
mysql -u $1 -p$2 -h $3 $4 < storedprocedures/lesson__get_ks123_pathway_objective_ids.sql

echo lesson__get_number_of_learning_objectives
mysql -u $1 -p$2 -h $3 $4 < storedprocedures/lesson__get_number_of_learning_objectives.sql

echo lesson__get_options
mysql -u $1 -p$2 -h $3 $4 < storedprocedures/lesson__get_options.sql

echo lesson__get_pathway_objective_ids
mysql -u $1 -p$2 -h $3 $4 < storedprocedures/lesson__get_pathway_objective_ids.sql

echo lesson__get_related_topic_ids
mysql -u $1 -p$2 -h $3 $4 < storedprocedures/lesson__get_related_topic_ids.sql

echo lesson__insert
mysql -u $1 -p$2 -h $3 $4 < storedprocedures/lesson__insert.sql

echo lesson__insert_keywords
mysql -u $1 -p$2 -h $3 $4 < storedprocedures/lesson__insert_keywords.sql

echo lesson__insert_ks123pathway
mysql -u $1 -p$2 -h $3 $4 < storedprocedures/lesson__insert_ks123_pathway.sql

echo lesson__insert_pathway
mysql -u $1 -p$2 -h $3 $4 < storedprocedures/lesson__insert_pathway.sql

echo lesson__insert_related_topic
mysql -u $1 -p$2 -h $3 $4 < storedprocedures/lesson__insert_related_topic.sql

echo lesson__publish
mysql -u $1 -p$2 -h $3 $4 < storedprocedures/lesson__publish.sql

echo lesson__update
mysql -u $1 -p$2 -h $3 $4 < storedprocedures/lesson__update.sql


## sow_learning_objectives

echo lesson_learning_objective__delete
mysql -u $1 -p$2 -h $3 $4 < storedprocedures/lesson_learning_objective__delete.sql

echo lesson_learning_objective__delete_unpublished
mysql -u $1 -p$2 -h $3 $4 < storedprocedures/lesson_learning_objective__delete_unpublished.sql

echo lesson_learning_objective__get
mysql -u $1 -p$2 -h $3 $4 < storedprocedures/lesson_learning_objective__get.sql

echo lesson_learning_objective__get_all
mysql -u $1 -p$2 -h $3 $4 < storedprocedures/lesson_learning_objective__get_all.sql

echo lesson_learning_objective__insert
mysql -u $1 -p$2 -h $3 $4 < storedprocedures/lesson_learning_objective__insert.sql

echo lesson_learning_objective__update
mysql -u $1 -p$2 -h $3 $4 < storedprocedures/lesson_learning_objective__update.sql

echo lesson_learning_objective__publish_item
mysql -u $1 -p$2 -h $3 $4 < storedprocedures/lesson_learning_objective__publish_item.sql

## sow_resource

echo lesson_resource__publish_item
mysql -u $1 -p$2 -h $3 $4 < storedprocedures/lesson_resource__publish_item.sql

## sow_scheme_of_work

echo scheme_of_work__delete
mysql -u $1 -p$2 -h $3 $4 < storedprocedures/scheme_of_work__delete.sql

echo scheme_of_work__delete_unpublished
mysql -u $1 -p$2 -h $3 $4 < storedprocedures/scheme_of_work__delete_unpublished.sql

echo scheme_of_work__get
mysql -u $1 -p$2 -h $3 $4 < storedprocedures/scheme_of_work__get.sql

echo scheme_of_work__get_all
mysql -u $1 -p$2 -h $3 $4 < storedprocedures/scheme_of_work__get_all.sql

echo scheme_of_work__get_key_stage_id_only
mysql -u $1 -p$2 -h $3 $4 < storedprocedures/scheme_of_work__get_key_stage_id_only.sql

echo scheme_of_work__get_latest
mysql -u $1 -p$2 -h $3 $4 < storedprocedures/scheme_of_work__get_latest.sql

echo scheme_of_work__get_number_of_learning_objectives
mysql -u $1 -p$2 -h $3 $4 < storedprocedures/scheme_of_work__get_number_of_learning_objectives.sql

echo scheme_of_work__get_number_of_lessons
mysql -u $1 -p$2 -h $3 $4 < storedprocedures/scheme_of_work__get_number_of_lessons.sql

echo scheme_of_work__get_number_of_resources
mysql -u $1 -p$2 -h $3 $4 < storedprocedures/scheme_of_work__get_number_of_resources.sql

echo scheme_of_work__get_options
mysql -u $1 -p$2 -h $3 $4 < storedprocedures/scheme_of_work__get_options.sql

echo scheme_of_work__get_schemeofwork_name_only
mysql -u $1 -p$2 -h $3 $4 < storedprocedures/scheme_of_work__get_schemeofwork_name_only.sql

echo scheme_of_work__insert
mysql -u $1 -p$2 -h $3 $4 < storedprocedures/scheme_of_work__insert.sql

echo scheme_of_work__update
mysql -u $1 -p$2 -h $3 $4 < storedprocedures/scheme_of_work__update.sql

echo scheme_of_work__delete
mysql -u $1 -p$2 -h $3 $4 < storedprocedures/scheme_of_work__delete.sql

echo scheme_of_work__has__teacher__insert
mysql -u $1 -p$2 -h $3 $4 < storedprocedures/scheme_of_work__has__teacher__insert.sql