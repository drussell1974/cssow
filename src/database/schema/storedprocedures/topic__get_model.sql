DELIMITER //

DROP PROCEDURE IF EXISTS topic__get_model;

CREATE PROCEDURE topic__get_model (
 IN p_topic_id INT,
 IN p_department_id INT,
 IN p_show_published_state INT,
 IN p_auth_user INT)
BEGIN
    SELECT 
        cur.id as id, 
        cur.name as name, 
        cur.lvl as lvl,
        cur.created as created, 
        cur.created_by as created_by,
        cur.published as published,
        pnt.id as parent_id, 
        pnt.name as parent_name,
        pnt.lvl as parent_lvl,
        pnt.created as parent_created, 
        pnt.created_by as parent_created_by 
    FROM 
        sow_topic as cur
        LEFT JOIN sow_topic as pnt ON pnt.id = cur.parent_id
    WHERE 
        cur.id = p_topic_id and cur.department_id = p_department_id
        and (p_show_published_state % cur.published = 0
			or cur.created_by = p_auth_user
        );
END;
//

DELIMITER ;

CALL topic__get_model(0, 5, 1, 2);
CALL topic__get_model(10009, 84, 1, 152);
SELECT * FROM sow_topic;
WHERE department_id = 84;

