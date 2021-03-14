DELIMITER //

DROP PROCEDURE IF EXISTS scheme_of_work__get_team_permissions;

CREATE PROCEDURE scheme_of_work__get_team_permissions (
 IN p_head_id INT,
 IN p_department_id INT,
 IN p_institute_id INT,
 IN p_is_authorised BOOLEAN,
 IN p_auth_user INT)
BEGIN
    SELECT 
        teacher_id as teacher_id,
        teacher_name as teacher_name,
		scheme_of_work_id as scheme_of_work_id,
        scheme_of_work_name as scheme_of_work_name,
        department_id as department_id,
        department_name as department_name,
        department_permission as department_permission,
		scheme_of_work_permission as scheme_of_work_permission,
        lesson_permission as lesson_permission,
		is_authorised as is_authorised, -- the head of department is authorised
        hod_id as head_of_department_id
    FROM sow_permission
	WHERE 
		hod_id = p_head_id -- get head for department
        and is_authorised = p_is_authorised -- authorised or pending
        and department_id = p_department_id
        and institute_id = p_institute_id	
    ORDER BY scheme_of_work_id, teacher_name;
END;
//

DELIMITER ;

CALL scheme_of_work__get_team_permissions(2,5,2,True,2);