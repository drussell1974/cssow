DELIMITER //

DROP PROCEDURE IF EXISTS keyword__get;

CREATE PROCEDURE keyword__get (
 IN p_keyword_id INT,
 IN p_auth_user INT)
BEGIN
    SELECT 
        id,
        name 
    FROM 
        sow_key_word
    WHERE
        id = p_keyword_id;
END;
//

DELIMITER ;