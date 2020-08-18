DELIMITER //

DROP PROCEDURE IF EXISTS lesson__insert_ks123_pathway;

CREATE PROCEDURE lesson__insert_ks123_pathway (
 IN p_lesson_id INT,
 IN p_ks123_pathway_id INT,
 IN p_auth_user INT)
BEGIN
    DECLARE record_exists INT DEFAULT 0;

    SET record_exists = (SELECT count(*) FROM sow_lesson__has__pathway WHERE lesson_id = p_lesson_id AND ks123_pathway_id = p_ks123_pathway_id);

    IF record_exists = 0 THEN
        INSERT INTO sow_lesson__has__ks123_pathway
            (lesson_id, ks123_pathway_id) 
        VALUES
            (p_lesson_id, p_ks123_pathway_id);
    END IF;
END;
//

DELIMITER ;