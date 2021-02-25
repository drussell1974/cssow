DELIMITER //

DROP PROCEDURE IF EXISTS institute__get_context_model;

CREATE PROCEDURE institute__get_context_model (
 IN p_institute_id INT)
BEGIN
	/* return data for lightweight Context model (id, name, parent_id, created_by, published) */
    SELECT 
        ins.id as id,
        ins.name as name,
        0 as parent_id,
        ins.created_by as created_by,
        ins.published as published
    FROM 
        sow_institute as ins
    WHERE
        ins.id = p_institute_id;
END;
//

DELIMITER ;

CALL institute__get_context_model(2);