DELIMITER //

DROP PROCEDURE IF EXISTS topic__get_model;

CREATE PROCEDURE topic__get_model (
 IN p_topic_id INT,
 IN p_department_id INT,
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
        id = p_topic_id
        and (p_show_published_state % published = 0
			or created_by = p_auth_user
        );
END;
//

DELIMITER ;