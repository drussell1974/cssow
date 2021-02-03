DELIMITER //

DROP PROCEDURE IF EXISTS keyword__publish;

CREATE PROCEDURE keyword__publish (
 IN p_keyword_id INT,
 IN p_published INT,
 IN p_auth_user INT)
BEGIN

    UPDATE sow_key_word	
    SET 
        published = p_published
    WHERE 
        id =  p_keyword_id 
            AND p_auth_user 
                IN (SELECT auth_user_id 
                    FROM sow_teacher 
                    WHERE auth_user_id = p_auth_user AND scheme_of_work_id = scheme_of_work_id);
END;
//

DELIMITER ;