DELIMITER //
DROP PROCEDURE IF EXISTS ks123_pathway__get_all;

CREATE PROCEDURE ks123_pathway__get_all (
 IN p_department_id INT,
 IN p_show_published_state INT,
 IN p_auth_user INT)
BEGIN
    SELECT 
        pw.id, pw.objective, pw.year_id, yr.name, pw.topic_id, tp.name, pw.published
    FROM 
        sow_ks123_pathway as pw
        INNER JOIN sow_year as yr ON yr.id = pw.year_id
        INNER JOIN sow_topic as tp ON tp.id = pw.topic_id
        INNER JOIN sow_key_stage as ks ON ks.id = yr.key_stage_id
    WHERE 
		pw.department_id = p_department_id and
        (p_show_published_state % pw.published = 0 
			or pw.created_by = p_auth_user
        );
END;
//

DELIMITER ;
