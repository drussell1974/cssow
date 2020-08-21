DELIMITER //

DROP PROCEDURE IF EXISTS lesson_resource__insert;

CREATE PROCEDURE lesson_resource__insert (
 OUT p_resource_id INT,
 IN p_title VARCHAR(300),
 IN p_publisher VARCHAR(500),
 IN p_type_id INT,
 IN p_notes text,
 IN p_url VARCHAR(2083),
 IN p_md_document_name VARCHAR(200),
 IN p_is_expired TINYINT,
 IN p_lesson_id INT,
 IN p_created DATETIME,
 IN p_created_by INT,
 IN p_published INT,
 IN p_auth_user INT)
BEGIN
    INSERT INTO sow_resource 
    (
        title, 
        publisher, 
        type_id, 
        page_notes, 
        url,
        md_document_name, 
        is_expired, 
        lesson_id, 
        created, 
        created_by, 
        published
    )
    VALUES 
    (
        p_title, 
        p_publisher,
        p_type_id,
        p_notes, 
        p_url,
        p_md_document_name, 
        p_is_expired, 
        p_lesson_id,
        p_created,
        p_created_by,
        p_published
    );

    SELECT LAST_INSERT_ID();
END;
//

DELIMITER ;