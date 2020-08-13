DELIMITER //

DROP PROCEDURE IF EXISTS scheme_of_work__get_key_stage_id_only;

CREATE PROCEDURE scheme_of_work__get_key_stage_id_only (
  IN scheme_of_work_id INT,
  IN auth_user INT)
BEGIN
    SELECT   
      sow.key_stage_id as key_stage_id  
    FROM sow_scheme_of_work as sow  
    LEFT JOIN auth_user as user ON user.id = sow.created_by  
      WHERE sow.id = scheme_of_work_id and is_sow_teacher(scheme_of_work_id, auth_user);
END;
//

DELIMITER ;