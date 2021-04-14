DELIMITER //

DROP PROCEDURE IF EXISTS academic_year__insert;

CREATE PROCEDURE academic_year__insert (
    -- OUT p_department_id INT,
    IN p_year INT,
    IN p_start_date datetime,
    IN p_end_date datetime,
    IN p_institute_id INT,
	IN p_published_state INT,
    IN p_created_by INT)
BEGIN
    -- CHECK sow_department
    INSERT INTO sow_academic_year 
    (
        year, 
        start_date,
        end_date,
        institute_id,
        created_by,
        published
    )
    VALUES
    (
        p_year,
        p_start_date,
        p_end_date,
        p_institute_id,
        p_created_by,
        p_published_state
    );

    SELECT p_year;
END;
//

DELIMITER ;
