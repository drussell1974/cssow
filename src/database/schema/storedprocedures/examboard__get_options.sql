DELIMITER //

DROP PROCEDURE IF EXISTS examboard__get_options;

CREATE PROCEDURE examboard__get_options (
 IN p_auth_user INT)
BEGIN
    SELECT 
        id, 
        name 
    FROM 
        sow_exam_board;
END;
//

DELIMITER ;