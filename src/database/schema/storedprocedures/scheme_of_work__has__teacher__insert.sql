DELIMITER //

DROP PROCEDURE IF EXISTS scheme_of_work__has__teacher_permission__insert$2;
-- CALL scheme_of_work__has__teacher_permission__insert$2(30, 11, 'PB6A46XS', 1, 4, 1, 30, False);
CREATE PROCEDURE scheme_of_work__has__teacher_permission__insert$2 (
 IN p_teacher_id INT,
 IN p_scheme_of_work_id INT,
 IN p_join_code CHAR(8),
 IN p_department_permission INT,
 IN p_scheme_of_work_permission INT,
 IN p_lesson_permission INT, 
 IN p_auth_user INT,
 IN p_is_authorised BOOLEAN
 )
BEGIN
	-- TODO: pass as parameter to allow pending join request 

	DECLARE p_email VARCHAR(254);
	
	SET p_email = (SELECT email FROM auth_user WHERE id = p_teacher_id LIMIT 1);
    
	INSERT IGNORE INTO sow_teacher_join_code (join_code, email, auth_user_id, is_authorised) VALUES (p_join_code, p_email, p_teacher_id, p_is_authorised);

	INSERT IGNORE INTO sow_scheme_of_work__has__teacher 
	(
		scheme_of_work_id,
		-- auth_user_id, -- assumes the auth_user (TODO: change column name to teacher_id)
        join_code,
        email,
		department_permission,
		scheme_of_work_permission,
		lesson_permission,
        -- is_authorised,
        created_by
	)
	VALUES 
	(
		p_scheme_of_work_id,
		-- p_teacher_id,
        p_join_code,
        p_email,
		p_department_permission,
		p_scheme_of_work_permission,
		p_lesson_permission,
        -- p_is_authorised,
        p_auth_user
	);
    
    -- UPDATE sow_scheme_of_work__has__teacher
	/*UPDATE sow_scheme_of_work__has__teacher as sow_teach
    INNER JOIN sow_teacher_join_code as teach_join ON teach_join.join_code = sow_teach.join_code
    SET 
        department_permission = p_department_permission,
        scheme_of_work_permission = p_scheme_of_work_permission,
        lesson_permission = p_lesson_permission
    WHERE
		sow_teach.scheme_of_work_id = p_scheme_of_work_id
        and teach_join.auth_user_id = p_teacher_id;*/
END;
//

CALL scheme_of_work__has__teacher_permission__insert$2(11, 30, '4QWGF98O', 1, 4, 1, 30, False);

DELIMITER ;

DELIMITER //

DROP PROCEDURE IF EXISTS scheme_of_work__has__teacher_permission__insert;

CREATE PROCEDURE scheme_of_work__has__teacher_permission__insert (
 IN p_scheme_of_work_id INT,
 IN p_teacher_id INT,
 IN p_department_permission INT,
 IN p_scheme_of_work_permission INT,
 IN p_lesson_permission INT, 
 IN p_auth_user INT,
 IN p_is_authorised BOOLEAN
 )
BEGIN
	INSERT IGNORE INTO sow_scheme_of_work__has__teacher 
	(
		scheme_of_work_id,
		auth_user_id, -- assumes the auth_user (TODO: change column name to teacher_id)
		department_permission,
		scheme_of_work_permission,
		lesson_permission,
        is_authorised,
        created_by
	)
	VALUES 
	(
		p_scheme_of_work_id,
		p_teacher_id,
		p_department_permission,
		p_scheme_of_work_permission,
		p_lesson_permission,
        p_is_authorised,
        p_auth_user
	);
END;
//

DELIMITER ;
