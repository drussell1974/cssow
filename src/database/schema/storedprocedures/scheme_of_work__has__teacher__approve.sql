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

#CALL scheme_of_work__has__teacher_permission__update(11, 113, 1, 1, 1, 2, True);

DELIMITER ;