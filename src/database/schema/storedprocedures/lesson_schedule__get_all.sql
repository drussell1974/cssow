DELIMITER //

DROP PROCEDURE IF EXISTS `lesson_schedule__get_all$2`;

CREATE PROCEDURE `lesson_schedule__get_all$2` 
(
 IN p_lesson_id INT,
 IN p_from_date DATETIME,
 IN p_to_date DATETIME,
 IN p_show_published_state INT,
 IN p_auth_user_id INT
 )
BEGIN
	SELECT 
		sch.id as id,
        lsn.title as title,
		sch.class_name as class_name,
		sch.class_code as class_code,
        sch.start_date as start_date,
        sch.lesson_id as lesson_id,
        sch.scheme_of_work_id as scheme_of_work_id,
        sch.published as published,
        sch.created_by as created_by
    FROM sow_lesson_schedule as sch
    INNER JOIN sow_lesson as lsn ON lsn.id = sch.lesson_id
    WHERE (lsn.id = p_lesson_id or p_lesson_id = 0)
		AND sch.start_date BETWEEN p_from_date and p_to_date
        AND (p_show_published_state % sch.published = 0 or sch.created_by = p_auth_user_id)
    ORDER BY sch.start_date;
END;

// DELIMITER ;
CALL lesson_schedule__get_all$2(0, '1700-04-04 00:00:00', '2121-12-31 23:59:59', 4, 2);

DELIMITER //

DROP PROCEDURE IF EXISTS `lesson_schedule__get_all`;

CREATE PROCEDURE `lesson_schedule__get_all` 
(
 IN p_lesson_id INT,
 IN p_from_date DATETIME,
 IN p_to_date DATETIME,
 IN p_show_published_state INT,
 IN p_auth_user_id INT
 )
BEGIN
	SELECT 
		id as id,
		class_name as class_name,
		class_code as class_code,
        start_date as start_date,
        lesson_id as lesson_id,
        scheme_of_work_id as scheme_of_work_id,
        published as published,
        created_by as created_by
    FROM sow_lesson_schedule
    WHERE lesson_id = p_lesson_id
		AND start_date BETWEEN p_from_date and p_to_date
        AND (p_show_published_state % published = 0 or created_by = p_auth_user_id)
    ORDER BY start_date;
END;

// DELIMITER ;
CALL lesson_schedule__get_all(131, '2021-04-04 00:00:00', '2121-04-04 00:00:00', 4, 2);