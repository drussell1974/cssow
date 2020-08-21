DELIMITER //

DROP PROCEDURE IF EXISTS ks123_pathway__get_linked_pathway;

CREATE PROCEDURE ks123_pathway__get_linked_pathway (
 IN p_lesson_id INT,
 IN p_auth_user INT)
BEGIN
    SELECT 
        pw.id as id, 
        pw.objective as objective 
    FROM sow_lesson__has__ks123_pathway as le_pw 
        INNER JOIN sow_ks123_pathway AS pw ON pw.id = le_pw.ks123_pathway_id 
    WHERE le_pw.lesson_id = p_lesson_id AND pw.published = 1;
END;
//

DELIMITER ;