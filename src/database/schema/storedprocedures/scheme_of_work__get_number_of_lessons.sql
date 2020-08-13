DELIMITER //

DROP PROCEDURE IF EXISTS scheme_of_work__get_number_of_lessons;

CREATE PROCEDURE scheme_of_work__get_number_of_lessons (
  IN scheme_of_work_id INT,
  IN auth_user INT)
BEGIN
    SELECT count(les.id)
    FROM sow_lesson as les
    WHERE les.scheme_of_work_id = scheme_of_work_id AND (les.published = 1 or is_sow_teacher(les.scheme_of_work_id, auth_user) > 0);
END;

//

DELIMITER ;