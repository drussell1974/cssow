DELIMITER //
DROP PROCEDURE IF EXISTS lesson_learning_objective__get_learning_objective_ids;

DROP PROCEDURE IF EXISTS lesson_learning_objective__delete_unpublished;

CREATE PROCEDURE lesson_learning_objective__delete_unpublished (
 IN p_lesson_id INT,
 IN p_auth_user INT)
BEGIN
    DELETE sow_learning_objective__has__lesson
    FROM sow_learning_objective__has__lesson 
    INNER JOIN sow_lesson AS l ON l.id = sow_learning_objective__has__lesson.lesson_id
    WHERE
        sow_learning_objective__has__lesson.published IN (0,2)
        AND l.id = p_lesson_id;
END;
//

DELIMITER ;

