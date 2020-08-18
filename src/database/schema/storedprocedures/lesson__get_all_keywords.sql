DELIMITER //

DROP PROCEDURE IF EXISTS lesson__get_all_keywords;

CREATE PROCEDURE lesson__get_all_keywords (
 IN p_lesson_id INT,
 IN p_auth_user INT)
BEGIN
      SELECT 
            kw.id as id, 
            name as term, 
            definition as definition 
      FROM sow_lesson__has__key_words as lkw 
            INNER JOIN sow_key_word kw ON kw.id = lkw.key_word_id 
      WHERE 
            lkw.lesson_id = p_lesson_id AND published = 1;
END;

//

DELIMITER ;