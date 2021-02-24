DELIMITER //

DROP PROCEDURE IF EXISTS content__delete_unpublished;

CREATE PROCEDURE content__delete_unpublished (
 IN p_scheme_of_work_id INT,
 IN p_remove_published_state INT,
 IN p_auth_user INT)
BEGIN
    DELETE sow_content
    FROM sow_content
    INNER JOIN sow_scheme_of_work as sow ON sow.key_stage_id = sow_content.key_stage_id
    WHERE 
		sow.id = p_scheme_of_work_id
		AND sow_content.published = p_remove_published_state;
END;
//

DELIMITER ;