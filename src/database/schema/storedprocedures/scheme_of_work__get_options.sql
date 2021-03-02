DELIMITER //

DROP PROCEDURE IF EXISTS scheme_of_work__get_options;

CREATE PROCEDURE scheme_of_work__get_options (
 IN p_department_id INT,
 IN p_institute_id INT,
 IN p_show_published_state INT,
 IN p_auth_user INT
)
BEGIN
    SELECT 
        sow.id as id, 
        sow.name as name, 
        ks.name as key_stage_name 
    FROM sow_scheme_of_work as sow 
        LEFT JOIN sow_key_stage as ks ON ks.id = sow.key_stage_id 
    WHERE 
        sow.department_id = p_department_id 
        AND (p_show_published_state % sow.published = 0 #323 use p_show_published_state and remove subquery 
			or sow.created_by = p_auth_user)
	ORDER BY sow.key_stage_id;
END;
//

DELIMITER ;