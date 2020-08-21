DELIMITER //

DROP PROCEDURE IF EXISTS lesson_learning_objective__publish_item;

CREATE PROCEDURE lesson_learning_objective__publish_item (
 IN p_learning_objective_id INT,
 IN p_lesson_id INT,
 IN p_scheme_of_work_id INT,
 IN p_published INT,
 IN p_auth_user INT)
BEGIN
    UPDATE sow_learning_objective__has__lesson 
    SET published = p_published
    WHERE lesson_id = p_lesson_id AND learning_objective_id = p_learning_objective_id
        AND p_auth_user IN (SELECT auth_user_id 
                            FROM sow_teacher 
                            WHERE auth_user_id = p_auth_user AND scheme_of_work_id = p_scheme_of_work_id);
END;
//

DELIMITER ;

