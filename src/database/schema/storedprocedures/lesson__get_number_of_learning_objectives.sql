DELIMITER //

DROP PROCEDURE IF EXISTS lesson__get_number_of_learning_objectives;

CREATE PROCEDURE lesson__get_number_of_learning_objectives (
 IN p_lesson_id INT,
 IN p_show_published_state INT,
 IN p_auth_user INT)
BEGIN
    SELECT count(lo.id)
    FROM sow_lesson as les 
    INNER JOIN sow_learning_objective__has__lesson as lo ON lo.lesson_id = les.id 
    WHERE les.id = p_lesson_id
      AND (p_show_published_state % les.published = 0 
            or les.created_by = p_auth_user
		);
END;

//

DELIMITER ;