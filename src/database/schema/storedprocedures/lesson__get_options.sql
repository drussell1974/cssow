DELIMITER //

DROP PROCEDURE IF EXISTS lesson__get_options;

CREATE PROCEDURE lesson__get_options (
 IN p_scheme_of_work_id INT,
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
        AND (le.published = 1 
                or p_auth_user IN (SELECT auth_user_id 
                                FROM sow_teacher 
                                WHERE auth_user_id = p_auth_user AND scheme_of_work_id = le.scheme_of_work_id)
        )
    ORDER BY le.year_id, le.order_of_delivery_id;
END;
//

DELIMITER ;