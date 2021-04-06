DELIMITER //

DROP PROCEDURE IF EXISTS logging__get_notifications;

CREATE PROCEDURE logging__get_notifications (
 IN p_start_date DATETIME,
 IN p_page INT,
 IN p_pagesize INT, 
 IN p_auth_user INT)
BEGIN
    DECLARE offset_n_records INT DEFAULT p_page * p_pagesize;

    SELECT 
        id as id,
        notify.start_date as start_date,
        log.created as created,
        event_type as event_type,
        log.message as message,
        notify.action as action,
        notify.message as notify_message
    FROM 
        sow_logging as log
        INNER JOIN sow_logging_notification as notify ON notify.logging_id = log.id
    WHERE
		notify.user_id = p_auth_user
        AND notify.start_date < p_start_date -- only get notifications greater than this date
    LIMIT p_pagesize OFFSET offset_n_records;   
END;
//

DELIMITER ;
SELECT * FROM drussell1974$cssow_api.sow_logging_notification;
CALL logging__get_notifications('2021-04-06T15:38', 0, 10, 2);
