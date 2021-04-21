DELIMITER //

DROP PROCEDURE IF EXISTS department__get$2;

CREATE PROCEDURE department__get$2 (
 IN p_department_id INT,
 IN p_show_published_state INT,
 IN p_auth_user INT)
BEGIN
    SELECT 
        dep.id as id,
        dep.name as name,
        top.id as topic_id,
        dep.head_id as hod_id,
		dep.institute_id as institute_id,
        ins.name as institute_name,
        dep.created as created,
        dep.created_by as created_by,
        usr.first_name as created_by_name,
        dep.published as published
    FROM 
        sow_department as dep
        INNER JOIN sow_topic as top on top.department_id = dep.id and top.parent_id is null
		INNER JOIN sow_institute as ins on ins.id = dep.institute_id
        INNER JOIN auth_user as usr ON usr.id = dep.created_by
    WHERE
        dep.id = p_department_id 
        AND (p_show_published_state % dep.published = 0 
			 or dep.created_by = p_auth_user);
END;
//

DELIMITER ;

CALL department__get$2(2,1,2);

DELIMITER //

DROP PROCEDURE IF EXISTS department__get;

CREATE PROCEDURE department__get (
 IN p_department_id INT,
 IN p_show_published_state INT,
 IN p_auth_user INT)
BEGIN
    SELECT 
        dep.id as id,
        dep.name as name,
        dep.head_id as hod_id,
		dep.institute_id as institute_id,
        ins.name as institute_name,
        dep.created as created,
        dep.created_by as created_by,
        usr.first_name as created_by_name,
        dep.published as published
    FROM 
        sow_department as dep
		INNER JOIN sow_institute as ins on ins.id = dep.institute_id
        INNER JOIN auth_user as usr ON usr.id = dep.created_by
    WHERE
        dep.id = p_department_id 
        AND (p_show_published_state % dep.published = 0 
			 or dep.created_by = p_auth_user);
END;
//

DELIMITER ;