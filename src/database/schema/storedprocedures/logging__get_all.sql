DELIMITER //

DROP PROCEDURE IF EXISTS logging__get_all;

CREATE PROCEDURE logging__get_all (
 IN p_start DATETIME,
 IN p_end DATETIME,
 IN p_event_type INT,
 IN p_auth_user INT)
BEGIN
    SELECT 
        id as id,
        created as created,
        event_type as event_type, 
        message as message,
        details as details,
        category as category,
        subcategory as subcategory
    FROM 
        sow_logging
    WHERE
        event_type <= p_event_type AND created BETWEEN p_start AND p_end;
END;
//

DELIMITER ;