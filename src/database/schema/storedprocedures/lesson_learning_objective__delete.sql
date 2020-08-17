DELIMITER //

DROP PROCEDURE IF EXISTS lesson_learning_objective__delete;

CREATE PROCEDURE lesson_learning_objective__delete (
 IN p_learning_objective_id INT,
 IN p_auth_user INT)
BEGIN
    DECLARE number_of_linked_lessons INT DEFAULT 0;
    
    DELETE sow_learning_objective__has__lesson
    FROM sow_learning_objective__has__lesson 
    INNER JOIN sow_lesson AS l ON l.id = sow_learning_objective__has__lesson.lesson_id
    WHERE learning_objective_id = p_learning_objective_id
        AND sow_learning_objective__has__lesson.published IN (0,2)
        -- delete only learning objectives from lesson owned by auth_user
        AND p_auth_user IN (SELECT auth_user_id 
                          FROM sow_teacher 
                          WHERE auth_user_id = p_auth_user AND scheme_of_work_id = l.scheme_of_work_id);

    SELECT count(*) 
    INTO number_of_linked_lessons
    FROM sow_learning_objective__has__lesson
    WHERE learning_objective_id = p_learning_objective_id;

    -- Delete the learning objective if it's the only one and still unpublished
    IF number_of_linked_lessons = 1 THEN
        DELETE FROM sow_learning_objective 
        WHERE id = p_learning_objective_id 
        AND published IN (0, 2)
        -- delete only learning objectives from lesson owned by auth_user
        AND p_auth_user IN (SELECT auth_user_id 
                            FROM sow_teacher 
                            WHERE auth_user_id = p_auth_user AND scheme_of_work_id = l.scheme_of_work_id);
    END IF;
END;
//

DELIMITER ;

