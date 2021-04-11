DELIMITER //

DROP PROCEDURE IF EXISTS academic_year__get_model;

CREATE PROCEDURE academic_year__get_model (
 IN p_institute_id INT,
 IN p_selected_year INT,
 IN p_auth_user INT)
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
		yr.institute_id = p_institute_id
        AND yr.year = p_selected_year
	ORDER BY
		yr.year;
END;
//

DELIMITER ;
