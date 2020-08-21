DELIMITER //

DROP PROCEDURE IF EXISTS learning_objective__insert;

CREATE PROCEDURE learning_objective__insert (
 OUT p_learning_objective_id INT,
 IN p_description VARCHAR(1000),
 IN p_group_name VARCHAR(15),
 IN p_notes VARCHAR(4000),
 IN p_key_words VARCHAR(1000),
 IN p_solo_taxonomy_id INT,
 IN p_content_id INT,
 IN p_parent_id INT,
 IN p_created DATETIME,
 IN p_created_by INT,
 IN p_published INT,
 IN p_auth_user INT)
BEGIN
  -- CHECK sow_teacher
    INSERT INTO sow_learning_objective
    (
        description, 
        group_name, 
        notes, 
        key_words,
        solo_taxonomy_id, 
        content_id, 
        parent_id,
        created,
        created_by
    )
    VALUES
    (
        p_description, 
        p_group_name, 
        p_notes, 
        p_key_words,
        p_solo_taxonomy_id, 
        p_content_id, 
        p_parent_id,
        p_created,
        p_created_by 
    );

    SET p_learning_objective_id = LAST_INSERT_ID();

    SELECT p_learning_objective_id
END;
//

DELIMITER ;

