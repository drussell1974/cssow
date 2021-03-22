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