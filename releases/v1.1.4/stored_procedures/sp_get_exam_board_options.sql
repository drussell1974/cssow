DELIMITER $$
CREATE PROCEDURE `sp_get_exam_board_options`()
BEGIN
	SELECT id, name FROM sow_exam_board;
END$$
DELIMITER ;
