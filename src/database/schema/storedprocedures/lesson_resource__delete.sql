DELIMITER //

DROP PROCEDURE IF EXISTS lesson_resource__delete;

CREATE PROCEDURE lesson_resource__delete (
 IN p_resource_id INT,
 IN p_auth_user INT)
BEGIN
  DELETE FROM sow_resource WHERE id = p_resource_id AND published IN (32,64);
END;
//

DELIMITER ;