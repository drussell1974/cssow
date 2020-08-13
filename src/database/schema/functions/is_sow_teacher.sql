DELIMITER //

DROP FUNCTION IF EXISTS is_sow_teacher;

CREATE FUNCTION is_sow_teacher (sowid INT, authid INT) RETURNS INT
BEGIN
    
    DECLARE is_teacher INT;
    SET is_teacher = 0;
    -- super users are omnipotent
    SET is_teacher = 
        (SELECT count(user.id)
         FROM auth_user AS user
         WHERE user.id = authid AND user.is_active = 1 AND user.is_superuser = 1);

    -- is the user as teacher of this this scheme of work
    
    IF is_teacher = 0 THEN
        SET is_teacher = 
            (SELECT count(teach.scheme_of_work_id)
             FROM auth_user AS user
             INNER JOIN sow_scheme_of_work__has__teacher AS teach ON user.id = teach.auth_user_id 
             WHERE user.is_active = 1 AND teach.scheme_of_work_id = sowid AND teach.auth_user_id = authid);
    END IF;

    RETURN is_teacher;
END; 
//

DELIMITER ;
