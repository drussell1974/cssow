DELIMITER //

DROP PROCEDURE IF EXISTS scheme_of_work__get_schemeofwork_name_only;

CREATE PROCEDURE scheme_of_work__get_schemeofwork_name_only (
 IN p_scheme_of_work_id INT,
 IN p_department_id INT,
 IN p_institute_id INT,
 IN p_show_published_state INT,
 IN p_auth_user INT)
BEGIN
    SELECT
      sow.name as name
    FROM sow_scheme_of_work as sow
    LEFT JOIN auth_user as user ON user.id = sow.created_by
      WHERE
        sow.id = p_scheme_of_work_id 
        AND sow.department_id = p_department_id
        AND (p_show_published_state % sow.published = 0 
                or sow.created_by = p_auth_user
          );
END;
//

DELIMITER ;