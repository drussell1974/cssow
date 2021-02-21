DELIMITER //

DROP PROCEDURE IF EXISTS scheme_of_work__get_latest;

CREATE PROCEDURE scheme_of_work__get_latest (
 IN p_top_n INT,
 IN p_department_id INT,
 IN p_institute_id INT,
 IN p_auth_user INT)
BEGIN
    SELECT DISTINCT
      sow.id as id, 
      sow.name as name, 
      sow.description as description, 
      sow.exam_board_id as 
      exam_board_id, 
      exam.name as exam_board_name, 
      sow.key_stage_id as key_stage_id, 
      kys.name as key_stage_name, 
      sow.created as created, 
      sow.created_by as created_by_id, 
      CONCAT_WS(' ', user.first_name, user.last_name) as created_by_name, 
      sow.published as published, 
      dep.id as department_id,
      dep.institute_id as institute_id
    FROM sow_scheme_of_work as sow 
    INNER JOIN sow_department as dep ON dep.id = sow.department_id
    LEFT JOIN sow_lesson as le ON le.scheme_of_work_id = sow.id 
    LEFT JOIN sow_learning_objective__has__lesson as lo_le ON lo_le.lesson_id = le.id 
    LEFT JOIN sow_exam_board as exam ON exam.id = sow.exam_board_id 
    LEFT JOIN sow_key_stage as kys ON kys.id = sow.key_stage_id  
    LEFT JOIN auth_user as user ON user.id = sow.created_by 
    WHERE sow.department_id = p_department_id AND sow.published = 1 
        or p_auth_user IN (SELECT auth_user_id 
                            FROM sow_teacher 
                            WHERE auth_user_id = p_auth_user AND scheme_of_work_id = sow.id)
    ORDER BY sow.created DESC LIMIT p_top_n;
END;
//

DELIMITER ;

#CALL scheme_of_work__get_latest(5, 2);