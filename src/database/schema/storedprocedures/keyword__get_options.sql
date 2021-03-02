DELIMITER //

DROP PROCEDURE IF EXISTS lesson__get_options;

CREATE PROCEDURE lesson__get_options (
 IN p_scheme_of_work_id INT,
 IN p_show_published_state INT,
 IN p_auth_user INT)
BEGIN
    SELECT 
        le.id as id, 
        le.title as title, 
        le.order_of_delivery_id as order_of_delivery_id, 
        top.id as topic_id, 
        top.name as name, 
        yr.id as year_id, 
        yr.name as year_name 
    FROM sow_lesson as le 
        INNER JOIN sow_topic as top ON top.id = le.topic_id 
        INNER JOIN sow_year as yr ON yr.id = le.year_id  
    WHERE 
        le.scheme_of_work_id = p_scheme_of_work_id
        AND (p_show_published_state % le.published = 0 
                or le.created_by = p_auth_user)
    ORDER BY le.year_id, le.order_of_delivery_id;
END;
//

DELIMITER ;

CALL lesson__get_options(11,1, 2);