DELIMITER //

DROP PROCEDURE IF EXISTS keyword__delete;

CREATE PROCEDURE keyword__delete (
 IN p_keyword_id INT,
 IN p_lesson_id INT,
 IN p_scheme_of_work_id INT,	
 IN p_auth_user INT)
BEGIN

	IF p_lesson_id > 0 THEN
		DELETE FROM sow_lesson__has__key_words
		WHERE lesson_id = p_lesson_id and key_word_id = p_keyword_id;
    ELSE
		DELETE FROM sow_key_word
		-- UPDATE sow_key_word
		-- SET published = 64	
		WHERE id = p_keyword_id and scheme_of_work_id = p_scheme_of_work_id
			AND p_auth_user IN (SELECT auth_user_id 
								FROM sow_teacher 
								WHERE auth_user_id = p_auth_user AND scheme_of_work_id = p_scheme_of_work_id);
	END IF;
END;
//

DELIMITER ;