DELIMITER //

DROP PROCEDURE IF EXISTS lesson_resource__get_all;

CREATE PROCEDURE lesson_resource__get_all (
 IN p_lesson_id INT,
 IN p_resource_type_id INT,
 IN p_auth_user INT)
BEGIN
    SELECT 
      res.id as id, 
      res.title as title, 
      res.publisher as publisher, 
      res.type_id as type_id, 
      res_typ.name as resource_type_name, 
      res_typ.task_icon as task_icon, 
      res.md_document_name as md_document_name, 
      res.page_notes as page_notes,  
      res.url as page_uri,  
      res.lesson_id as lesson_id,  
      res.created as created,  
      res.created_by as created_by_id,  
      CONCAT_WS(' ', user.first_name, user.last_name) as created_by_name,  
      res.published as published 
    FROM sow_resource AS res
    LEFT JOIN sow_lesson AS les ON les.id = res.lesson_id
    LEFT JOIN sow_resource_type as res_typ ON res.type_id = res_typ.id  
    LEFT JOIN auth_user AS user ON user.id = res.created_by 
    WHERE res.lesson_id = p_lesson_id 
      AND (res.type_id = p_resource_type_id or p_resource_type_id = p_resource_type_id) 
      AND (res.published = 1
        or p_auth_user IN 
                (SELECT auth_user_id 
                FROM sow_teacher 
                WHERE scheme_of_work_id = les.scheme_of_work_id)
        );
END;
//

DELIMITER ;