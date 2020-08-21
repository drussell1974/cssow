DELIMITER //

DROP PROCEDURE IF EXISTS keyword__update;

CREATE PROCEDURE keyword__update (
 IN p_keyword_id INT,
 IN p_name VARCHAR(100),
 IN p_defintion TEXT,
 IN p_published INT,
 IN p_auth_user INT)
BEGIN
    UPDATE sow_key_word 
    SET
        name = p_name, 
        definition = p_defintion,
        published = p_published
    WHERE id = p_keyword_id;
END;
//

DELIMITER ;