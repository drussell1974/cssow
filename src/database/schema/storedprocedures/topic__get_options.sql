DELIMITER //

DROP PROCEDURE IF EXISTS topic__get_options$2;

CREATE PROCEDURE topic__get_options$2 (
 IN p_topic_id INT,
 IN p_department_id INT,
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
		department_id = p_department_id
        and lvl = p_lvl and parent_id = p_topic_id
        -- and (p_show_published_state % published = 0
		-- 	or created_by = p_auth_user
        -- )
        ;
END;
//

DELIMITER ;

CALL topic__get_options$2(2, 5, 2, 1, 2);

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