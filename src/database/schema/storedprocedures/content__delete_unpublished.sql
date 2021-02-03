DELIMITER //

DROP PROCEDURE IF EXISTS content__delete_unpublished;

CREATE PROCEDURE content__delete_unpublished (
 IN p_scheme_of_work_id INT,
 IN p_auth_user INT)
BEGIN
    DELETE FROM sow_content
    WHERE scheme_of_work_id = p_scheme_of_work_id 
            AND published IN (0,2) 
            AND p_auth_user IN 
                    (SELECT auth_user_id 
                    FROM sow_teacher 
                    WHERE scheme_of_work_id = p_scheme_of_work_id);
END;
//

DELIMITER ;