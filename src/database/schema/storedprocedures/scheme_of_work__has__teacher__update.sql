DELIMITER //

DROP PROCEDURE IF EXISTS scheme_of_work__has__teacher_permission__update;

CREATE PROCEDURE scheme_of_work__has__teacher_permission__update (
 IN p_scheme_of_work_id INT,
 IN p_teacher_id INT,
 IN p_department_permission INT,
 IN p_scheme_of_work_permission INT,
 IN p_lesson_permission INT, 
 IN p_auth_user INT -- The user executing the sp
 )
BEGIN
    UPDATE sow_scheme_of_work__has__teacher 
	SET
		department_permission = p_department_permission,
        scheme_of_work_permission = p_scheme_of_work_permission,
        lesson_permission = p_lesson_permission
    WHERE
		scheme_of_work_id = p_scheme_of_work_id AND
		auth_user_id = p_teacher_id;  -- assumes the auth_user (TODO: change column name to teacher_id)
END;
//

DELIMITER ;