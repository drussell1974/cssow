DELIMITER //

DROP PROCEDURE IF EXISTS keyword__get_options;

CREATE PROCEDURE keyword__get_options (
 IN p_auth_user INT)
BEGIN
    SELECT 
        id, 
        name, 
        definition 
    FROM 
        sow_key_word kw
    WHERE 
        published = 1 
    ORDER BY name;
END;
//

DELIMITER ;