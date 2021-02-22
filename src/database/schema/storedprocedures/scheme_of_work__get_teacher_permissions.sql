DELIMITER //

DROP PROCEDURE IF EXISTS scheme_of_work__get_teacher_permissions;

CREATE PROCEDURE scheme_of_work__get_teacher_permissions (
 IN p_teacher_id INT,
 IN p_department_id INT,
 IN p_institute_id INT,
 IN p_is_authorised BIT,
 IN p_auth_user INT)
BEGIN
    SELECT 
		teacher_id as teacher_id,
		teacher_name as teacher_name,
		scheme_of_work_id as scheme_of_work_id,
        scheme_of_work_name as scheme_of_work_name,
        department_id as department_id,
        department_name as department_name,
		institute_id as institute_id,	
        institute_name as institute_name,
		scheme_of_work_permission as scheme_of_work_permission, 
        lesson_permission as lesson_permission,
        department_permission as department_permission,
		is_authorised as is_authorised
    FROM sow_permission
    WHERE department_id = p_department_id
		and institute_id = p_institute_id
        and teacher_id = p_teacher_id
        and is_authorised = p_is_authorised;
END;
//

DELIMITER ;

-- CALL scheme_of_work__get_team_permissions(2, 5, 2, True, 2);
-- CALL scheme_of_work__get_teacher_permissions(2, 5, 2, True, 2);
