DELIMITER //

DROP PROCEDURE IF EXISTS scheme_of_work__delete_unpublished;

CREATE PROCEDURE scheme_of_work__delete_unpublished (
    IN p_published INT,
    IN p_auth_user INT)
BEGIN
    -- CHECK sow_teacher
    DELETE sow_scheme_of_work 
    FROM sow_scheme_of_work 
    WHERE published = p_published
        AND (created_by = p_auth_user 
			or p_auth_user IN (SELECT auth_user_id 
								FROM sow_teacher 
								WHERE auth_user_id = p_auth_user AND scheme_of_work_id = sow_scheme_of_work.id)
			);
END;
//

DELIMITER ;