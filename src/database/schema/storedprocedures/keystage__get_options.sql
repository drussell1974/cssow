DELIMITER //

DROP PROCEDURE IF EXISTS keystage__get_options$2;

CREATE PROCEDURE `keystage__get_options$2`(
 IN p_department_id INT,
 IN p_show_published_state INT,
 IN p_auth_user INT)
BEGIN
    SELECT 
        id,
        name 
    FROM 
        sow_key_stage
	WHERE
		department_id = p_department_id 
        AND (
			p_show_published_state % published = 0
			or created_by = p_auth_user);
END$$
DELIMITER ;

DELIMITER //

DROP PROCEDURE IF EXISTS keystage__get_options;

CREATE PROCEDURE keystage__get_options (
 IN p_show_published_state INT,
 IN p_auth_user INT)
BEGIN
    SELECT 
        id,
        name 
    FROM 
        sow_key_stage
	WHERE p_show_published_state % published = 0
		or created_by = p_auth_user;
END;
//

DELIMITER ;
