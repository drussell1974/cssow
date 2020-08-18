DELIMITER //

DROP PROCEDURE IF EXISTS lesson__insert_keywords;

CREATE PROCEDURE lesson__insert_keywords (
 IN p_lesson_id INT,
 IN p_keyword_id INT,
 IN p_auth_user INT)
BEGIN
    DECLARE record_exists INT DEFAULT 0;

    SET record_exists = (SELECT count(*) FROM sow_lesson__has__key_words WHERE lesson_id = p_lesson_id AND key_word_id = p_keyword_id);

    IF record_exists = 0 THEN
        INSERT INTO sow_lesson__has__key_words 
            (lesson_id, key_word_id)
        VALUES
            (p_lesson_id, p_keyword_id);
    END IF;
END;
//

DELIMITER ;