DELIMITER //

DROP PROCEDURE IF EXISTS department__get_my$2;

CREATE PROCEDURE department__get_my$2 (
 IN p_institute_id INT,
 IN p_department_id INT,
 IN p_show_published_state INT,
 IN p_auth_user INT)
BEGIN
    SELECT 
        dep.id as id,
        dep.name as name,
        top.id as topic_id,
        dep.created as created,
        dep.created_by as created_by,
        usr.first_name as created_by_name,
        dep.published as published
    FROM 
        sow_department as dep
        INNER JOIN sow_topic as top ON top.department_id = dep.id and parent_id is null
        INNER JOIN auth_user as usr ON usr.id = dep.created_by
    WHERE 
		dep.head_id = p_auth_user
        and dep.institute_id = p_institute_id
        and (dep.id = p_department_id or p_department_id = 0)
        and	(p_show_published_state % dep.published = 0
			or dep.created_by = p_auth_user)
    ORDER BY dep.name;
END;
//

DELIMITER ;

DELIMITER //

DROP PROCEDURE IF EXISTS department__get_my;

CREATE PROCEDURE department__get_my (
 IN p_institute_id INT,
 IN p_department_id INT,
 IN p_show_published_state INT,
 IN p_auth_user INT)
BEGIN
    SELECT 
        dep.id as id,
        dep.name as name,
        dep.created as created,
        dep.created_by as created_by,
        usr.first_name as created_by_name,
        dep.published as published
    FROM 
        sow_department as dep
        INNER JOIN auth_user as usr ON usr.id = dep.created_by
    WHERE 
		dep.head_id = p_auth_user
        and dep.institute_id = p_institute_id
        and (dep.id = p_department_id or p_department_id = 0)
        and	(p_show_published_state % published = 0
			or dep.created_by = p_auth_user)
    ORDER BY dep.name;
END;
//

DELIMITER ;
