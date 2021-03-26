DELIMITER //

DROP PROCEDURE IF EXISTS keystage__insert_from_pathway_template;

CREATE PROCEDURE keystage__insert_from_pathway_template (
    IN p_pathway_template_id INT,
    IN p_department_id INT,
    IN p_created DATETIME,
    IN p_created_by INT,
    IN p_published_state INT)
BEGIN
    INSERT IGNORE INTO sow_key_stage (
        name, 
        department_id,
        created,
        created_by,
        published)
    SELECT 
        name,
        p_department_id,
        p_created,
        p_created_by,
        p_published_state
    FROM sow_pathway_template_key_stages
    WHERE pathway_template_id = p_pathway_template_id;
	
END;
//

DELIMITER ;