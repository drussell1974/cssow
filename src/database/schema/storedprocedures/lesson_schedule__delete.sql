DELIMITER //

DROP PROCEDURE IF EXISTS `lesson_schedule__delete`;

CREATE PROCEDURE `lesson_schedule__delete` 
( IN p_lesson_schedule_id INT,
  IN p_auth_user INT)
BEGIN
	 DELETE FROM sow_lesson_schedule
     WHERE id = p_lesson_schedule_id;
END;
//

DELIMITER ;
