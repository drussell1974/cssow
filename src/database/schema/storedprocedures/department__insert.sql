DELIMITER //

DROP PROCEDURE IF EXISTS department__insert;

CREATE PROCEDURE department__insert (
    OUT p_department_id INT,
    IN p_name VARCHAR(70),
    IN p_head_id INT,
    IN p_school_id INT,
    IN p_created DATETIME,
    IN p_created_by INT,
    IN p_auth_user INT)
BEGIN
    -- CHECK sow_department
    INSERT INTO sow_department 
    (
        name, 
        head_id, 
        school_id,
        created, 
        created_by, 
        published
    )
    VALUES
    (
        p_name,
        p_head_id,
        p_school_id,
        p_created,
        p_created_by,
        p_published
    );

    SELECT LAST_INSERT_ID();
END;
//

DELIMITER ;

