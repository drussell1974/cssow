DELIMITER //

DROP PROCEDURE IF EXISTS department__get_context_model$2;

CREATE PROCEDURE department__get_context_model$2 (
 IN p_institute_id INT,
 IN p_department_id INT)
BEGIN
	/* return data for lightweight Context model (id, name, parent_id, created_by, published) */
    SELECT 
        dep.id as id,
        dep.name as term,
        top.id as topic_id,
		dep.institute_id as parent_id,
        dep.created_by as created_by,
        dep.published as published
    FROM sow_department as dep
        -- use inner join as topic is created on department insert see stored procecure department__insert
	INNER JOIN sow_topic as top ON top.department_id = dep.id and top.parent_id is null
	WHERE
        dep.id = p_department_id
        AND dep.institute_id = p_institute_id
        AND top.published = 1;
END;
//

DELIMITER ;

CALL department__get_context_model$2(120, 84);

DELIMITER //

DROP PROCEDURE IF EXISTS department__get_context_model;

CREATE PROCEDURE department__get_context_model (
 IN p_institute_id INT,
 IN p_department_id INT)
BEGIN
	/* return data for lightweight Context model (id, name, parent_id, created_by, published) */
    SELECT 
        dep.id as id,
        dep.name as term,
		dep.institute_id as parent_id,
        dep.created_by as created_by,
        dep.published as published
    FROM 
        sow_department as dep
    WHERE
        dep.id = p_department_id
        AND dep.institute_id = p_institute_id;
END;
//

DELIMITER ;
