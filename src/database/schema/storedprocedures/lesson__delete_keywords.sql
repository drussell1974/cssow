DELIMITER //

DROP PROCEDURE IF EXISTS lesson__delete_keywords;

CREATE PROCEDURE lesson__delete_keywords (
 IN p_lesson_id INT,
 IN p_auth_user INT)
BEGIN
    DELETE FROM sow_lesson__has__key_words 
    WHERE lesson_id = p_lesson_id;
END;
//

DELIMITER ;