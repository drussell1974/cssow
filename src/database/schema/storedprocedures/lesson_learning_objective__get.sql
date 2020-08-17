DELIMITER //

DROP PROCEDURE IF EXISTS lesson_learning_objective__get;

CREATE PROCEDURE lesson_learning_objective__get (
 IN p_learning_objective_id INT,
 IN p_auth_user INT)
BEGIN
    SELECT 
        lob.id as id, 
        lob.description as description, 
        solo.id as solo_id, 
        solo.name as solo_taxonomy_name, 
        solo.lvl as solo_taxonomy_level, 
        cnt.id as content_id, cnt.description as content_description, 
        le.id as lesson_id, 
        sow.key_stage_id as key_stage_id, 
        ks.name as key_stage_name, 
        lob.key_words as key_words, 
        lob.notes as notes, 
        lob.group_name as group_name, 
        lob.created as created, 
        lob.created_by as created_by_id, 
        CONCAT_WS(' ', user.first_name, user.last_name) as created_by_name,  
        le_lo.published as published      
    FROM sow_scheme_of_work as sow 
        INNER JOIN sow_lesson as le ON le.scheme_of_work_id = sow.id
        INNER JOIN sow_learning_objective__has__lesson as le_lo ON le_lo.lesson_id = le.id
        INNER JOIN sow_learning_objective as lob ON lob.id = le_lo.learning_objective_id 
        LEFT JOIN sow_key_stage as ks ON ks.id = sow.key_stage_id 
        LEFT JOIN sow_solo_taxonomy as solo ON solo.id = lob.solo_taxonomy_id 
        LEFT JOIN sow_content as cnt ON cnt.id = lob.content_id 
        LEFT JOIN auth_user as user ON user.id = lob.created_by 
    WHERE lob.id = p_learning_objective_id
        AND (lob.published = 1
        or p_auth_user IN (SELECT auth_user_id 
                        FROM sow_teacher 
                        WHERE auth_user_id = p_auth_user AND scheme_of_work_id = sow.id)
        );
END;
//

DELIMITER ;