DELIMITER //

DROP PROCEDURE IF EXISTS keyword__get;

CREATE PROCEDURE keyword__get (
 IN p_keyword_id INT,
 IN p_scheme_of_work_id INT,
 IN p_auth_user INT)
BEGIN
    SELECT 
        id,
        name,
        definition,
        scheme_of_work_id
    FROM 
        sow_key_word
    WHERE
        id = p_keyword_id 
        AND scheme_of_work_id = p_scheme_of_work_id;
END;
//

DELIMITER ;