DELIMITER //

DROP PROCEDURE IF EXISTS ks123_pathway__get_options;

CREATE PROCEDURE ks123_pathway__get_options (
 IN p_year_id INT,
 IN p_topic_id INT,
 IN p_show_published_state INT,
 IN p_auth_user INT)
BEGIN
    SELECT 
        id, objective 
    FROM 
        sow_ks123_pathway 
    WHERE 
        year_id = p_year_id and 
        topic_id = p_topic_id and
        (p_show_published_state % published = 0 
			or created_by = p_auth_user
        );
END;
//

DELIMITER ;