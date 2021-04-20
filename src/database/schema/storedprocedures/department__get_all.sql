DELIMITER //

DROP PROCEDURE IF EXISTS department__get_all$2;

CREATE PROCEDURE department__get_all$2 (
 IN p_institute_id INT,
 IN p_show_published_state INT,
 IN p_auth_user INT)
BEGIN
    SELECT 
        dep.id as id,
        dep.name as name,
        top.id as topic_id,
        dep.institute_id as institute_id,
        ins.name as institute_name,
        dep.created as created,
        dep.created_by as created_by,
        usr.first_name as created_by_name,
        dep.published as published
    FROM 
        sow_department as dep
        INNER JOIN sow_topic as top ON top.department_id = dep.id and parent_id is null
		INNER JOIN sow_institute as ins ON ins.id = dep.institute_id
        INNER JOIN auth_user as usr ON usr.id = dep.created_by
    WHERE 
		dep.institute_id = p_institute_id 
        and (p_show_published_state % dep.published = 0 
			or dep.created_by = p_auth_user)
    ORDER BY dep.name;
END;
//

DELIMITER ;

CALL department__get_all$2(2,32, 2);

DELIMITER //

DROP PROCEDURE IF EXISTS department__get_all;

CREATE PROCEDURE department__get_all (
 IN p_institute_id INT,
 IN p_show_published_state INT,
 IN p_auth_user INT)
BEGIN
    SELECT 
        dep.id as id,
        dep.name as name,
        dep.institute_id as institute_id,
        dep.created as created,
        dep.created_by as created_by,
        usr.first_name as created_by_name,
        dep.published as published
    FROM 
        sow_department as dep
        INNER JOIN auth_user as usr ON usr.id = dep.created_by
    WHERE 
		dep.institute_id = p_institute_id 
        and (p_show_published_state % published = 0 
			or dep.created_by = p_auth_user)
    ORDER BY dep.name;
END;
//

DELIMITER ;
