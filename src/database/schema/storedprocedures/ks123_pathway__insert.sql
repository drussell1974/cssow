DELIMITER //

DROP PROCEDURE IF EXISTS ks123_pathway__insert;

CREATE PROCEDURE ks123_pathway__insert (
    OUT p_pathway_item_id INT,
    IN p_objective VARCHAR(500),
    IN p_department_id INT,
    IN p_year_id INT,
    IN p_topic_id INT,
    IN p_published_state INT,
    IN p_created_by INT)
BEGIN
	INSERT IGNORE INTO sow_ks123_pathway (
		objective,
        department_id,
		year_id,
		topic_id,
		created_by,
		published
	)
	VALUES (
		p_objective,
        p_department_id,
		p_year_id,
		p_topic_id,
		p_created_by,
		p_published_state
	);
    
    SET p_pathway_item_id = LAST_INSERT_ID();
    SELECT p_pathway_item_id;
END;
//

DELIMITER ;

        