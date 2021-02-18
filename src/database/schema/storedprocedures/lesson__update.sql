DELIMITER //

DROP PROCEDURE IF EXISTS lesson__update;

CREATE PROCEDURE lesson__update (
 IN p_lesson_id INT,
 IN p_title VARCHAR(45),
 IN p_summary VARCHAR(100),
 IN p_order_of_delivery_id INT,
 IN p_scheme_of_work_id INT,
 IN p_content_id INT,
 IN p_topic_id INT,
 IN p_year_id INT,
 IN p_published INT,
 IN p_auth_user INT)
BEGIN
    UPDATE sow_lesson 
    SET title = p_title, 
        summary = p_summary, 
        order_of_delivery_id = p_order_of_delivery_id, 
        scheme_of_work_id = p_scheme_of_work_id, 
        content_id = p_content_id,
        topic_id = p_topic_id, 
        year_id = p_year_id, 
        published = p_published,
        modified_by = p_auth_user
    WHERE 
        id =  p_lesson_id;
END;
//

DELIMITER ;