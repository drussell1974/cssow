DELIMITER //

DROP PROCEDURE IF EXISTS keyword__delete;

CREATE PROCEDURE keyword__delete (
 IN p_keyword_id INT,
 IN p_auth_user INT)
BEGIN
    DELETE FROM sow_key_word
    WHERE id = p_keyword_id;
END;
//

DELIMITER ;