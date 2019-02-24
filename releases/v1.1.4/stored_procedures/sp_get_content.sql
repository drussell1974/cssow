CREATE PROCEDURE `sp_get_content_options`(IN key_stage_id int)
BEGIN
	SELECT cnt.id as id, cnt.description as description 
    FROM sow_content as cnt 
    WHERE key_stage_id = key_stage_id;
END