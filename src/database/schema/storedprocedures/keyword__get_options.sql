DELIMITER //

DROP PROCEDURE IF EXISTS keyword__get_options;

CREATE PROCEDURE keyword__get_options (
 IN p_scheme_of_work_id INT,
 IN p_auth_user INT)
BEGIN
    SELECT 
        id, 
        name, 
        definition,
        scheme_of_work_id
    FROM 
        sow_key_word kw
    WHERE 
        scheme_of_work_id = p_scheme_of_work_id
        AND published = 1 
    ORDER BY name;
END;
//

DELIMITER ;