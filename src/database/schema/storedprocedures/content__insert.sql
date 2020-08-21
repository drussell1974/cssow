DELIMITER //

DROP PROCEDURE IF EXISTS content__insert;

CREATE PROCEDURE content__insert (
 IN p_content_id INT,
 IN p_description VARCHAR(500),
 IN p_prefix VARCHAR(30),
 IN p_key_stage_id INT,
 IN p_scheme_of_work_id INT,
 IN p_published INT,
 IN p_auth_user INT)
BEGIN
    INSERT INTO sow_content 
    (
        description, 
        letter, 
        key_stage_id,
        scheme_of_work_id,
        published, 
        created_by,
        created 
    )
    VALUES 
    (
        p_description,
        p_prefix, 
        p_key_stage_id, 
        p_scheme_of_work_id,
        p_published,
        p_auth_user,
        NOW()
    );

    SELECT LAST_INSERT_ID();
END;
//

DELIMITER ;