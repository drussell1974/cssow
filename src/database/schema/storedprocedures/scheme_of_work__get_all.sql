DELIMITER //

DROP PROCEDURE IF EXISTS scheme_of_work__get_all;

CREATE PROCEDURE scheme_of_work__get_all (
 IN p_key_stage_id INT,
 IN p_department_id INT,
 IN p_institute_id INT,
 IN p_show_published_state INT,
 IN p_auth_user INT)
BEGIN
    SELECT 
        sow.id as id,
        sow.name as name,
        sow.description as description,
        sow.exam_board_id as exam_board_id,
        exam.name as exam_board_name,
        sow.key_stage_id as key_stage_id,
        kys.name as key_stage_name,
        dep.id as department_id,
        dep.name as department_name,
        sow.created as created,
        sow.created_by as created_by_id,
        user.first_name as created_by_name,
        sow.published as published
    FROM sow_scheme_of_work as sow
        INNER JOIN sow_department as dep ON dep.id = sow.department_id	
        LEFT JOIN sow_exam_board as exam ON exam.id = sow.exam_board_id
        INNER JOIN sow_key_stage as kys ON kys.id = sow.key_stage_id
        INNER JOIN auth_user as user ON user.id = sow.created_by
    WHERE 
		sow.department_id = p_department_id 
		AND (sow.key_stage_id = p_key_stage_id or p_key_stage_id = 0)
        AND (p_show_published_state % sow.published = 0 #323 use p_show_published_state and remove subquery 
			or sow.created_by = p_auth_user)
    ORDER BY sow.key_stage_id;
END;
//

DELIMITER ;

CALL scheme_of_work__get_all(0,5,2,2,1);