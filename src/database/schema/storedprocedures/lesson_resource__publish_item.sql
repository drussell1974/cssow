DELIMITER //

DROP PROCEDURE IF EXISTS lesson_resource__publish_item;

CREATE PROCEDURE lesson_resource__publish_item (
 IN p_resource_id INT,
 IN p_scheme_of_work_id INT,
 IN p_published INT,
 IN p_auth_user INT)
BEGIN
    UPDATE sow_resource 
    SET published = p_published
    WHERE id = p_learning_objective_id
        AND p_auth_user IN (SELECT auth_user_id 
                            FROM sow_teacher 
                            WHERE auth_user_id = p_auth_user AND scheme_of_work_id = p_scheme_of_work_id);
END;
//

DELIMITER ;

