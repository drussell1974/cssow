DELIMITER //

DROP PROCEDURE IF EXISTS scheme_of_work__get_schemeofwork_name_only;

CREATE PROCEDURE scheme_of_work__get_schemeofwork_name_only (
  IN scheme_of_work_id INT,
  IN auth_user INT)
BEGIN
    SELECT
      sow.name as name
    FROM sow_scheme_of_work as sow
    LEFT JOIN auth_user as user ON user.id = sow.created_by
      WHERE sow.id = scheme_of_work_id 
        AND (sow.published = 1 
                or auth_user IN (SELECT auth_user_id 
                            FROM sow_teacher 
                            WHERE auth_user_id = auth_user_id AND scheme_of_work_id = sow.id)
        );
END;
//

DELIMITER ;