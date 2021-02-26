DELIMITER //

DROP PROCEDURE IF EXISTS scheme_of_work__get_number_of_lessons;

CREATE PROCEDURE scheme_of_work__get_number_of_lessons (
 IN p_scheme_of_work_id INT,
 IN p_show_published_state INT,
 IN p_auth_user INT)
BEGIN
    SELECT count(les.id)
    FROM sow_lesson as les 
    WHERE les.scheme_of_work_id = p_scheme_of_work_id 
      AND (p_show_published_state % les.published = 0 
            or les.created_by = p_auth_user 
	);
END;

//

DELIMITER ;