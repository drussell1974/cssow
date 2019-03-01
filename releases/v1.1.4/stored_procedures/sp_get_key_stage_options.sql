CREATE PROCEDURE `sp_get_key_stage_options` ()
BEGIN
	SELECT id, name FROM sow_key_stage;
END
