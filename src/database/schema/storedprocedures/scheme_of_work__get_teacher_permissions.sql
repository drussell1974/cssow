DELIMITER //

DROP PROCEDURE IF EXISTS scheme_of_work__get_teacher_permissions;

CREATE PROCEDURE scheme_of_work__get_teacher_permissions (
 IN p_scheme_of_work_id INT,
 IN p_auth_user INT)
BEGIN
	SELECT scheme_of_work_permission, lesson_permission 
    FROM sow_scheme_of_work__has__teacher 
    WHERE scheme_of_work_id = p_scheme_of_work_id 
		and auth_user_id = p_auth_user
    LIMIT 1;
END;
//

DELIMITER ;

CALL `drussell1974$cssow_api`.`scheme_of_work__get_teacher_permissions`(11, 2);
