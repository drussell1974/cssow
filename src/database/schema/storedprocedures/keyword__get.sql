DELIMITER //

DROP PROCEDURE IF EXISTS keyword__get;

CREATE PROCEDURE keyword__get (
 IN p_keyword_id INT,
 IN p_scheme_of_work_id INT,
 IN p_show_published_state INT,
 IN p_auth_user INT)
BEGIN
    SELECT 
        id as id,
        name as term,
        kw.definition as definition,
        kw.scheme_of_work_id as scheme_of_work_id,
        kw.published as published,
        kw.created as created
    FROM 
        sow_key_word as kw
    WHERE
        kw.id = p_keyword_id 
        AND kw.scheme_of_work_id = p_scheme_of_work_id
        AND (p_show_published_state % kw.published = 0
			or kw.created_by = p_auth_user)
	ORDER BY kw.name;
END;
//

DELIMITER ;