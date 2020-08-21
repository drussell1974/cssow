DELIMITER //

DROP PROCEDURE IF EXISTS solotaxonomy__get_options;

CREATE PROCEDURE solotaxonomy__get_options (
 IN p_auth_user INT)
BEGIN
    SELECT 
        id, 
        name, 
        lvl 
    FROM
        sow_solo_taxonomy;
END;
//

DELIMITER ;