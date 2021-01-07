DELIMITER //

DROP PROCEDURE IF EXISTS scheme_of_work__get_teacher_permissions;

CREATE PROCEDURE scheme_of_work__get_teacher_permissions (
 IN p_scheme_of_work_id INT,
 IN p_auth_user INT)
BEGIN
	SELECT scheme_of_work_permission, lesson_permission 
    FROM sow_teacher 
    WHERE scheme_of_work_id = p_scheme_of_work_id LIMIT 1;
END;
//

DELIMITER ;