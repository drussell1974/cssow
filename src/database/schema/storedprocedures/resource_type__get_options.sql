DELIMITER //

DROP PROCEDURE IF EXISTS resource_type__get_options;

CREATE PROCEDURE resource_type__get_options (
 IN p_auth_user INT)
BEGIN
    SELECT
        type.id as id,
        type.name as name
    FROM
        sow_resource_type as type
    WHERE
        type.published = 1 OR type.created_by = p_auth_user;
END;
//

DELIMITER ;