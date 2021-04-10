DELIMITER //

DROP PROCEDURE IF EXISTS academic_year__get_all;

CREATE PROCEDURE academic_year__get_all (
 IN p_department_id INT,
 IN p_auth_user INT)
BEGIN
    SELECT 
        yr.start_date,
        yr.end_date
    FROM 
        sow_academic_year as yr
    WHERE 
		yr.department_id = p_department_id
	ORDER BY
		yr.start_date;
END;
//

DELIMITER ;

CALL academic_year__get_all(5, 2);