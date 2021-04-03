DELIMITER //

DROP PROCEDURE IF EXISTS `lesson_schedule__get_all`;

CREATE PROCEDURE `lesson_schedule__get_all` 
(
 IN p_lesson_id INT,
 IN p_published_state INT,
 IN p_auth_user INT
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
    WHERE id = p_lesson_id;
END;

// DELIMITER ;