DELIMITER //

DROP PROCEDURE IF EXISTS lesson_schedule__delete_unpublished;

CREATE PROCEDURE lesson_schedule__delete_unpublished (
 IN p_lesson_id INT,
 IN p_scheme_of_work_id INT,
 IN p_auth_user INT)
BEGIN
    DELETE FROM sow_lesson_schedule
    WHERE lesson_id = p_lesson_id 
            AND published IN (32,64) 
            AND p_auth_user IN 
                    (SELECT auth_user_id 
                    FROM sow_teacher 
                    WHERE scheme_of_work_id = p_scheme_of_work_id);
END;
//

DELIMITER ;