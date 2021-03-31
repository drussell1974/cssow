DELIMITER //

DROP PROCEDURE IF EXISTS ks123_pathway__update;

CREATE PROCEDURE ks123_pathway__update (
    IN p_pathway_item_id INT,
    IN p_objective VARCHAR(500),
    IN p_year_id INT,
    IN p_topic_id INT,
    IN p_published_state INT,
    IN p_created_by INT)
BEGIN
	UPDATE sow_ks123_pathway
    SET
		objective = p_objective,
		year_id = p_year_id,
		topic_id = p_topic_id,
		created_by = p_created_by,
		published = p_published_state
	WHERE id = p_pathway_item_id;
END;
//

DELIMITER ;

        