DELIMITER //

DROP PROCEDURE IF EXISTS keyword__merge_duplicates;

CREATE PROCEDURE keyword__merge_duplicates (
 IN p_key_word_id INT,
 IN p_scheme_of_work_id INT,
 IN p_auth_user INT)
BEGIN
	DECLARE term varchar(100);
        
    SET term = (SELECT name 
				FROM sow_key_word 
				WHERE id = p_key_word_id
					and scheme_of_work_id = p_scheme_of_work_id
				LIMIT 1);                
    
    -- Create new the lesson keyword links from the keywords being deleted
    
	INSERT IGNORE INTO sow_lesson__has__key_words (key_word_id, lesson_id)
	SELECT p_key_word_id as replacement, lkw.lesson_id
    FROM sow_lesson__has__key_words as lkw 
    INNER JOIN sow_key_word as kw ON lkw.key_word_id = kw.id
	WHERE kw.name = term and kw.id != p_key_word_id and kw.scheme_of_work_id = p_scheme_of_work_id;	

	-- Mark other keywords as deleted 
	
    UPDATE sow_key_word 
	SET published = 2 -- marked for deletion
    WHERE name = term and id != p_key_word_id and scheme_of_work_id = p_scheme_of_work_id;
    
END;
//

DELIMITER ;
