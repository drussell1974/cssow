DELIMITER //

DROP PROCEDURE IF EXISTS logging_notification__insert;

CREATE PROCEDURE logging_notification__insert (
 IN p_message VARCHAR(135),
 IN p_action VARCHAR(2083),
 IN p_start_date DATETIME,
 IN p_event_log_id INT,
 IN p_auth_user_id INT
)
BEGIN

    INSERT IGNORE INTO sow_logging_notification
    (
		message,
        action,
		logging_id, 
        user_id, 
        start_date
    )
    VALUES 
    (
		p_message,
        p_action,
		p_event_log_id,
        p_auth_user_id,
        p_start_date
    );

    SELECT LAST_INSERT_ID();
END;
//

DELIMITER ;