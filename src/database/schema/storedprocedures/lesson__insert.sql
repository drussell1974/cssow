DELIMITER //

DROP PROCEDURE IF EXISTS lesson__insert;

CREATE PROCEDURE lesson__insert (
 OUT p_lesson_id INT,
 IN p_title VARCHAR(45),
 IN p_summary VARCHAR(100),
 IN p_order_of_delivery_id INT,
 IN p_scheme_of_work_id INT,
 IN p_content_id INT,
 IN p_topic_id INT,
 IN p_year_id INT,
 IN p_published INT,
 IN p_auth_user INT,
 IN p_created DATETIME)
BEGIN
    INSERT sow_lesson
    ( 
        title, 
        summary, 
        order_of_delivery_id, 
        scheme_of_work_id, 
        content_id,
        topic_id, 
        year_id,
        created_by,
        created,
        published
    )
    VALUES
    ( 
        p_title, 
        p_summary, 
        p_order_of_delivery_id, 
        p_scheme_of_work_id, 
        p_content_id,
        p_topic_id, 
        p_year_id,
        p_auth_user,
        p_created,
        p_published
    );
    
    SET p_lesson_id = LAST_INSERT_ID();
    SELECT p_lesson_id;
END;
//

DELIMITER ;