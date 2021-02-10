DELIMITER //

DROP PROCEDURE IF EXISTS institute__insert;

CREATE PROCEDURE institute__insert (
 OUT p_institute_id INT,
 IN p_name VARCHAR(100),
 IN p_auth_user INT,
 IN p_published INT)
BEGIN
    INSERT INTO sow_key_word 
    (
        name, 
        created,
        created_by,
        published
    ) 
    VALUES
    (
        p_name, 
        NOW(),
        p_auth_user,
        p_published
    );

    SELECT LAST_INSERT_ID();
END;
//

DELIMITER ;