DELIMITER //

DROP PROCEDURE IF EXISTS department__get_options;

CREATE PROCEDURE department__get_options (
 IN p_auth_user INT)
BEGIN
    SELECT 
        id, 
        name 
    FROM sow_department as dep
    INNER JOIN sow_department__has__teacher as dep_teach
		ON dep_teach.department_id = dep.id
    WHERE dep_teach.created_by = p_auth_user;
END;
//

DELIMITER ;
