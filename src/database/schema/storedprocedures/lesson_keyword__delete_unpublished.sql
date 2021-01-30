DELIMITER //

DROP PROCEDURE IF EXISTS lesson_keyword__delete_unpublished;

CREATE PROCEDURE lesson_keyword__delete_unpublished (
 IN p_scheme_of_work_id INT,
 IN p_lesson_id INT,
 IN p_auth_user INT)
BEGIN
	DELETE FROM sow_lesson__has__key_words
    WHERE lesson_id = p_lesson_id 
		AND key_word_id IN (
			SELECT id FROM sow_key_word
			WHERE scheme_of_work_id = p_scheme_of_work_id 
					AND published IN (0,2) 
					AND p_auth_user IN 
							(SELECT auth_user_id 
							FROM sow_teacher 
							WHERE scheme_of_work_id = p_scheme_of_work_id)
			);
END;
//

DELIMITER ;