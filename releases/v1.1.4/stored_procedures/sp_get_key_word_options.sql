CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_get_key_word_options`()
BEGIN
	SELECT name 
    FROM sow_key_word kw 
    WHERE published = 1 ORDER BY name;
END