DELIMITER //

DROP PROCEDURE IF EXISTS logging_notification__delete;

CREATE PROCEDURE logging_notification__delete (
 IN p_event_log_id INT,
 IN p_auth_user_id INT
)
BEGIN
    DELETE FROM sow_logging_notification
    WHERE user_id = p_auth_user_id and logging_id = p_event_log_id;
END;
//

DELIMITER ;