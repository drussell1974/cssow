DELIMITER //

DROP PROCEDURE IF EXISTS lesson_learning_objective__get_all_pathway_objectives;

CREATE PROCEDURE lesson_learning_objective__get_all_pathway_objectives (
 IN p_key_stage_id INT,
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
    CONCAT_WS(' ', user.first_name, user.last_name) as created_by_name
    FROM sow_learning_objective as lob 
        LEFT JOIN sow_topic as top ON top.id = lob.topic_id 
        LEFT JOIN sow_topic as pnt_top ON pnt_top.id = top.parent_id 
        LEFT JOIN sow_solo_taxonomy as solo ON solo.id = lob.solo_taxonomy_id 
        LEFT JOIN sow_content as cnt ON cnt.id = lob.content_id 
        LEFT JOIN sow_key_stage as ks ON ks.id = cnt.key_stage_id 
        LEFT JOIN auth_user as user ON user.id = lob.created_by 
    WHERE ks.id < p_key_stage_id 
    ORDER BY ks.name DESC, solo.lvl;
END;
//

DELIMITER ;