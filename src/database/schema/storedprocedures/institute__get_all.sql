DELIMITER //

DROP PROCEDURE IF EXISTS institute__get_all;

CREATE PROCEDURE institute__get_all (
 IN p_show_published_state INT,
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
	    p_show_published_state % published = 0 
        or ins.created_by = p_auth_user
    ORDER BY ins.name;
END;
//

DELIMITER ;

CALL institute__get_all(2, 1);