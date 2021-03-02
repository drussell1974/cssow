DELIMITER //

DROP PROCEDURE IF EXISTS department__get_context_model;

CREATE PROCEDURE department__get_context_model (
 IN p_department_id INT,
 IN p_institute_id INT)
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

CALL department__get_context_model(2, 5);