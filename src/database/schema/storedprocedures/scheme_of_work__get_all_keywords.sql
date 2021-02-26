DELIMITER $$

DROP PROCEDURE IF EXISTS scheme_of_work__get_all_keywords;

CREATE PROCEDURE `scheme_of_work__get_all_keywords`(
 IN p_scheme_of_work_id INT,
 IN p_show_published_state INT,
 IN p_auth_user INT)
BEGIN
      SELECT 
            kw.id as id, 
            kw.name as term, 
            kw.definition as definition, 
            kw.scheme_of_work_id as scheme_of_work_id,
            kw.published as published,
            kw.created as created
      FROM sow_key_word kw
      WHERE 
            kw.scheme_of_work_id = p_scheme_of_work_id
            AND (p_show_published_state % published = 0 
                  or kw.created_by = p_auth_user
			  )
      ORDER BY kw.name;
END$$
DELIMITER ;
