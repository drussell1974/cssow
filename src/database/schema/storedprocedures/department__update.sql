DELIMITER //

DROP PROCEDURE IF EXISTS department__update;

CREATE PROCEDURE department__update (
 IN p_department_id INT,
 IN p_name VARCHAR(100),
 IN p_institute_id INT,
 IN p_published INT,
 IN p_auth_user INT)
BEGIN
    UPDATE sow_department
    SET
        name = p_name,
        institute_id = p_institute_id,
        published = p_published,
        modified_by = p_auth_user
    WHERE id = p_department_id;
END;
//

DELIMITER ;