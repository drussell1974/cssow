DELIMITER //

DROP PROCEDURE IF EXISTS scheme_of_work__has__teacher_permission__delete;

CREATE PROCEDURE scheme_of_work__has__teacher_permission__delete (
 IN p_scheme_of_work_id INT,
 IN p_teacher_id INT,
 IN p_auth_user_id INT)
BEGIN
    DELETE FROM sow_scheme_of_work__has__teacher 
    WHERE
		scheme_of_work_id = p_scheme_of_work_id AND
		auth_user_id = p_teacher_id; -- assumes the auth_user (TODO: change column name to teacher_id)
END;
//

DELIMITER ;