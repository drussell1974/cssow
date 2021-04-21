DELIMITER //

DROP PROCEDURE IF EXISTS topic__insert;

CREATE PROCEDURE topic__insert (
    OUT p_topic_id INT,
    IN p_name VARCHAR(45),
    IN p_department_id INT,
    IN p_parent_topic_id INT,
    IN p_lvl INT,
    IN p_published_state INT,
    IN p_created_by INT)
BEGIN
    
	INSERT IGNORE INTO sow_topic (
		name,
        department_id,
		parent_id,
        lvl,
		created_by,
		published
	)
	VALUES (
		p_name,
        p_department_id,
		p_parent_topic_id,
        p_lvl,
		p_created_by,
		p_published_state
	);
    
    SET p_topic_id = LAST_INSERT_ID();
    SELECT p_topic_id;
END;
//

DELIMITER ;

        