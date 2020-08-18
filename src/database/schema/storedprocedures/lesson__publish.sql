DELIMITER //

DROP PROCEDURE IF EXISTS lesson__publish;

CREATE PROCEDURE lesson__publish (
 IN p_lesson_id INT,
 IN p_published INT,
 IN p_auth_user INT)
BEGIN

    UPDATE sow_lesson 
    SET 
        published = p_published
    WHERE 
        id =  p_lesson_id 
            AND p_auth_user 
                IN (SELECT auth_user_id 
                    FROM sow_teacher 
                    WHERE auth_user_id = p_auth_user AND scheme_of_work_id = scheme_of_work_id);
END;
//

DELIMITER ;