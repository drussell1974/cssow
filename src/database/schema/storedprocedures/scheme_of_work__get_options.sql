DELIMITER //

DROP PROCEDURE IF EXISTS scheme_of_work__get_options;

CREATE PROCEDURE scheme_of_work__get_options (
  IN auth_user INT)
BEGIN
    SELECT 
        sow.id as id, 
        sow.name as name, 
        ks.name as key_stage_name 
    FROM sow_scheme_of_work as sow 
        LEFT JOIN sow_key_stage as ks ON ks.id = sow.key_stage_id 
    WHERE sow.published = 1 OR is_sow_teacher(sow.id, auth_user)
        ORDER BY sow.key_stage_id;            
END;
//

DELIMITER ;