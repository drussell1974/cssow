DELIMITER $$

DROP PROCEDURE IF EXISTS `lesson_schedule__update$2`;

CREATE PROCEDURE `lesson_schedule__update$2`
(IN p_lesson_schedule_id INT,
 IN p_start_date DATETIME,
 IN p_class_code CHAR(6),
 IN p_class_name VARCHAR(10),
 IN p_institute_id INT,
 IN p_department_id INT,
 IN p_scheme_of_work_id INT,
 IN p_lesson_id INT,
 IN p_published_state INT,
 IN p_auth_user INT
 )
BEGIN
	 UPDATE sow_lesson_schedule
     SET 
		start_date = p_start_date,
		class_code = p_class_code,
        class_name = p_class_name,
        institute_id = p_institute_id,
        department_id = p_department_id,
        scheme_of_work_id = p_scheme_of_work_id,
        lesson_id = p_lesson_id,
        modified_by = p_auth_user
     WHERE id = p_lesson_schedule_id;
END$$
DELIMITER ;


DELIMITER //

/*
DELIMITER //

DROP PROCEDURE IF EXISTS `lesson_schedule__update`;

CREATE PROCEDURE `lesson_schedule__update` 
(IN p_lesson_schedule_id INT,
 IN p_class_code CHAR(6),
 IN p_institute_id INT,
 IN p_department_id INT,
 IN p_scheme_of_work_id INT,
 IN p_lesson_id INT,
 IN p_published_state INT,
 IN p_auth_user INT
 )
BEGIN
	 UPDATE sow_lesson_schedule
     SET 
		class_code = p_class_code,
        institute_id = p_institute_id,
        department_id = p_department_id,
        scheme_of_work_id = p_scheme_of_work_id,
        lesson_id = p_lesson_id,
        modified_by = p_auth_user
     WHERE id = p_lesson_schedule_id;
END;

DELIMITER ; */