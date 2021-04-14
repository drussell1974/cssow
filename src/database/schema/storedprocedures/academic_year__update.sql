DELIMITER //

DROP PROCEDURE IF EXISTS academic_year__update;

CREATE PROCEDURE academic_year__update (
    -- OUT p_department_id INT,
    IN p_year INT,
    IN p_start_date datetime,
    IN p_end_date datetime,
    IN p_institute_id INT,
	IN p_published_state INT,
    IN p_created_by INT)
BEGIN
    -- CHECK sow_department
    UPDATE sow_academic_year 
    SET
        year = p_year, 
        institute_id = p_institute_id,
        start_date = p_start_date,
        end_date = p_end_date,
        created_by = p_created_by,
        published = p_published_state
    WHERE year = p_year and institute_id = p_institute_id;

    SELECT p_year;
END;
//

DELIMITER ;
