DELIMITER //

DROP PROCEDURE IF EXISTS scheme_of_work__get_number_of_resources;

CREATE PROCEDURE scheme_of_work__get_number_of_resources (
 IN p_scheme_of_work_id INT,
 IN p_auth_user INT)
BEGIN
    SELECT count(lo.id)
    FROM sow_lesson as les 
    INNER JOIN sow_resource as lo ON lo.lesson_id = les.id 
    WHERE les.scheme_of_work_id = p_scheme_of_work_id 
      AND (les.published = 1 
            or p_auth_user IN (SELECT auth_user_id 
                             FROM sow_teacher 
                             WHERE auth_user_id = p_auth_user AND scheme_of_work_id = les.scheme_of_work_id)
      );
END;

//

DELIMITER ;