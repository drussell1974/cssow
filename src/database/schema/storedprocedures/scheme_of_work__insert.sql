DELIMITER //

DROP PROCEDURE IF EXISTS scheme_of_work__insert;

CREATE PROCEDURE scheme_of_work__insert (
    OUT scheme_of_work_id INT,
    IN p_name VARCHAR(40),
    IN p_description TEXT,
    IN p_exam_board_id INT,
    IN p_key_stage_id INT,
    IN p_created DATETIME,
    IN p_created_by INT,
    IN p_published INT,
    IN p_auth_user INT)
BEGIN
    -- CHECK sow_teacher
    INSERT INTO sow_scheme_of_work 
    (
        name, 
        description, 
        exam_board_id, 
        key_stage_id, 
        created, 
        created_by, 
        published
    )
    VALUES
    (
        p_name,
        p_description,
        p_exam_board_id,
        p_key_stage_id,
        p_created,
        p_created_by,
        p_published
    );

    SELECT LAST_INSERT_ID();
END;
//

DELIMITER ;

