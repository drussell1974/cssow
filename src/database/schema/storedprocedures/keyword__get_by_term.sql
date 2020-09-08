DELIMITER //

DROP PROCEDURE IF EXISTS keyword__get_by_term;
/*
CREATE PROCEDURE keyword__get_by_term (
 IN p_search VARCHAR(100),
 IN p_scheme_of_work_id INT,
 IN p_auth_user INT)

BEGIN
    SELECT 
        kw.id as id,
        kw.name as term, 
        kw.definition as definition,
        kw.scheme_of_work_id as p_scheme_of_work_id,
        kw.published as published
    FROM 
        sow_key_word kw 
    WHERE 
        name = p_search 
            AND (published = 1 
                  or p_auth_user IN (SELECT auth_user_id 
                                FROM sow_teacher 
                                WHERE auth_user_id = p_auth_user AND scheme_of_work_id = kw.scheme_of_work_id))
    ORDER BY kw.name;
END;*/
//

DELIMITER ;