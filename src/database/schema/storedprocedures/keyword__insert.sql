DELIMITER //

DROP PROCEDURE IF EXISTS keyword__insert;

CREATE PROCEDURE keyword__insert (
 OUT p_keyword_id INT,
 IN p_name VARCHAR(100),
 IN p_definition TEXT,
 IN p_auth_user INT,
 IN p_published INT)
BEGIN
    INSERT INTO sow_key_word 
    (
        name, 
        definition,
        created,
        created_by,
        published
    ) 
    VALUES
    (
        p_name, 
        p_definition,
        NOW(),
        p_auth_user,
        p_published
    );

    SELECT LAST_INSERT_ID();
END;
//

DELIMITER ;