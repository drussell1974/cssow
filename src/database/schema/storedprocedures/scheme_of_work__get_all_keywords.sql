DELIMITER //

DROP PROCEDURE IF EXISTS scheme_of_work__get_all_keywords;

CREATE PROCEDURE scheme_of_work__get_all_keywords (
 IN p_scheme_of_work_id INT,
 IN p_auth_user INT)
BEGIN
      SELECT 
            kw.id as id, 
            kw.name as term, 
            kw.definition as definition,
            kw.scheme_of_work_id as scheme_of_work_id,
            kw.published as published
      FROM sow_key_word kw
      WHERE 
            kw.scheme_of_work_id = p_scheme_of_work_id
            AND (published = 1 
                  or p_auth_user IN (SELECT auth_user_id 
                                     FROM sow_teacher 
                                     WHERE auth_user_id = p_auth_user AND scheme_of_work_id = kw.scheme_of_work_id))
      ORDER BY kw.name;
END;

//

DELIMITER ;