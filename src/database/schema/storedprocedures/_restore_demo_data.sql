
DELIMITER //
DROP PROCEDURE IF EXISTS demo_restoredata;

CREATE PROCEDURE demo_restoredata (
 IN p_auth_user_id INT,
 IN p_institute_id INT,
 IN p_department_id INT,
 IN p_scheme_of_work_id INT,
 IN p_content_id INT,
 IN p_lesson_id INT,
 IN p_learning_objective_id INT,
 IN p_resource_id INT,
 IN p_keyword_id INT)
BEGIN
	-- RESTORE INSTITUTE
    -- RESTORE DEPARTMENT
	-- RESTORE SCHEME OF WORK
	-- RESTORE LESSON
    
    -- RESTORE KEYWORD
	IF (SELECT count(*) FROM `sow_key_word` WHERE id = p_keyword_id) = 0 THEN
		INSERT INTO `sow_key_word` (`id`, `name`, `definition`, `scheme_of_work_id`, `created_by`, `published`) 
		VALUES (p_keyword_id, 'Random Access Memory (RAM)', '', p_scheme_of_work_id, p_auth_user_id, '1');
	END IF;
	SELECT * FROM `sow_key_word` WHERE id = p_keyword_id;
    
    -- RESTORE LESSON KEYWORD
    IF (SELECT count(*) FROM `sow_lesson__has__key_words` WHERE key_word_id = p_keyword_id and lesson_id = p_lesson_id) = 0 THEN
		INSERT INTO `sow_lesson__has__key_words` (`key_word_id`, `lesson_id`) 
        VALUES (p_keyword_id, p_lesson_id);
	END IF;
    SELECT * FROM `sow_lesson__has__key_words` WHERE key_word_id = p_keyword_id and lesson_id = p_lesson_id;
    
    -- RESTORE RESOURCE
    
END;
//
/*
DELIMITER ;
SET @DEMO_USER_ID=2;
SET @DEMO_INSTITUTE_ID=2;
SET @DEMO_DEPARTMENT_ID=5;
SET @DEMO_SCHEME_OF_WORK_ID=11;
SET @DEMO_CONTENT_ID=192;
SET @DEMO_LESSON_ID=220;
SET @DEMO_LEARNING_OBJECTIVE_ID=410;
SET @DEMO_RESOURCE_ID=983;
SET @DEMO_KEYWORD_ID=92;

CALL demo_restoredata(
	@DEMO_USER_ID,
	@DEMO_INSTITUTE_ID, 
	@DEMO_DEPARTMENT_ID, 
    @DEMO_SCHEME_OF_WORK_ID, 
    @DEMO_CONTENT_ID,
    @DEMO_LESSON_ID, 
    @DEMO_LEARNING_OBJECTIVE_ID,
    @DEMO_RESOURCE_ID, 
    @DEMO_KEYWORD_ID);
*/