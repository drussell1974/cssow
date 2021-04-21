DELIMITER //

DROP PROCEDURE IF EXISTS topic__delete_unpublished;

CREATE PROCEDURE topic__delete_unpublished (
 IN p_department_id INT,
 IN p_auth_user INT)
BEGIN
    DELETE FROM sow_topic
    WHERE 
		department_id = p_department_id
		AND published IN (32, 64);
END;
//

DELIMITER ;