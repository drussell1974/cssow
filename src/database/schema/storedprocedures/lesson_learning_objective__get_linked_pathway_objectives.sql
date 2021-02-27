DELIMITER //

DROP PROCEDURE IF EXISTS lesson_learning_objective__get_linked_pathway_objectives;

CREATE PROCEDURE lesson_learning_objective__get_linked_pathway_objectives (
 IN p_lesson_id INT,
 IN p_auth_user INT)
BEGIN
    SELECT
        lob.id as id, 
        lob.description as description, 
        solo.id as solo_id, 
        solo.name as solo_taxonomy_name, 
        solo.lvl as solo_taxonomy_level, 
        cnt.id as content_id, 
        cnt.description as content_description, 
        ks.id as key_stage_id, 
        ks.name as key_stage_name, 
        lob.key_words as key_words, 
        lob.group_name as group_name, 
        lob.created as created, 
        lob.created_by as created_by_id, 
        user.first_name as created_by_name 
    FROM sow_learning_objective as lob 
        INNER JOIN sow_lesson__has__pathway as pw ON pw.learning_objective_id = lob.id 
        LEFT JOIN sow_solo_taxonomy as solo ON solo.id = lob.solo_taxonomy_id 
        LEFT JOIN sow_content as cnt ON cnt.id = lob.content_id 
        LEFT JOIN sow_key_stage as ks ON ks.id = cnt.key_stage_id 
        LEFT JOIN auth_user as user ON user.id = lob.created_by 
   WHERE 
        pw.lesson_id = p_lesson_id 
        ORDER BY ks.name DESC, solo.lvl;
END;
//

DELIMITER ;