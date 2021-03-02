DELIMITER //

DROP PROCEDURE IF EXISTS topic__get_options;

CREATE PROCEDURE topic__get_options (
 IN p_topic_id INT,
 IN p_lvl INT,
 IN p_show_published_state INT,
 IN p_auth_user INT)
BEGIN
    SELECT 
        id, 
        name, 
        created, 
        created_by 
    FROM 
        sow_topic 
    WHERE 
        lvl = p_lvl and parent_id = p_topic_id
        and (p_show_published_state % published = 0
			or created_by = p_auth_user
        );
END;
//

DELIMITER ;