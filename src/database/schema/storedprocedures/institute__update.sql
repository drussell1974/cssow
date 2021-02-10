DELIMITER //

DROP PROCEDURE IF EXISTS institute__update;

CREATE PROCEDURE institute__update (
 IN p_institute_id INT,
 IN p_name VARCHAR(100),
 IN p_published INT,
 IN p_auth_user INT)
BEGIN
    UPDATE sow_key_word 
    SET
        name = p_name, 
        published = p_published
    WHERE id = p_institute_id;
END;
//

DELIMITER ;