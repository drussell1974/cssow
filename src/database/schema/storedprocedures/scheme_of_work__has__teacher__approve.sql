DELIMITER //
        
DROP PROCEDURE IF EXISTS scheme_of_work__has__teacher_permission__approve$2;

CREATE PROCEDURE scheme_of_work__has__teacher_permission__approve$2 (
 IN p_department_id INT,
 IN p_scheme_of_work_id INT,
 IN p_teacher_id INT,
 IN p_join_code CHAR(8),
 IN p_department_permission INT,
 IN p_scheme_of_work_permission INT,
 IN p_lesson_permission INT, 
 IN p_auth_user INT
 )
BEGIN
	-- START TRANSACTION;

	/* DELETE OTHER JOIN CODE RELATED TO SCHEME OF WORK */
    
	DELETE FROM sow_teacher_join_code
    WHERE
		auth_user_id = p_teacher_id and
        join_code IN (SELECT join_code FROM sow_scheme_of_work__has__teacher WHERE scheme_of_work_id = p_scheme_of_work_id) and
        is_authorised = TRUE;
	
    /* approve the pending request */
    
	UPDATE sow_scheme_of_work__has__teacher
    SET
		department_permission = p_department_permission,
		scheme_of_work_permission = p_scheme_of_work_permission,
		lesson_permission = p_lesson_permission,
		modified_by = p_auth_user
	WHERE
		scheme_of_work_id = p_scheme_of_work_id and -- NOTE: select using scheme_of_work_id, as some old join_codes are duplicated across schemes_of_work
        join_code = p_join_code;
        
    /* Update permission for the department */
	
    UPDATE sow_department__has__teacher
	SET
		department_permission = p_department_permission,
		modified_by = p_auth_user
	WHERE
		department_id = p_department_id -- NOTE: select using department_id, as some old join_codes are duplicated across departments
        and join_code = p_join_code;
    
    /* Update current join code to be approved */
	
	UPDATE sow_teacher_join_code
    SET 
		is_authorised = TRUE
    WHERE
		auth_user_id = p_teacher_id and
		join_code = p_join_code;		
	
    -- COMMIT;
END;
//

DELIMITER ;

-- CALL scheme_of_work__has__teacher_permission__approve$2(5, 11, 30, 'T9OTDQSI', 1, 1, 2, 2);


DELIMITER //

DROP PROCEDURE IF EXISTS scheme_of_work__has__teacher_permission__approve;

CREATE PROCEDURE scheme_of_work__has__teacher_permission__approve (
 IN p_department_id INT,
 IN p_scheme_of_work_id INT,
 IN p_teacher_id INT,
 IN p_department_permission INT,
 IN p_scheme_of_work_permission INT,
 IN p_lesson_permission INT, 
 IN p_auth_user INT
 )
BEGIN
	START TRANSACTION;
    
	/* delete the current approved request (if it exists) */
	
    DELETE FROM sow_scheme_of_work__has__teacher 
    WHERE 
		scheme_of_work_id = p_scheme_of_work_id and
		auth_user_id = p_teacher_id and
        is_authorised = True;
    
    /* make the pending request approved */
    
	UPDATE sow_scheme_of_work__has__teacher 
	SET
		department_permission = p_department_permission,
		scheme_of_work_permission = p_scheme_of_work_permission,
		lesson_permission = p_lesson_permission,
		modified_by = p_auth_user,
        is_authorised = True
	WHERE
		scheme_of_work_id = p_scheme_of_work_id and
		auth_user_id = p_teacher_id and
        is_authorised = False;
	
    /* Update permission for the department */
	
    UPDATE sow_department__has__teacher 
	SET
		department_permission = p_department_permission,
		modified_by = p_auth_user
	WHERE
		department_id = p_department_id and
		auth_user_id = p_teacher_id;
	
    COMMIT;
END;
//

DELIMITER ;