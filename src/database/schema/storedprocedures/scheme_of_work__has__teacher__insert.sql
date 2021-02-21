DELIMITER //

DROP PROCEDURE IF EXISTS scheme_of_work__has__teacher_permission__insert;

CREATE PROCEDURE scheme_of_work__has__teacher_permission__insert (
 IN p_scheme_of_work_id INT,
 IN p_teacher_id INT,
 IN p_department_permission INT,
 IN p_scheme_of_work_permission INT,
 IN p_lesson_permission INT, 
 IN p_auth_user INT,
 IN p_is_authorised BOOLEAN
 )
BEGIN
	INSERT IGNORE INTO sow_scheme_of_work__has__teacher 
	(
		scheme_of_work_id,
		auth_user_id, -- assumes the auth_user (TODO: change column name to teacher_id)
		department_permission,
		scheme_of_work_permission,
		lesson_permission,
        is_authorised,
        created_by
	)
	VALUES 
	(
		p_scheme_of_work_id,
		p_teacher_id,
		p_department_permission,
		p_scheme_of_work_permission,
		p_lesson_permission,
        p_is_authorised,
        p_auth_user
	);
END;
//

DELIMITER ;
