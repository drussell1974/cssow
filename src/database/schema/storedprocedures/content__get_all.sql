DELIMITER //

DROP PROCEDURE IF EXISTS content__get_all;

CREATE PROCEDURE content__get_all (
 IN p_scheme_of_work_id INT,
 IN p_key_stage_id INT,
 IN p_auth_user INT)
BEGIN
    SELECT 
        id as id, 
        description as description, 
        letter as letter_prefix, 
        published as published 
    FROM sow_content 
    WHERE
        key_stage_id = p_key_stage_id 
        AND (published = 1 or
             p_auth_user IN 
                    (SELECT auth_user_id 
                    FROM sow_teacher 
                    WHERE scheme_of_work_id = p_scheme_of_work_id)
        )
    ORDER BY letter ASC;
END;
//

DELIMITER ;