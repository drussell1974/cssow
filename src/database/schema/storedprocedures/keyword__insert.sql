DELIMITER //

DROP PROCEDURE IF EXISTS keyword__insert;

CREATE PROCEDURE `keyword__insert`(
 OUT p_keyword_id INT,
 IN p_name VARCHAR(100),
 IN p_definition TEXT,
 IN p_scheme_of_work_id INT,
 IN p_auth_user INT,
 IN p_published INT)
BEGIN
    INSERT INTO sow_key_word 
    (
        name, 
        definition,
        scheme_of_work_id,
        created,
        created_by,
        published
    ) 
    VALUES
    (
        p_name, 
        p_definition,
        p_scheme_of_work_id,
        NOW(),
        p_auth_user,
        p_published
    );

    SELECT LAST_INSERT_ID();
END;
//

DELIMITER ;