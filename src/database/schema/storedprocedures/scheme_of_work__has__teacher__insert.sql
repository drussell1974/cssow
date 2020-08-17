DELIMITER //

DROP PROCEDURE IF EXISTS scheme_of_work__has__teacher__insert;

CREATE PROCEDURE scheme_of_work__has__teacher__insert (
 IN p_scheme_of_work_id INT,
 IN p_auth_user INT)
BEGIN
  INSERT INTO sow_scheme_of_work__has__teacher
    (scheme_of_work_id, auth_user_id)
  VALUES
    (p_scheme_of_work_id, p_auth_user);
END;
//

DELIMITER ;