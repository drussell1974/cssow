DELIMITER //

DROP PROCEDURE IF EXISTS ks123_pathway__delete;

CREATE PROCEDURE ks123_pathway__delete (
    IN p_pathway_item_id INT,
    IN p_department_id INT,
    IN p_auth_user INT)
BEGIN
	DELETE FROM sow_ks123_pathway
    WHERE id = p_pathway_item_id AND published IN (32,64) 
                AND p_auth_user IN 
                        (SELECT head_id 
                        FROM sow_department
                        WHERE id = p_department_id);
END;
//

DELIMITER ;

        