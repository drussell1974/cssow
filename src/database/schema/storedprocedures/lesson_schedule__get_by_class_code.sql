DELIMITER //

DROP PROCEDURE IF EXISTS lesson_schedule__get_by_class_code$2;

CREATE PROCEDURE lesson_schedule__get_by_class_code$2 (
 IN p_class_code CHAR(6),
 IN p_show_published_state INT,
 IN p_auth_user_id INT)
BEGIN
	SELECT 
		sch.class_name as class_name,
		sch.id as id,
		sch.start_date as start_date,
        sch.lesson_id as lesson_id,
        sch.scheme_of_work_id as scheme_of_work_id,
        sch.published as published,
        sch.created_by as created_by
    FROM sow_lesson_schedule as sch
    WHERE class_code = p_class_code
        AND (p_show_published_state % sch.published = 0 or sch.created_by = p_auth_user_id);
END;

// DELIMITER ;

DELIMITER //

DROP PROCEDURE IF EXISTS lesson_schedule__get_by_class_code;

CREATE PROCEDURE lesson_schedule__get_by_class_code (
 IN p_class_code CHAR(6),
 IN p_show_published_state INT,
 IN p_auth_user_id INT)
BEGIN
	SELECT 
		sch.id as id,
		sch.class_code as class_code,
        -- les.title as title,
        -- les.summary as summary,
        sch.institute_id as institute_id,
        sch.department_id as department_id,
        sch.scheme_of_work_id as scheme_of_work_id,
        sch.lesson_id as lesson_id,
        sch.published as published,
        sch.created_by as created_by
    FROM sow_lesson_schedule as sch
    -- INNER JOIN sow_lesson as les ON les.id = sch.lesson_id
    WHERE class_code = p_class_code
        AND (p_show_published_state % sch.published = 0 or sch.created_by = p_auth_user_id);
END;

// DELIMITER ;