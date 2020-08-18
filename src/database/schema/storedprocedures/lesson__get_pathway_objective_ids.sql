DELIMITER //

DROP PROCEDURE IF EXISTS lesson__get_pathway_objective_ids;

CREATE PROCEDURE lesson__get_pathway_objective_ids (
 IN p_lesson_id INT,
 IN p_auth_user INT)
BEGIN

      SELECT learning_objective_id
      FROM sow_lesson__has__pathway as lp
      INNER JOIN sow_lesson as les on les.id = lp.lesson_id
      WHERE lp.lesson_id = p_lesson_id
      AND les.published = 1 
            or p_auth_user IN (SELECT auth_user_id 
                             FROM sow_teacher 
                             WHERE auth_user_id = p_auth_user AND scheme_of_work_id = les.scheme_of_work_id);
END;

//

DELIMITER ;