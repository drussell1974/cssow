DELIMITER //
DROP PROCEDURE IF EXISTS lesson_learning_objective__delete_unpublished;

CREATE PROCEDURE lesson_learning_objective__delete_unpublished (
 IN p_scheme_of_work_id INT,
 IN p_lesson_id INT,
 IN p_auth_user INT)
BEGIN
    DELETE sow_learning_objective__has__lesson
    FROM sow_learning_objective__has__lesson 
    INNER JOIN sow_lesson AS l ON l.id = sow_learning_objective__has__lesson.lesson_id
    WHERE
        sow_learning_objective__has__lesson.published IN (32,64)
        AND l.scheme_of_work_id = p_scheme_of_work_id
        AND l.id = p_lesson_id;
END;
//

DELIMITER ;

