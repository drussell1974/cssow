DELIMITER //

DROP PROCEDURE IF EXISTS topic__update;

CREATE PROCEDURE topic__update (
    IN p_topic_id INT,
    IN p_name VARCHAR(500),
    IN p_department_id INT,
    IN p_parent_topic_id INT,
    IN p_lvl INT,
    IN p_published_state INT,
    IN p_created_by INT)
BEGIN
	UPDATE sow_topic
    SET
		name = p_name,
        department_id = p_department_id,
		parent_id = p_parent_topic_id,
        lvl = p_lvl,
		created_by = p_created_by,
		published = p_published_state
	WHERE id = p_topic_id;
END;
//

DELIMITER ;

        