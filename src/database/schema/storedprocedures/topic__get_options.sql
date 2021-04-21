DELIMITER //

DROP PROCEDURE IF EXISTS topic__get_options$2;

CREATE PROCEDURE topic__get_options$2 (
 IN p_topic_id INT,
 IN p_department_id INT,
 IN p_lvl INT,
 IN p_show_published_state INT,
 IN p_auth_user INT)
BEGIN	
    SELECT 
        top.id as id, 
        top.name as name, 
        top.lvl as lvl,
        top.created as created, 
        top.created_by as created_by,
        top.published as published,
        prt_top.id as prt_id, 
        prt_top.name as prt_name, 
        prt_top.lvl as prt_lvl,
        prt_top.created as prt_created, 
        prt_top.created_by as prt_created_by,
        prt_top.published as prt_published
    FROM 
        sow_topic as top
        INNER JOIN sow_topic as prt_top ON prt_top.department_id = top.department_id
    WHERE 
		top.department_id = p_department_id -- and tl_top.parent_id is NULL
        and top.lvl = p_lvl and top.parent_id = prt_top.id
        and (p_show_published_state % top.published = 0
			or top.created_by = p_auth_user
        )
        ;
END;
//

DELIMITER ;

CALL topic__get_options$2(0, 5, 2, 1, 2);
CALL topic__get_options$2(2, 5, 2, 1, 2);

DELIMITER //

DROP PROCEDURE IF EXISTS topic__get_options;

CREATE PROCEDURE topic__get_options (
 IN p_topic_id INT,
 IN p_lvl INT,
 IN p_show_published_state INT,
 IN p_auth_user INT)
BEGIN
    SELECT 
        id, 
        name, 
        created, 
        created_by 
    FROM 
        sow_topic 
    WHERE 
        lvl = p_lvl and parent_id = p_topic_id
        and (p_show_published_state % published = 0
			or created_by = p_auth_user
        );
END;
//

DELIMITER ;