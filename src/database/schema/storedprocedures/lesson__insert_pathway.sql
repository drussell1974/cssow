DELIMITER //

DROP PROCEDURE IF EXISTS lesson__insert_pathway;

CREATE PROCEDURE lesson__insert_pathway (
 IN p_lesson_id INT,
 IN p_learning_objective_id INT,
 IN p_auth_user INT)
BEGIN
    DECLARE record_exists INT DEFAULT 0;

    SET record_exists = (SELECT count(*) FROM sow_lesson__has__pathway WHERE lesson_id = p_lesson_id AND learning_objective_id = p_learning_objective_id);

    IF record_exists = 0 THEN
        INSERT INTO sow_lesson__has__pathway 
            (lesson_id, learning_objective_id)
        VALUES
            (p_lesson_id, p_learning_objective_id);
    END IF;
END;
//

DELIMITER ;