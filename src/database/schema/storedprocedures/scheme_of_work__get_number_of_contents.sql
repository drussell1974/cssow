DELIMITER //

DROP PROCEDURE IF EXISTS scheme_of_work__get_number_of_contents;

CREATE PROCEDURE scheme_of_work__get_number_of_contents (
 IN p_scheme_of_work_id INT,
 IN p_show_published_state INT,
 IN p_auth_user INT)
BEGIN
    SELECT count(cnt.id)
    FROM sow_content as cnt 
    WHERE cnt.scheme_of_work_id = p_scheme_of_work_id 
      AND (p_show_published_state % cnt.published = 0 
            or cnt.created_by = p_auth_user 
	);
END;

//

DELIMITER ;

CALL scheme_of_work__get_number_of_contents(11, 1, 2);