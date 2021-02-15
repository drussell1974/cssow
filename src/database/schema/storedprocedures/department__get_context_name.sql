DELIMITER //

DROP PROCEDURE IF EXISTS department__get_context_name;

CREATE PROCEDURE department__get_context_name (
 IN p_department_id INT,
 IN p_institute_id INT,
 IN p_auth_user_id INT)
BEGIN
    SELECT 
      dep.name as department_name
	FROM sow_department as dep
	WHERE dep.id = p_department_id and dep.institute_id = p_institute_id
    LIMIT 1;
END;
//

DELIMITER ;

CALL department__get_context_name(1,5,2);