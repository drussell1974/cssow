DELIMITER //

DROP PROCEDURE IF EXISTS institute__get;

CREATE PROCEDURE institute__get (
 IN p_institute_id INT,
 IN p_auth_user INT)
BEGIN
    SELECT 
        ins.id as id,
        ins.name as name,
        ins.created as created,
        ins.created_by as created_by,
        usr.first_name as created_by_name,
        ins.published as published
    FROM 
        sow_institute as ins
        INNER JOIN auth_user as usr ON usr.id = ins.created_by
    WHERE
        ins.id = p_institute_id;
	-- ORDER BY ins.name;
END;
//

DELIMITER ;

CALL institute__get(2,2);