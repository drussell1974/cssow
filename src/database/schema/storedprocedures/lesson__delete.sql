DELIMITER //

DROP PROCEDURE IF EXISTS lesson__delete;

CREATE PROCEDURE lesson__delete (
 IN p_lesson_id INT,
 IN p_auth_user INT)
BEGIN
    DELETE sow_lesson 
    FROM sow_lesson
    INNER JOIN sow_scheme_of_work AS sow ON sow.id = sow_lesson.scheme_of_work_id
    WHERE 
        sow_lesson.id = p_lesson_id AND sow_lesson.published IN (32,64) 
                AND p_auth_user IN 
                        (SELECT auth_user_id 
                        FROM sow_teacher 
                        WHERE scheme_of_work_id = sow_lesson.scheme_of_work_id);
END;
//

DELIMITER ;