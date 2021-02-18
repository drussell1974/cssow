DELIMITER //

DROP PROCEDURE IF EXISTS scheme_of_work__update;

CREATE PROCEDURE scheme_of_work__update (
 IN p_scheme_of_work_id INT,
 IN p_name VARCHAR(40),
 IN p_description TEXT,
 IN p_exam_board_id INT,
 IN p_key_stage_id INT,
 IN p_department_id INT,
 IN p_published INT,
 IN p_auth_user INT)
BEGIN
    UPDATE sow_scheme_of_work 
    SET 
        name = p_name,
        description = p_description, 
        exam_board_id = p_exam_board_id,
        key_stage_id = p_key_stage_id, 
        department_id = p_department_id,
        published = p_published,
        modified_by = p_auth_user
    WHERE id =  p_scheme_of_work_id 
        AND p_auth_user IN (SELECT auth_user_id 
                            FROM sow_teacher 
                            WHERE auth_user_id = p_auth_user AND scheme_of_work_id = p_scheme_of_work_id);
END;
//

DELIMITER ;

