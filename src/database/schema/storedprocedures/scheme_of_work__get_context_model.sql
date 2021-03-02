DELIMITER //

DROP PROCEDURE IF EXISTS scheme_of_work__get_context_model;

CREATE PROCEDURE scheme_of_work__get_context_model (
 IN p_scheme_of_work_id INT)
BEGIN
	/* return data for lightweight Context model (id, name, parent_id, created_by, published) */
    SELECT
        sow.id as id,
        sow.name as name,  
        sow.department_id as parent_id,
        sow.created_by as created_by_id,
        sow.published as published
    FROM sow_scheme_of_work as sow
	WHERE sow.id = p_scheme_of_work_id  
	;
END;
//

DELIMITER ;
CALL scheme_of_work__get_context_model(11);