DELIMITER //

DROP PROCEDURE IF EXISTS scheme_of_work__get_team_permissions;

CREATE PROCEDURE scheme_of_work__get_team_permissions (
 IN p_auth_user INT)
BEGIN
    SELECT 
        sow_teach.auth_user_id as auth_user_id,
        user.first_name as auth_user_name,
		sow_teach.scheme_of_work_id as scheme_of_work_id,
        sow.name as scheme_of_work_name,
        sow_teach.department_permission,
        sow_teach.scheme_of_work_permission,
        sow_teach.lesson_permission
    FROM sow_department as dep
    INNER JOIN sow_department__has__teacher as dep_teach
		ON dep_teach.department_id = dep.id -- link department teachers to department
	INNER JOIN auth_user as user 
		ON user.id = dep_teach.auth_user_id -- get teachers details from auth_user
	INNER JOIN sow_scheme_of_work__has__teacher as sow_teach 
		ON sow_teach.auth_user_id = dep_teach.auth_user_id -- link schemes of work to department teachers
	INNER JOIN sow_scheme_of_work as sow
		ON sow.id = sow_teach.scheme_of_work_id
	WHERE dep.head_id = p_auth_user; -- get head for department
END;
//

DELIMITER ;

CALL scheme_of_work__get_team_permissions(2);