DELIMITER //

DROP PROCEDURE IF EXISTS lesson_learning_objective__update;

CREATE PROCEDURE lesson_learning_objective__update (
 IN p_learning_objective_id INT,
 IN p_lesson_id INT,
 IN p_description VARCHAR(1000),
 IN p_group_name VARCHAR(15),
 IN p_notes VARCHAR(4000),
 IN p_key_words VARCHAR(1000),
 IN p_solo_taxonomy_id INT,
 IN p_content_id INT,
 IN p_parent_id INT,
 IN p_published INT,
 IN p_auth_user INT)
BEGIN
  -- CHECK sow_teacher
    UPDATE sow_learning_objective
    SET 
        description = p_description, 
        group_name = p_group_name, 
        notes = p_notes, 
        key_words = p_key_words,
        solo_taxonomy_id = p_solo_taxonomy_id, 
        content_id = p_content_id, 
        parent_id = p_parent_id,
        modified_by = p_auth_user
    WHERE id = p_learning_objective_id;

    UPDATE sow_learning_objective__has__lesson
    SET 
        published = p_published
    WHERE learning_objective_id = p_learning_objective_id and lesson_id = p_lesson_id;
END;
//

DELIMITER ;

