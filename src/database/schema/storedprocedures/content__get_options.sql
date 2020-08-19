DELIMITER //

DROP PROCEDURE IF EXISTS content__get_options;

CREATE PROCEDURE content__get_options (
 IN p_key_stage_id INT,
 IN p_auth_user INT)
BEGIN
    SELECT 
        cnt.id as id, 
        cnt.description as description, 
        cnt.letter as letter_prefix
    FROM sow_content as cnt 
        WHERE key_stage_id = p_key_stage_id;
END;
//

DELIMITER ;