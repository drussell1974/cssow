DELIMITER //

DROP PROCEDURE IF EXISTS department__has__teacher__insert$2;

CREATE PROCEDURE department__has__teacher__insert$2 (
 IN p_teacher_id INT,
 IN p_department_id INT,
 IN p_join_code CHAR(8),
 IN p_department_permission INT,
 IN p_scheme_of_work_permission INT,
 IN p_lesson_permission INT,
 IN p_created_by INT
)
BEGIN
	DECLARE p_email VARCHAR(254);
	
	SET p_email = (SELECT username FROM auth_user WHERE id = p_teacher_id LIMIT 1);
    
	INSERT IGNORE INTO sow_teacher_join_code (join_code, email, auth_user_id, is_authorised) VALUES (p_join_code, p_email, p_teacher_id, False);
    
    INSERT IGNORE INTO sow_department__has__teacher
    (	
		-- auth_user_id, 
		join_code,
        email,
        department_id, 
		department_permission, 
		scheme_of_work_permission, 
		lesson_permission, 
		created_by
	)
	VALUES
	(
		p_join_code,
		-- p_teacher_id, 
		p_email,
        p_department_id, 
        p_department_permission, -- IF (p_department_permission > 1, p_department_permission, department_permission), 
        p_scheme_of_work_permission, -- IF (p_scheme_of_work_permission > 1, p_scheme_of_work_permission, scheme_of_work_permission), 
        p_lesson_permission, -- IF (p_lesson_permission > 1, p_lesson_permission, lesson_permission), 
        p_created_by
	);
    
    -- UPDATE sow_department__has__teacher
	/*UPDATE sow_department__has__teacher as dep_teach
    INNER JOIN sow_teacher_join_code as teach_join ON teach_join.join_code = dep_teach.join_code
    SET 
        department_permission = p_department_permission,
        scheme_of_work_permission = p_scheme_of_work_permission,
        lesson_permission = p_lesson_permission
    WHERE
		dep_teach.department_id = p_department_id
        and teach_join.auth_user_id = p_teacher_id;*/
END;
//

DELIMITER ;
    
DELIMITER //

DROP PROCEDURE IF EXISTS department__has__teacher__insert;

CREATE PROCEDURE department__has__teacher__insert (
 IN p_teacher_id INT,
 IN p_department_id INT,
 IN p_department_permission INT,
 IN p_scheme_of_work_permission INT,
 IN p_lesson_permission INT,
 IN p_created_by INT
)
BEGIN

  INSERT IGNORE INTO sow_department__has__teacher
    (	
		auth_user_id, 
		department_id, 
		department_permission, 
		scheme_of_work_permission, 
		lesson_permission, 
		created_by
	)
  VALUES
	(
		p_teacher_id, 
		p_department_id, 
        p_department_permission, -- IF (p_department_permission > 1, p_department_permission, department_permission), 
        p_scheme_of_work_permission, -- IF (p_scheme_of_work_permission > 1, p_scheme_of_work_permission, scheme_of_work_permission), 
        p_lesson_permission, -- IF (p_lesson_permission > 1, p_lesson_permission, lesson_permission), 
        p_created_by
	);
END;
//

DELIMITER ;