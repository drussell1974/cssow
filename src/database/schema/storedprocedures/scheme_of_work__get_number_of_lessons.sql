DELIMITER //

DROP PROCEDURE IF EXISTS scheme_of_work__get_number_of_lessons;

CREATE PROCEDURE scheme_of_work__get_number_of_lessons (
 IN p_scheme_of_work_id INT,
 IN p_auth_user INT)
BEGIN
    SELECT count(les.id)
    FROM sow_lesson as les 
    WHERE les.scheme_of_work_id = p_scheme_of_work_id 
      AND (les.published = 1 
            or p_auth_user IN (SELECT auth_user_id 
                           FROM sow_teacher 
                           WHERE auth_user_id = p_auth_user AND scheme_of_work_id = les.scheme_of_work_id)
      );
END;

//

DELIMITER ;