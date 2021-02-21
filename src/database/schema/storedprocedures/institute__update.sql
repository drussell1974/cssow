DELIMITER //

DROP PROCEDURE IF EXISTS institute__update;

CREATE PROCEDURE institute__update (
 IN p_institute_id INT,
 IN p_name VARCHAR(100),
 IN p_teacher_id INT,
 IN p_published INT,
 IN p_auth_user INT)
BEGIN
    UPDATE sow_institute
    SET
        name = p_name, 
        head_id = p_teacher_id,
        published = p_published,
        modified_by = p_auth_user
    WHERE id = p_institute_id;
END;
//

DELIMITER ;