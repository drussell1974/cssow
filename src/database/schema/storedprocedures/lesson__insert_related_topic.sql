DELIMITER //

DROP PROCEDURE IF EXISTS lesson__insert_related_topic;

CREATE PROCEDURE lesson__insert_related_topic (
 IN p_lesson_id INT,
 IN p_topic_id INT,
 IN p_auth_user INT)
BEGIN
    DECLARE record_exists INT DEFAULT 0;

    SET record_exists = (SELECT count(*) FROM sow_lesson__has__topics WHERE lesson_id = p_lesson_id AND topic_id = p_topic_id);

    IF record_exists = 0 THEN
        INSERT INTO sow_lesson__has__topics 
            (lesson_id, topic_id) 
        VALUES
            (p_lesson_id, p_topic_id);
    END IF;
END;
//

DELIMITER ;