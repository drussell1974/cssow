DELIMITER //

DROP PROCEDURE IF EXISTS scheme_of_work__get_my;

CREATE PROCEDURE scheme_of_work__get_my (	
 IN p_department_id INT,
 IN p_institute_id INT,
 IN p_show_published_state INT,
 IN p_auth_user INT)
BEGIN
    SELECT DISTINCT
      sow.id as id, -- 0
      sow.name as name, -- 1
      sow.description as description, -- 2
      sow.exam_board_id as exam_board_id, -- 3
      exam.name as exam_board_name, -- 4
      sow.key_stage_id as key_stage_id, -- 5
      kys.name as key_stage_name, -- 6
      sow.created as created, -- 7
      sow.created_by as created_by_id, -- 8 
      CONCAT_WS(' ', user.first_name, user.last_name) as created_by_name, -- 9
      sow.published as published, -- 10
      dep.id as department_id, -- 11
	  dep.name as department_name, -- 12
      ins.id as institute_id, -- 13
      ins.name as institute_name -- 14
	FROM sow_scheme_of_work as sow 
		INNER JOIN sow_department as dep ON dep.id = sow.department_id
		INNER JOIN sow_institute as ins ON ins.id = dep.institute_id
		LEFT JOIN sow_lesson as le ON le.scheme_of_work_id = sow.id 
		LEFT JOIN sow_learning_objective__has__lesson as lo_le ON lo_le.lesson_id = le.id 
		LEFT JOIN sow_exam_board as exam ON exam.id = sow.exam_board_id 
		LEFT JOIN sow_key_stage as kys ON kys.id = sow.key_stage_id  
		LEFT JOIN auth_user as user ON user.id = sow.created_by 
    WHERE p_show_published_state % sow.published = 0
		and (sow.created_by = p_auth_user or dep.head_id = p_auth_user)
        and (dep.id = p_department_id or p_department_id = 0)
        and (ins.id = p_institute_id or p_institute_id = 0);
END;
//

DELIMITER ;