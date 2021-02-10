DELIMITER //

DROP PROCEDURE IF EXISTS scheme_of_work__get_teacher_permissions;

CREATE PROCEDURE scheme_of_work__get_teacher_permissions (
 IN p_scheme_of_work_id INT,
 IN p_teacher_id INT,
 IN p_department_id INT,
 IN p_institute_id INT,
 IN p_auth_user INT)
BEGIN
    SELECT 
      IFNULL(IFNULL(teach_sow.scheme_of_work_permission, teach_dep.scheme_of_work_permission), 7) as scheme_of_work_permission, 
      IFNULL(IFNULL(teach_sow.lesson_permission, teach_dep.lesson_permission), 7) as lesson_permission, 
      IFNULL(IFNULL(teach_sow.department_permission, teach_dep.department_permission), 7) as department_permission,
      user.first_name as teacher_name,  
      -- authorise based on scheme_of_work__has__teacher relationship,
      -- if this does not exist yet, then is_authorised is true, if 
      -- the teacher is the head of the department
      IFNULL(teach_sow.is_authorised, dep.head_id = p_teacher_id) as is_authorised
    FROM auth_user as user    
    INNER JOIN sow_department as dep
    LEFT JOIN sow_department__has__teacher as teach_dep 
		ON teach_dep.auth_user_id = user.id
        and (teach_dep.department_id = dep.id
			or p_scheme_of_work_id = 0)
	LEFT JOIN sow_scheme_of_work__has__teacher AS teach_sow 
		ON teach_sow.auth_user_id = user.id 
        and (teach_sow.scheme_of_work_id = p_scheme_of_work_id
			or p_scheme_of_work_id = 0)
    WHERE user.id = p_teacher_id and dep.id = p_department_id;
    
END;
//

DELIMITER ;

CALL scheme_of_work__get_teacher_permissions(0, 59, 19, 0, 59);