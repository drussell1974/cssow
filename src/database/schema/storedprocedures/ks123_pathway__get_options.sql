DELIMITER //

DROP PROCEDURE IF EXISTS ks123_pathway__get_options;

CREATE PROCEDURE ks123_pathway__get_options (
 IN p_key_stage_id INT,
 IN p_topic_id INT,
 IN p_show_published_state INT,
 IN p_auth_user INT)
BEGIN
    SELECT 
        pw.id, CONCAT(ks.name, " ", pw.objective)
    FROM 
        sow_ks123_pathway as pw
        INNER JOIN sow_year as yr ON yr.id = pw.year_id
        INNER JOIN sow_key_stage as ks ON ks.id = yr.key_stage_id
    WHERE 
        yr.key_stage_id BETWEEN p_key_stage_id - 2 and p_key_stage_id and 
        pw.topic_id = p_topic_id and
        (p_show_published_state % pw.published = 0 
			or pw.created_by = p_auth_user
        );
END;
//

DELIMITER ;

CALL ks123_pathway__get_options(4, 4, 1, 2);