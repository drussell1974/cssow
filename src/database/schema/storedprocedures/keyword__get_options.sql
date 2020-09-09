DELIMITER //

DROP PROCEDURE IF EXISTS keyword__get_options;

CREATE PROCEDURE keyword__get_options (
 IN p_scheme_of_work_id INT,
 IN p_auth_user INT)
BEGIN
    SELECT 
        kw.id as id, 
        kw.name as name, 
        kw.definition as definition,
        kw.scheme_of_work_id as scheme_of_work_id,
        kw.published as published,
        count(lkw.lesson_id) as number_of_lessons
    FROM 
        sow_key_word as kw 
        LEFT JOIN sow_lesson__has__key_words as lkw ON lkw.key_word_id = kw.id
    WHERE 
        kw.scheme_of_work_id = p_scheme_of_work_id
            AND published = 1 
                  -- or p_auth_user IN (SELECT auth_user_id 
                  --                   FROM sow_teacher 
                  --                   WHERE auth_user_id = p_auth_user AND scheme_of_work_id = kw.scheme_of_work_id)
    GROUP BY id, name, definition, scheme_of_work_id, published
    ORDER BY name;
END;
//

DELIMITER ;