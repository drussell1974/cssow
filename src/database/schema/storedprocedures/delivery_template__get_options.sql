DELIMITER //

DROP PROCEDURE IF EXISTS delivery_template__get_options;

CREATE PROCEDURE delivery_template__get_options ()
BEGIN
    SELECT 
        id, 
        name, 
        created, 
        created_by 
    FROM 
        sow_delivery_template;
END;
//

DELIMITER ;