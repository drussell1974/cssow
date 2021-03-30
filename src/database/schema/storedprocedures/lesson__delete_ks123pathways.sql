DELIMITER //

DROP PROCEDURE IF EXISTS lesson__delete_ks123pathways;

CREATE PROCEDURE lesson__delete_ks123pathways (
 IN p_lesson_id INT,
 IN p_auth_user INT)
BEGIN
    DELETE FROM sow_lesson__has__ks123_pathway
    WHERE lesson_id = p_lesson_id;
END;
//

DELIMITER ;