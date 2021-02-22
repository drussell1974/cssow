DELIMITER //

DROP PROCEDURE IF EXISTS department__delete;

CREATE PROCEDURE department__delete (
 OUT p_department_id INT,
 IN p_auth_user INT)
BEGIN
    DELETE FROM sow_department
    WHERE id = p_department_id and head_id = p_auth_user;
END;
//

DELIMITER ;