DELIMITER //

DROP PROCEDURE IF EXISTS `lesson_schedule__get$2`;

CREATE PROCEDURE `lesson_schedule__get$2` 
(
 IN p_schedule_id INT,
 IN p_show_published_state INT,
 IN p_auth_user_id INT
 )
BEGIN
	SELECT 
		class_name as class_name,
		class_code as class_code,
        start_date as start_date,
        lesson_id as lesson_id,
        scheme_of_work_id as scheme_of_work_id,
        published as published,
        created_by as created_by
    FROM sow_lesson_schedule
    WHERE id = p_schedule_id AND (p_show_published_state % published = 0 or created_by = p_auth_user_id);
END;

// DELIMITER ;

DELIMITER //

DROP PROCEDURE IF EXISTS `lesson_schedule__get`;

CREATE PROCEDURE `lesson_schedule__get` 
(IN p_lesson_id INT,
 IN p_published_state INT,
 IN p_auth_user INT
 )
BEGIN
	SELECT 
		id as id,
		class_code as class_code,
        institute_id as institute_id,
        department_id as department_id,
        scheme_of_work_id as scheme_of_work_id,
        lesson_id as lesson_id,
        published as published,
        created_by as created_by
    FROM sow_lesson_schedule
    WHERE lesson_id = p_lesson_id;
END;

// DELIMITER ;