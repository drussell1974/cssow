DELIMITER //

DROP PROCEDURE IF EXISTS `lesson_schedule__insert$2`;

CREATE PROCEDURE `lesson_schedule__insert$2` 
(OUT p_lesson_schedule_id INT,
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
	 INSERT INTO sow_lesson_schedule
     (
		start_date,
		class_code,
        class_name,
        institute_id,
        department_id,
        scheme_of_work_id,
        lesson_id,
        published,
        created_by
     )
     VALUES
     (
		p_start_date,
		p_class_code,
        p_class_name,
        p_institute_id,
        p_department_id,
        p_scheme_of_work_id,
        p_lesson_id,
        p_published_state,
        p_auth_user
     );
     
     SET p_lesson_schedule_id = LAST_INSERT_ID();
     SELECT p_lesson_schedule_id;
END;
//

DELIMITER ;

DELIMITER //

DROP PROCEDURE IF EXISTS `lesson_schedule__insert`;

CREATE PROCEDURE `lesson_schedule__insert` 
(OUT p_lesson_schedule_id INT,
 IN p_class_code CHAR(6),
 IN p_institute_id INT,
 IN p_department_id INT,
 IN p_scheme_of_work_id INT,
 IN p_lesson_id INT,
 IN p_published_state INT,
 IN p_auth_user INT
 )
BEGIN
	 INSERT INTO sow_lesson_schedule
     (
		class_code,
        institute_id,
        department_id,
        scheme_of_work_id,
        lesson_id,
        published,
        created_by
     )
     VALUES
     (
		p_class_code,
        p_institute_id,
        p_department_id,
        p_scheme_of_work_id,
        p_lesson_id,
        p_published_state,
        p_auth_user
     );
     
     SET p_lesson_schedule_id = LAST_INSERT_ID();
     SELECT p_lesson_schedule_id;
END;
//

DELIMITER ;