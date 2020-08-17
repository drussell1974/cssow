DELIMITER //

DROP PROCEDURE IF EXISTS lesson__get_number_of_learning_objectives;

CREATE PROCEDURE lesson__get_number_of_learning_objectives (
 IN p_lesson_id INT,
 IN p_auth_user INT)
BEGIN
    SELECT count(lo.id)
    FROM sow_lesson as les 
    INNER JOIN sow_learning_objective__has__lesson as lo ON lo.lesson_id = les.id 
    WHERE les.id = p_lesson_id
      AND (les.published = 1 
            or p_auth_user IN (SELECT auth_user_id 
                             FROM sow_teacher 
                             WHERE auth_user_id = p_auth_user AND scheme_of_work_id = les.scheme_of_work_id)
      );
END;

//

DELIMITER ;