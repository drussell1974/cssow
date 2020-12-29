DELIMITER //

DROP PROCEDURE IF EXISTS keyword__merge_duplicate;

CREATE PROCEDURE keyword__merge_duplicate (
 IN p_key_word_id INT,
 IN p_scheme_of_work_id INT,
 IN p_auth_user INT)
BEGIN
	SELECT * FROM sow_key_word 
	WHERE name IN (
		SELECT name FROM sow_key_word 
		WHERE id = p_key_word_id and scheme_of_work_id = p_scheme_of_work_id)
	and scheme_of_work_id = p_scheme_of_work_id;

	-- INSERT INTO sow_lesson__has__key_words (key_word_id, lesson_id)
	SELECT p_key_word_id as key_word_id, lesson_id
    FROM sow_lesson__has__key_words WHERE key_word_id IN (
		SELECT id FROM sow_key_word 
		WHERE name IN (
					SELECT name FROM sow_key_word 
					WHERE id = p_key_word_id and scheme_of_work_id = p_scheme_of_work_id)
				and scheme_of_work_id = p_scheme_of_work_id
	);

	-- DELETE FROM sow_key_word 
	SELECT * FROM sow_key_word 
	WHERE name IN (
				SELECT name FROM sow_key_word
				 WHERE id = p_key_word_id and scheme_of_work_id = p_scheme_of_work_id) 
 		and id != p_key_word_id and scheme_of_work_id = p_scheme_of_work_id;
END;
//

DELIMITER ;
