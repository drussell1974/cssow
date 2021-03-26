DELIMITER //

DROP PROCEDURE IF EXISTS pathway_template__get_options;

CREATE PROCEDURE pathway_template__get_options ()
BEGIN
    SELECT 
        id, 
        name, 
        created, 
        created_by 
    FROM 
        sow_pathway_template
	ORDER BY show_order ASC;
END;
//

DELIMITER ;