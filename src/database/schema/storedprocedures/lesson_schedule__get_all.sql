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