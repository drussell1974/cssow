DELIMITER //

DROP PROCEDURE IF EXISTS keyword__delete;

CREATE PROCEDURE keyword__delete (
 IN p_keyword_id INT,
 IN p_scheme_of_work_id INT,
 IN p_auth_user INT)
BEGIN
    INSERT INTO sow_key_word__archive (id, name, definition, scheme_of_work_id)
    SELECT id, name, definition, scheme_of_work_id
    FROM sow_key_word
    WHERE id = p_keyword_id and scheme_of_work_id = p_scheme_of_work_id;

    INSERT INTO sow_lesson__has__key_words__archive (key_word_id, lesson_id)
    SELECT lkw.key_word_id, lkw.lesson_id
    FROM sow_key_word kw 
        INNER JOIN sow_lesson__has__key_words lkw ON lkw.key_word_id = kw.id
        WHERE kw.id = p_keyword_id and kw.scheme_of_work_id = p_scheme_of_work_id;

    DELETE FROM sow_key_word
    -- UPDATE sow_key_word
    -- SET published = 64
    WHERE id = p_keyword_id and scheme_of_work_id = p_scheme_of_work_id
        AND p_auth_user IN (SELECT auth_user_id 
                            FROM sow_teacher 
                            WHERE auth_user_id = p_auth_user AND scheme_of_work_id = p_scheme_of_work_id);
END;
//

DELIMITER ;