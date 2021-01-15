DELIMITER //

DROP PROCEDURE IF EXISTS department__has__teacher__insert;

CREATE PROCEDURE department__has__teacher__insert (
 IN p_department_id INT,
 IN p_head_id INT)
BEGIN
  INSERT INTO sow_teacher__has__department
    (department_id, head_id)
  VALUES
    (p_department_id, p_head_id);
END;
//

DELIMITER ;