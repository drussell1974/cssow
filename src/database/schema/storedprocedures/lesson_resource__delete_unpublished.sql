DELIMITER //

DROP PROCEDURE IF EXISTS lesson_resource__delete_unpublished;

CREATE PROCEDURE lesson_resource__delete_unpublished (
 IN p_lesson_id INT,
 IN p_auth_user INT)
BEGIN
  DELETE FROM sow_resource 
  WHERE lesson_id = p_lesson_id
    AND published IN (32,64);
END;
//

DELIMITER ;