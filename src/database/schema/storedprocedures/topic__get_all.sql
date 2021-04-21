DELIMITER //

DROP PROCEDURE IF EXISTS topic__get_all$2;

CREATE PROCEDURE topic__get_all$2 (
 IN p_department_id INT,
 IN p_show_published_state INT,
 IN p_auth_user INT)
BEGIN
    SELECT 
        cur.id, 
        cur.name, 
        cur.lvl as lvl,
        cur.created, 
        cur.created_by,
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
		cur.department_id = p_department_id
        and (p_show_published_state % cur.published = 0
		  	or cur.created_by = p_auth_user)
	ORDER BY 
		pnt.lvl, pnt.id, cur.lvl, cur.name 
        ;
END;
//

DELIMITER ;

CALL topic__get_all$2(5, 1, 2);

DELIMITER //

DROP PROCEDURE IF EXISTS topic__get_all;

CREATE PROCEDURE topic__get_all (
 IN p_department_id INT,
 IN p_show_published_state INT,
 IN p_auth_user INT)
BEGIN
    SELECT 
        cur.id, 
        cur.name, 
        cur.lvl as lvl,
        cur.created, 
        cur.created_by,
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
		cur.department_id = p_department_id
        and (p_show_published_state % cur.published = 0
		  	or cur.created_by = p_auth_user)
	ORDER BY 
		pnt.id, cur.name 
        ;
END;
//

DELIMITER ;
