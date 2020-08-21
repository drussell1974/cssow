DELIMITER //

DROP PROCEDURE IF EXISTS year__get_options;

CREATE PROCEDURE year__get_options (
 IN p_key_stage_id INT,
 IN p_auth_user INT)
BEGIN
    SELECT 
        id, 
        name 
    FROM sow_year 
    WHERE key_stage_id = p_key_stage_id;
END;
//

DELIMITER ;