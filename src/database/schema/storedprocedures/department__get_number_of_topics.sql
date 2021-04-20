DELIMITER //

DROP PROCEDURE IF EXISTS department__get_number_of_topics;

CREATE PROCEDURE department__get_number_of_topics (
 IN p_department_id INT,
 IN p_auth_user INT)
BEGIN
    SELECT 
        count(top.id)
    FROM 
        sow_topic as top
    INNER JOIN
		sow_department as dep ON dep.id = top.department_id
    WHERE
		top.department_id = p_department_id
        and top.lvl = 1
        and (top.published = 1); -- or p_auth_user IN (SELECT auth_user_id 
													-- FROM sow_teacher 
													-- WHERE auth_user_id = p_auth_user));
END;
//

DELIMITER ;

CALL department__get_number_of_topics(5,2);