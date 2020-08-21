DELIMITER //

DROP PROCEDURE IF EXISTS scheme_of_work__get;

CREATE PROCEDURE scheme_of_work__get (
 IN p_scheme_of_work_id INT,
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
        sow.created as created,
        sow.created_by as created_by_id,
        CONCAT_WS(' ', user.first_name, user.last_name) as created_by_name,
        sow.published as published 
    FROM sow_scheme_of_work as sow  
        LEFT JOIN sow_exam_board as exam ON exam.id = sow.exam_board_id
        INNER JOIN sow_key_stage as kys ON kys.id = sow.key_stage_id
        INNER JOIN auth_user as user ON user.id = sow.created_by   
    WHERE sow.id = p_scheme_of_work_id 
        AND (sow.published = 1 
                or p_auth_user IN (SELECT auth_user_id 
                                FROM sow_teacher 
                                WHERE auth_user_id = p_auth_user AND scheme_of_work_id = sow.id)
        );
END;
//

DELIMITER ;