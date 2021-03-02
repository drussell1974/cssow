DELIMITER //

DROP PROCEDURE IF EXISTS lesson__get_ks123_pathway_objective_ids;

CREATE PROCEDURE lesson__get_ks123_pathway_objective_ids (
 IN p_lesson_id INT,
 IN p_show_published_state INT,
 IN p_auth_user INT)
BEGIN
      SELECT ks123_pathway_id
      FROM sow_lesson__has__ks123_pathway as lp
      INNER JOIN sow_lesson as les on les.id = lp.lesson_id
      WHERE lp.lesson_id = p_lesson_id
      AND (p_show_published_state % les.published = 0 
            or les.created_by = p_auth_user
		);
END;

//

DELIMITER;