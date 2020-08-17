DELIMITER //

DROP PROCEDURE IF EXISTS scheme_of_work__get_schemeofwork_name_only;

CREATE PROCEDURE scheme_of_work__get_schemeofwork_name_only (
 IN p_scheme_of_work_id INT,
 IN p_auth_user INT)
BEGIN
    SELECT
      sow.name as name
    FROM sow_scheme_of_work as sow
    LEFT JOIN auth_user as user ON user.id = sow.created_by
      WHERE sow.id = p_scheme_of_work_id 
        AND (sow.published = 1 
                or p_auth_user IN (SELECT auth_user_id 
                            FROM sow_teacher 
                            WHERE auth_user_id = p_auth_user AND scheme_of_work_id = sow.id)
        );
END;
//

DELIMITER ;