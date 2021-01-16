DELIMITER //

DROP PROCEDURE IF EXISTS scheme_of_work__has__teacher__insert;

CREATE PROCEDURE scheme_of_work__has__teacher__insert (
 IN p_scheme_of_work_id INT,
 IN p_auth_user INT,
 IN p_department_permission INT,
 IN p_scheme_of_work_permission INT,
 IN p_lesson_permission INT)
BEGIN
  INSERT INTO sow_scheme_of_work__has__teacher
    (scheme_of_work_id, auth_user_id, department_permission, scheme_of_work_permission, lesson_permission)
  VALUES
    (p_scheme_of_work_id, p_auth_user, p_department_permission, p_scheme_of_work_permission, p_lesson_permission);
END;
//

DELIMITER ;