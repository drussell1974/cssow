DELIMITER //

DROP PROCEDURE IF EXISTS lesson__get_all_keywords;

CREATE PROCEDURE lesson__get_all_keywords (
 IN p_lesson_id INT,
 IN p_auth_user INT)
BEGIN
      SELECT 
            kw.id as id, 
            kw.name as term, 
            kw.definition as definition,
            kw.scheme_of_work_id as scheme_of_work_id,
            kw.published as published
      FROM sow_lesson__has__key_words as lkw 
            INNER JOIN sow_key_word kw ON kw.id = lkw.key_word_id 
      WHERE 
            lkw.lesson_id = p_lesson_id
            AND published = 1 
                  -- or p_auth_user IN (SELECT auth_user_id 
                  --              FROM sow_teacher 
                  --              WHERE auth_user_id = p_auth_user AND scheme_of_work_id = kw.scheme_of_work_id)
      ORDER BY kw.name;
END;

//

DELIMITER ;