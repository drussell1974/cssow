DELIMITER //

DROP PROCEDURE IF EXISTS scheme_of_work__get_teacher_permissions;

CREATE PROCEDURE scheme_of_work__get_teacher_permissions (
 IN p_scheme_of_work_id INT,
 IN p_auth_user INT)
BEGIN
	
    SELECT 
      IFNULL(IFNULL(teach_sow.scheme_of_work_permission, teach_dep.scheme_of_work_permission), 7) as scheme_of_work_permission, 
      IFNULL(IFNULL(teach_sow.lesson_permission, teach_dep.lesson_permission), 7) as lesson_permission, 
      IFNULL(IFNULL(teach_sow.department_permission, teach_dep.department_permission), 7) as department_permission
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
    WHERE user.id = p_auth_user
    LIMIT 1;
END;
//

DELIMITER ;

CALL `drussell1974$cssow_api`.`scheme_of_work__get_teacher_permissions`(0, 2);
CALL `drussell1974$cssow_api`.`scheme_of_work__get_teacher_permissions`(11, 2);
CALL `drussell1974$cssow_api`.`scheme_of_work__get_teacher_permissions`(0, 12);
CALL `drussell1974$cssow_api`.`scheme_of_work__get_teacher_permissions`(11, 12);
CALL `drussell1974$cssow_api`.`scheme_of_work__get_teacher_permissions`(999999, 12);

