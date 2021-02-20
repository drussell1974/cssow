DELIMITER //

DROP PROCEDURE IF EXISTS scheme_of_work__get_key_stage_id_only;

CREATE PROCEDURE scheme_of_work__get_key_stage_id_only (
 IN p_scheme_of_work_id INT,
 IN p_department_id INT,
 IN p_institute_id INT,
 IN p_auth_user INT)
BEGIN
    SELECT   
      sow.key_stage_id as key_stage_id  
    FROM sow_scheme_of_work as sow  
    LEFT JOIN auth_user as user ON user.id = sow.created_by  
      WHERE sow.department_id = p_department_id 
        AND sow.id = p_scheme_of_work_id 
        AND (sow.published = 1 
              or p_auth_user IN (SELECT auth_user_id 
                              FROM sow_teacher 
                              WHERE auth_user_id = p_auth_user AND scheme_of_work_id = sow.id)
        );
END;
//

DELIMITER ;