DELIMITER //

DROP PROCEDURE IF EXISTS scheme_of_work__has__teacher_permission__update$2;

CREATE PROCEDURE scheme_of_work__has__teacher_permission__update$2 (
 IN p_department_id INT,
 IN p_scheme_of_work_id INT,
 IN p_teacher_id INT,
 IN p_department_permission INT,
 IN p_scheme_of_work_permission INT,
 IN p_lesson_permission INT, 
 IN p_auth_user INT,
 IN p_is_authorised BOOLEAN
 )
BEGIN
	
	UPDATE sow_scheme_of_work__has__teacher as sow_teach
    INNER JOIN sow_teacher_join_code as teach_join ON teach_join.join_code = sow_teach.join_code
	SET
		sow_teach.department_permission = p_department_permission,
		sow_teach.scheme_of_work_permission = p_scheme_of_work_permission,
		sow_teach.lesson_permission = p_lesson_permission,
		sow_teach.modified_by = p_auth_user,
        teach_join.is_authorised = p_is_authorised
	WHERE
		sow_teach.scheme_of_work_id = p_scheme_of_work_id and
		teach_join.auth_user_id = p_teacher_id and teach_join.join_code = sow_teach.join_code;
	
    /* Update permission for the department */
	UPDATE sow_department__has__teacher as dep_teach
    INNER JOIN sow_teacher_join_code as teach_join ON teach_join.join_code = dep_teach.join_code
	SET
		dep_teach.department_permission = p_department_permission,
		dep_teach.modified_by = p_auth_user
	WHERE
		dep_teach.department_id = p_department_id and
		teach_join.auth_user_id = p_teacher_id and teach_join.join_code = dep_teach.join_code;
END;
//

DELIMITER ;

DELIMITER //

DROP PROCEDURE IF EXISTS scheme_of_work__has__teacher_permission__update;

CREATE PROCEDURE scheme_of_work__has__teacher_permission__update (
 IN p_department_id INT,
 IN p_scheme_of_work_id INT,
 IN p_teacher_id INT,
 IN p_department_permission INT,
 IN p_scheme_of_work_permission INT,
 IN p_lesson_permission INT, 
 IN p_auth_user INT,
 IN p_is_authorised BOOLEAN
 )
BEGIN
	
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
	
    /* Update permission for the department */
	UPDATE sow_department__has__teacher 
	SET
		department_permission = p_department_permission,
		modified_by = p_auth_user
	WHERE
		department_id = p_department_id and
		auth_user_id = p_teacher_id;
END;
//

DELIMITER ;