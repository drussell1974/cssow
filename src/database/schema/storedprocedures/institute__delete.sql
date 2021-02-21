DELIMITER //

DROP PROCEDURE IF EXISTS institute__delete;

CREATE PROCEDURE institute__delete (
 OUT p_institute_id INT,
 IN p_auth_user INT)
BEGIN
    DELETE FROM sow_institute
    WHERE id = p_institute_id and head_id = p_auth_user;
END;
//

DELIMITER ;