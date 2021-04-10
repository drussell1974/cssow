DELIMITER //

DROP PROCEDURE IF EXISTS academic_year_period__get_all;

CREATE PROCEDURE academic_year_period__get_all (
 IN p_department_id INT,
 IN p_academic_year INT,
 IN p_auth_user INT)
BEGIN
    SELECT 
        pd.time,
        pd.name
    FROM 
        sow_academic_year as yr
        INNER JOIN sow_academic_year_period as pd ON pd.academic_year = yr.year
    WHERE 
		yr.year = p_academic_year and yr.department_id = p_department_id
	ORDER BY
		yr.year, pd.time;
END;
//

DELIMITER ;

CALL academic_year_period__get_all(5, 2020, 2);