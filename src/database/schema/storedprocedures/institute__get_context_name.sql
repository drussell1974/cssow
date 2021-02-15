DELIMITER //

DROP PROCEDURE IF EXISTS institute__get_context_name;

CREATE PROCEDURE institute__get_context_name (
 IN p_institute_id INT,
 IN p_auth_user_id INT)
BEGIN
    SELECT 
      ins.name as institute_name
	FROM sow_institute as ins
	WHERE ins.id = p_institute_id
    LIMIT 1;
END;
//

DELIMITER ;

CALL institute__get_context_name(2,2);