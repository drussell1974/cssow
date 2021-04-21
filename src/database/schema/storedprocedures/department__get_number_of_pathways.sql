DELIMITER //

DROP PROCEDURE IF EXISTS department__get_number_of_pathways;

CREATE PROCEDURE department__get_number_of_pathways (
 IN p_department_id INT,
 IN p_auth_user INT)
BEGIN
    SELECT 
        count(pw.id)
    FROM 
        sow_ks123_pathway as pw
    INNER JOIN
		sow_department as dep ON dep.id = pw.department_id
    WHERE
		pw.department_id = p_department_id
        and (pw.published = 1); -- or p_auth_user IN (SELECT auth_user_id 
													-- FROM sow_teacher 
													-- WHERE auth_user_id = p_auth_user));
END;
//

DELIMITER ;

CALL department__get_number_of_pathways(5,2);