DELIMITER //

DROP PROCEDURE IF EXISTS keystage__get_options;

CREATE PROCEDURE keystage__get_options (
 IN p_auth_user INT)
BEGIN
    SELECT 
        id,
        name 
    FROM 
        sow_key_stage;
END;
//

DELIMITER ;