SELECT * FROM drussell1974$cssow_api.auth_user;

SET @user_id = 168;

SELECT * FROM sow_academic_year WHERE created_by = @user_id;
SELECT * FROM sow_academic_year_period WHERE created_by = @user_id;
SELECT * FROM sow_content WHERE created_by = @user_id;
SELECT * FROM sow_department WHERE created_by = @user_id;
SELECT * FROM sow_department__has__teacher WHERE created_by = @user_id;
SELECT * FROM sow_institute WHERE created_by = @user_id;
SELECT * FROM sow_key_stage WHERE created_by = @user_id;
SELECT * FROM sow_key_word WHERE created_by = @user_id;
SELECT * FROM sow_ks123_pathway WHERE created_by = @user_id;
SELECT * FROM sow_learning_objective WHERE created_by = @user_id;
SELECT * FROM sow_lesson WHERE created_by = @user_id;
SELECT * FROM sow_lesson_plan WHERE created_by = @user_id;
SELECT * FROM sow_lesson_schedule WHERE created_by = @user_id;
SELECT * FROM sow_logging_notification WHERE user_id = @user_id;
SELECT * FROM sow_resource WHERE created_by = @user_id;
SELECT * FROM sow_scheme_of_work WHERE created_by = @user_id;
SELECT * FROM sow_scheme_of_work__has__teacher WHERE created_by = @user_id;
SELECT * FROM sow_topic WHERE created_by = @user_id;
SELECT * FROM sow_year WHERE created_by = @user_id;