DELIMITER //

DROP PROCEDURE IF EXISTS keystage__get_options;

CREATE PROCEDURE keystage__get_options (
 IN p_show_published_state INT,
 IN p_auth_user INT)
BEGIN
    SELECT 
        id,
        name 
    FROM 
        sow_key_stage
	WHERE p_show_published_state % published = 0
		or created_by = p_auth_user;
END;
//

DELIMITER ;