DELIMITER //

DROP PROCEDURE IF EXISTS content__get;

CREATE PROCEDURE content__get (
 IN p_content_id INT,
 IN p_scheme_of_work_id INT,
 IN p_auth_user INT)
BEGIN

    SELECT 
        id as id, 
        description as description, 
        letter as letter_prefix, 
        published as published 
    FROM sow_content 
    WHERE
        id = p_content_id 
        AND (published = 1 or
             p_auth_user IN 
                    (SELECT auth_user_id 
                    FROM sow_teacher 
                    WHERE scheme_of_work_id = p_scheme_of_work_id)
        );
END;
//

DELIMITER ;