DELIMITER //

DROP PROCEDURE IF EXISTS scheme_of_work__insert$2;

CREATE PROCEDURE scheme_of_work__insert$2 (
    OUT scheme_of_work_id INT,
    IN p_name VARCHAR(40),
    IN p_study_duration INT,
    IN p_start_study_in_year INT,
    IN p_description TEXT,
    IN p_exam_board_id INT,
    IN p_key_stage_id INT,
    IN p_department_id INT,
    IN p_created DATETIME,
    IN p_created_by INT,
    IN p_published INT,
    IN p_auth_user INT)
BEGIN
    -- CHECK sow_teacher
    INSERT INTO sow_scheme_of_work 
    (
        name, 
        study_duration,
        start_study_in_year, -- E.g. Year7 for KS3, Year 10 for KS4
        description, 
        exam_board_id, 
        key_stage_id, 
        department_id,
        created, 
        created_by, 
        published
    )
    VALUES
    (
        p_name,
        p_study_duration,
        p_start_study_in_year,
        p_description,
        p_exam_board_id,
        p_key_stage_id,
        p_department_id,
        p_created,
        p_created_by,
        p_published
    );
	-- get last inserted scheme of work
    SET @last_insert_id = LAST_INSERT_ID();
    
	-- create available years for key stage
	CALL year__insert(
		p_study_duration, 
        p_start_study_in_year,
		p_key_stage_id,
		p_created_by,
		p_published);

	-- return last inserted scheme of work
    SELECT @last_insert_id;
END;
//

DELIMITER ;

DELIMITER //

DROP PROCEDURE IF EXISTS scheme_of_work__insert;

CREATE PROCEDURE scheme_of_work__insert (
    OUT scheme_of_work_id INT,
    IN p_name VARCHAR(40),
    IN p_description TEXT,
    IN p_exam_board_id INT,
    IN p_key_stage_id INT,
    IN p_department_id INT,
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
        department_id,
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
        p_department_id,
        p_created,
        p_created_by,
        p_published
    );

    SELECT LAST_INSERT_ID();
END;
//

DELIMITER ;

