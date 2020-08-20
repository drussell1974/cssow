DELIMITER //

DROP PROCEDURE IF EXISTS content__update;

CREATE PROCEDURE content__update (
 IN p_content_id INT,
 IN p_description VARCHAR(500),
 IN p_prefix VARCHAR(30),
 IN p_key_stage_id INT,
 IN p_scheme_of_work_id INT,
 IN p_published INT,
 IN p_auth_user INT)
BEGIN
    UPDATE 
        sow_content 
    SET 
        description = p_description, 
        letter = p_prefix,
        key_stage_id = p_key_stage_id,
        scheme_of_work_id = p_scheme_of_work_id,
        published = p_published
    WHERE
        id = p_content_id;
END;
//

DELIMITER ;