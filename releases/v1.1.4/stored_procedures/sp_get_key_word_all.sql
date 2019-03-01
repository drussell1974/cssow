CREATE PROCEDURE `sp_get_key_word_all` ()
BEGIN
	SELECT 
		id as id, 
		name as term, 
        definition as definition 
    FROM sow_key_word kw 
    WHERE published = 1
	ORDER BY name;
END
