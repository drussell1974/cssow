DELIMITER //

DROP PROCEDURE IF EXISTS academic_year__get_all$2;

CREATE PROCEDURE academic_year__get_all$2 (
 IN p_institute_id INT,
 IN p_auth_user INT)
BEGIN
    SELECT 
		yr.year,
        yr.start_date,
        yr.end_date,
        yr.created_by
    FROM 
        sow_academic_year as yr
    WHERE 
		yr.institute_id = p_institute_id
	ORDER BY
		yr.start_date;
END;
//

DELIMITER ;

CALL academic_year__get_all$2(2, 2);

DELIMITER //

DROP PROCEDURE IF EXISTS academic_year__get_all;

CREATE PROCEDURE academic_year__get_all (
 IN p_institute_id INT,
 IN p_auth_user INT)
BEGIN
    SELECT 
        yr.start_date,
        yr.end_date
    FROM 
        sow_academic_year as yr
    WHERE 
		yr.institute_id = p_institute_id
	ORDER BY
		yr.start_date;
END;
//

DELIMITER ;

CALL academic_year__get_all(2, 2);