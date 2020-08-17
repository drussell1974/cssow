# tables
mysql -u $1 -p$2 -h $3 $4 < tables/sow_scheme_of_work__has__teacher.sql
mysql -u $1 -p$2 -h $3 $4 < tables/alter_table__sow_learning_objective__has__lesson.sql
mysql -u $1 -p$2 -h $3 $4 < tables/alter_table__sow_lesson.sql

# views
mysql -u $1 -p$2 -h $3 $4 < views/sow_teacher.sql

echo lesson__get
mysql -u $1 -p$2 -h $3 $4 < storedprocedures/lesson__get.sql

echo lesson__get_all
mysql -u $1 -p$2 -h $3 $4 < storedprocedures/lesson__get_all.sql

echo lesson__update
mysql -u $1 -p$2 -h $3 $4 < storedprocedures/lesson__update.sql

echo lesson__insert
mysql -u $1 -p$2 -h $3 $4 < storedprocedures/lesson__insert.sql

echo lesson__delete
mysql -u $1 -p$2 -h $3 $4 < storedprocedures/lesson__delete.sql

echo lesson__get_number_of_learning_objectives
mysql -u $1 -p$2 -h $3 $4 < storedprocedures/lesson__get_number_of_learning_objectives.sql

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

echo lesson_resource__publish_item
mysql -u $1 -p$2 -h $3 $4 < storedprocedures/lesson_resource__publish_item.sql

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

echo scheme_of_work__has__teacher__insert
mysql -u $1 -p$2 -h $3 $4 < storedprocedures/scheme_of_work__has__teacher__insert.sql