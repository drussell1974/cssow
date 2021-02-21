DELIMITER //

DROP PROCEDURE IF EXISTS scheme_of_work__has__teacher_permission__update;

CREATE PROCEDURE scheme_of_work__has__teacher_permission__update (
 IN p_scheme_of_work_id INT,
 IN p_teacher_id INT,
 IN p_department_permission INT,
 IN p_scheme_of_work_permission INT,
 IN p_lesson_permission INT, 
 IN p_auth_user INT,
 IN p_is_authorised BOOLEAN
 )
BEGIN
	-- DO NOT UPDATE ESSENTIAL USERS
	UPDATE sow_scheme_of_work__has__teacher 
	SET
		department_permission = p_department_permission,
		scheme_of_work_permission = p_scheme_of_work_permission,
		lesson_permission = p_lesson_permission,
		modified_by = p_auth_user,
        is_authorised = p_is_authorised
	WHERE
		scheme_of_work_id = p_scheme_of_work_id and
		auth_user_id = p_teacher_id;
END;
//

#CALL scheme_of_work__has__teacher_permission__update(11, 113, 1, 1, 1, 2, True);

DELIMITER ;