DELIMITER //

DROP PROCEDURE IF EXISTS logging__get_notifications;

CREATE PROCEDURE logging__get_notifications (
 IN p_page INT,
 IN p_pagesize INT, 
 IN p_auth_user INT)
BEGIN
    DECLARE offset_n_records INT DEFAULT p_page * p_pagesize;

    SELECT 
        id as id,
        created as created,
        event_type as event_type, 
        message as message,
        details as details,
        action as action
    FROM 
        sow_logging as log
        INNER JOIN sow_logging_notification as notify ON notify.logging_id = log.id
    WHERE
		notify.user_id = p_auth_user 
    LIMIT p_pagesize OFFSET offset_n_records;   
END;
//

DELIMITER ;