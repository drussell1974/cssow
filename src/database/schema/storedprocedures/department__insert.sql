DELIMITER //

DROP PROCEDURE IF EXISTS department__insert;

CREATE PROCEDURE department__insert (
    OUT p_department_id INT,
    IN p_name VARCHAR(70),
    IN p_teacher_id INT,
    IN p_institute_id INT,
    IN p_created DATETIME,
    IN p_created_by INT,
	IN p_published INT)
BEGIN
    -- CHECK sow_department
    INSERT INTO sow_department 
    (
        name, 
        head_id, 
        institute_id,
        created, 
        created_by,
        published
    )
    VALUES
    (
        p_name,
        p_teacher_id,
        p_institute_id,
        p_created,
        p_created_by,
        p_published
    );
    -- Create top level topic
    SET p_department_id = LAST_INSERT_ID();
    
    INSERT INTO sow_topic (name, lvl, department_id, published) VALUES (p_name, 0, p_department_id, 1);
    SELECT p_department_id;
END;
//

DELIMITER ;
