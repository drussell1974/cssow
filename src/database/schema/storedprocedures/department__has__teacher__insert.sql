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

DELETE FROM sow_department__has__teacher WHERE auth_user_id = 83;

CALL department__has__teacher__insert(83, 5, 0, 0, 0, 2);

SELECT * FROM sow_department__has__teacher WHERE auth_user_id = 83;