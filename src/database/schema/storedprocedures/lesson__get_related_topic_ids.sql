DELIMITER //

DROP PROCEDURE IF EXISTS lesson__get_related_topic_ids;

CREATE PROCEDURE lesson__get_related_topic_ids (
 IN p_lesson_id INT,
 IN p_parent_topic_id INT,
 IN p_auth_user INT)
BEGIN
      SELECT 
            top.id as id, 
            top.name as name, 
            letop.topic_id as checked, 
            (SELECT count(topic_id) 
                  FROM sow_learning_objective AS lob 
                  LEFT JOIN sow_learning_objective__has__lesson AS lole ON lole.learning_objective_id = lob.id 
                  WHERE lole.lesson_id = letop.lesson_id and lob.topic_id = top.id) as disabled 
      FROM sow_topic AS top 
            LEFT JOIN sow_lesson__has__topics AS letop ON top.id = letop.topic_id and letop.lesson_id = p_lesson_id
      WHERE top.parent_id = p_parent_topic_id;
END;

//

DELIMITER ;