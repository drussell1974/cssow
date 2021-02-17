DELIMITER //

DROP PROCEDURE IF EXISTS department__get_number_of_schemes_of_work;

CREATE PROCEDURE department__get_number_of_schemes_of_work (
 IN p_department_id INT,
 IN p_auth_user INT)
BEGIN
    SELECT 
        count(sow.id)
    FROM 
        sow_scheme_of_work as sow
	INNER JOIN
		sow_department__has__scheme_of_work as dep_sow ON dep_sow.scheme_of_work_id = sow.id
    INNER JOIN
		sow_department as dep ON dep.id = dep_sow.department_id
    WHERE
		dep_sow.department_id = p_department_id
        and (sow.published = 1); -- or p_auth_user IN (SELECT auth_user_id 
													-- FROM sow_teacher 
													-- WHERE auth_user_id = p_auth_user));
END;
//

DELIMITER ;
CALL department__get_number_of_schemes_of_work(5,2);