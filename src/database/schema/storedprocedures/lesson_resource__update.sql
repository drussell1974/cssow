DELIMITER //

DROP PROCEDURE IF EXISTS lesson_resource__update;

CREATE PROCEDURE lesson_resource__update (
 IN p_resource_id INT,
 IN p_title VARCHAR(300),
 IN p_publisher VARCHAR(500),
 IN p_type_id INT,
 IN p_notes text,
 IN p_url VARCHAR(2083),
 IN p_md_document_name VARCHAR(200),
 IN p_is_expired TINYINT,
 IN p_lesson_id INT,
 IN p_published INT,
 IN p_auth_user INT)
BEGIN
    UPDATE 
        sow_resource
    SET 
        title = p_title, 
        publisher = p_publisher, 
        type_id = p_type_id,
        page_notes = p_notes,
        url = p_url,
        md_document_name = p_md_document_name,
        is_expired = p_is_expired,
        lesson_id = p_lesson_id, 
        published = p_published,
        modified_by = p_auth_user
    WHERE 
        id = p_resource_id;
END;
//

DELIMITER ;