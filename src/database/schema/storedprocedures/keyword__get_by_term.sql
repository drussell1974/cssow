DELIMITER //

DROP PROCEDURE IF EXISTS keyword__get_by_term;

CREATE PROCEDURE keyword__get_by_term (
 IN p_search VARCHAR(100),
 IN p_auth_user INT)

BEGIN
    SELECT 
        id as id,
        name as term, 
        definition as definition 
    FROM 
        sow_key_word kw 
    WHERE 
        name LIKE CONCAT('%', p_search, '%') AND kw.published = 1
    ORDER BY name;
END;
//

DELIMITER ;