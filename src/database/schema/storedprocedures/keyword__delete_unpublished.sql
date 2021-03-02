DELIMITER //

DROP PROCEDURE IF EXISTS keyword__delete_unpublished;

CREATE PROCEDURE keyword__delete_unpublished (
 IN p_scheme_of_work_id INT,
 IN p_auth_user INT)
BEGIN
    DELETE FROM sow_key_word
	-- UPDATE sow_key_word
	-- SET published = 64
    WHERE scheme_of_work_id = p_scheme_of_work_id 
            AND published IN (32,64)
			AND p_auth_user IN 
					(SELECT auth_user_id 
					FROM sow_teacher 
					WHERE scheme_of_work_id = p_scheme_of_work_id);

END;
//

DELIMITER ;