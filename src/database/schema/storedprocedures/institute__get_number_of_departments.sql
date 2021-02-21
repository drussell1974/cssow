DELIMITER //

DROP PROCEDURE IF EXISTS institute__get_number_of_departments;

CREATE PROCEDURE institute__get_number_of_departments (
 IN p_institute_id INT,
 IN p_auth_user INT)
BEGIN
    SELECT 
        count(id)
    FROM 
        sow_department
    WHERE
		institute_id = p_institute_id and (
	    published = 1 or p_auth_user IN (SELECT auth_user_id 
                                FROM sow_teacher 
	 							WHERE auth_user_id = p_auth_user));
END;
//

DELIMITER ;