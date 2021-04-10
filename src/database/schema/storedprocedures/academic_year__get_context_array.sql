DELIMITER //

DROP PROCEDURE IF EXISTS academic_year__get_context_array;

CREATE PROCEDURE academic_year__get_context_array (
 IN p_department_id INT)
BEGIN
    SELECT 
		yr.year,
        yr.start_date,
        yr.end_date,
        yr.created_by,
        1 as published
    FROM 
        sow_academic_year as yr
    WHERE 
		yr.department_id = p_department_id
	ORDER BY
		yr.year;
END;
//

DELIMITER ;

CALL academic_year__get_context_array(5);