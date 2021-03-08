DELIMITER //

DROP PROCEDURE IF EXISTS lesson_learning_objective__insert;

CREATE PROCEDURE lesson_learning_objective__insert (
 OUT learning_objective_id INT,
 IN p_lesson_id INT,
 IN p_description VARCHAR(1000),
 IN p_group_name VARCHAR(15),
 IN p_notes VARCHAR(4000),
 IN p_missing_words_challenge VARCHAR(140),
 IN p_key_words VARCHAR(1000),
 IN p_solo_taxonomy_id INT,
 IN p_content_id INT,
 IN p_parent_id INT,
 IN p_created DATETIME,
 IN p_created_by INT,
 IN p_published INT,
 IN p_auth_user INT)
BEGIN
  DECLARE new_id INT DEFAULT 0;
  -- CHECK sow_teacher
    INSERT INTO sow_learning_objective
    (
        description, 
        group_name, 
        notes, 
        missing_words_challenge,
        key_words,
        solo_taxonomy_id, 
        content_id, 
        parent_id,
        created,
        created_by,
        published
    )
    VALUES
    (
        p_description, 
        p_group_name, 
        p_notes, 
        p_missing_words_challenge,
        p_key_words,
        p_solo_taxonomy_id, 
        p_content_id, 
        p_parent_id,
        p_created,
        p_created_by,
        p_published
    );

    SET new_id = LAST_INSERT_ID();
    
    INSERT INTO sow_learning_objective__has__lesson 
    (
        learning_objective_id, 
        lesson_id,
        published
    ) 
    VALUES
    (
        new_id,
        p_lesson_id, 
        p_published
    );

    SELECT new_id;
END;
//

DELIMITER ;

