DELIMITER //

DROP PROCEDURE IF EXISTS content__delete;

CREATE PROCEDURE content__delete (
 IN p_content_id INT,
 IN p_scheme_of_work_id INT,
 IN p_auth_user INT)
BEGIN
    DELETE FROM sow_content 
    WHERE id = p_content_id 
        AND (
            published IN (0,2)
            and p_auth_user IN 
            (SELECT auth_user_id 
             FROM sow_teacher 
             WHERE scheme_of_work_id = scheme_of_work_id)
        );
END;
//

DELIMITER ;