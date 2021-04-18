DELIMITER //

DROP PROCEDURE IF EXISTS topic__delete;

CREATE PROCEDURE topic__delete (
    IN p_topic_id INT,
    IN p_published_state INT,
    IN p_auth_user INT)
BEGIN
    
	DELETE FROM sow_topic 
    WHERE id = p_topic_id
		and (p_published_state % published = 0
		or created_by = p_auth_user)
	;
END;
//

DELIMITER ;

        