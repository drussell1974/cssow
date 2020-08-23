DELIMITER //

DROP PROCEDURE IF EXISTS logging__get_all;

CREATE PROCEDURE logging__get_all (
 IN p_start DATETIME,
 IN p_end DATETIME,
 IN p_auth_user INT)
BEGIN
    SELECT 
        id as id,
        created as created,
        0 as type_id, 
        message as message,
        details as details,
        category as category,
        subcategory as subcategory
    FROM 
        sow_logging
    WHERE
        created BETWEEN p_start AND p_end;
END;
//

DELIMITER ;