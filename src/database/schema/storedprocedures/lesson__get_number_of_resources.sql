DELIMITER //

DROP PROCEDURE IF EXISTS lesson__get_number_of_resources;

CREATE PROCEDURE lesson__get_number_of_resources (
 IN p_lesson_id INT,
 IN p_published INT,
 IN p_auth_user INT)
BEGIN
    SELECT 
        count(id)
    FROM 
        sow_resource 
    WHERE
        lesson_id = p_lesson_id;
END;
//

DELIMITER ;