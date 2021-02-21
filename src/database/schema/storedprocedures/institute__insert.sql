DELIMITER //

DROP PROCEDURE IF EXISTS institute__insert;

CREATE PROCEDURE institute__insert (
 OUT p_institute_id INT,
 IN p_name VARCHAR(100),
 IN p_teacher_id INT,
 IN p_auth_user INT,
 IN p_published INT)	
BEGIN
    INSERT INTO sow_institute
    (
        name, 
        head_id,
        created,
        created_by,
        published
    ) 
    VALUES
    (
        p_name, 
        p_teacher_id,
        NOW(),
        p_auth_user,
        p_published
    );

    SELECT LAST_INSERT_ID();
END;
//

DELIMITER ;