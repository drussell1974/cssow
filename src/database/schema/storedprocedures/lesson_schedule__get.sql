DELIMITER //

DROP PROCEDURE IF EXISTS `lesson_schedule__get`;

CREATE PROCEDURE `lesson_schedule__get` 
(IN p_lesson_schedule_id INT,
 IN p_published_state INT,
 IN p_auth_user INT
 )
BEGIN
	SELECT 
		class_code = p_class_code,
        institute_id = p_institute_id,
        department_id = p_department_id,
        scheme_of_work_id = p_scheme_of_work_id,
        lesson_id = p_lesson_id,
        modified_by = p_auth_user
    FROM sow_lesson_schedule
    WHERE id = p_lesson_schedule_id;
END;

// DELIMITER ;