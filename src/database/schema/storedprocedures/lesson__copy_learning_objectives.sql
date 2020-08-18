DELIMITER //

DROP PROCEDURE IF EXISTS lesson__copy_learning_objectives;

CREATE PROCEDURE lesson__copy_learning_objectives (
 IN p_new_lesson_id INT,
 IN p_old_lesson_id INT,
 IN p_auth_user INT)
BEGIN
    -- learning objectives
    INSERT INTO sow_learning_objective__has__lesson
        (lesson_id, learning_objective_id) 
    SELECT p_new_lesson_id, learning_objective_id
        FROM sow_learning_objective__has__lesson
        WHERE lesson_id = p_old_lesson_id;
END;
//

DELIMITER ;