DELIMITER //

DROP PROCEDURE IF EXISTS scheme_of_work__delete;

CREATE PROCEDURE scheme_of_work__delete (
    IN scheme_of_work_id INT,
    IN p_auth_user INT)
BEGIN
    -- CHECK sow_teacher
    DELETE sow_scheme_of_work 
    FROM sow_scheme_of_work 
    WHERE id = scheme_of_work_id
        AND p_auth_user IN (SELECT auth_user_id 
                            FROM sow_teacher 
                            WHERE auth_user_id = p_auth_user AND scheme_of_work_id = scheme_of_work_id);
END;
//

DELIMITER ;

