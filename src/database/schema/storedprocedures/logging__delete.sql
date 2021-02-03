DELIMITER //

DROP PROCEDURE IF EXISTS logging__delete;

CREATE PROCEDURE logging__delete (
 IN p_scheme_of_work_id INT,
 IN p_older_than_n_days INT,
 IN p_auth_user INT
)
BEGIN
    DECLARE older_than_date DATETIME DEFAULT DATE_SUB(now(), INTERVAL p_older_than_n_days DAY);

    DELETE FROM sow_logging
    WHERE 
		scheme_of_work_id = p_scheme_of_work_id
		AND created < older_than_date;
END;
//

DELIMITER ;