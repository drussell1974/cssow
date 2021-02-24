DELIMITER //

DROP PROCEDURE IF EXISTS content__delete;

CREATE PROCEDURE content__delete (
 IN p_content_id INT,
 IN p_remove_published_state INT,
 IN p_auth_user INT)
BEGIN
    DELETE FROM sow_content 
    WHERE id = p_content_id 
		AND published = p_remove_published_state;
END;
//

DELIMITER ;