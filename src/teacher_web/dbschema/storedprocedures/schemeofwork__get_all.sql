DELIMITER //

CREATE OR REPLACE PROCEDURE schemeofwork__get_all (
  IN key_stage_id INT,
  IN auth_user INT)
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
        sow.published as published,
        COUNT(les.id) as number_of_lessons
    FROM sow_scheme_of_work as sow
        LEFT JOIN sow_lesson as les ON les.scheme_of_work_id = sow.id
        LEFT JOIN sow_exam_board as exam ON exam.id = sow.exam_board_id
        INNER JOIN sow_key_stage as kys ON kys.id = sow.key_stage_id
        LEFT JOIN auth_user as user ON user.id = sow.created_by
    WHERE (sow.key_stage_id = key_stage_id or key_stage_id = 0) AND (sow.published = 1 OR sow.created_by = auth_user)
    GROUP BY id, name, description, exam_board_id, exam_board_name, key_stage_id, key_stage_name, created, created_by_id, created_by_name, published
    ORDER BY sow.key_stage_id;
END;
//

DELIMITER ;