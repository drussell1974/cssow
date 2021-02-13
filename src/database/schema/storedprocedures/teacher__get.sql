DELIMITER //

DROP PROCEDURE IF EXISTS teacher__get;

CREATE PROCEDURE teacher__get (
 IN p_teacher_id INT,
 IN p_department_id INT,
 IN p_institute_id INT)
BEGIN
    SELECT 
      user.id as teacher_id,
      user.first_name as teacher_name,  
      dep.id as department_id,
      dep.name as department_name,
      ins.id as institute_id,
      ins.name as institute_name,
      -- authorise based on department__has__teacher relationship,
      -- if this does not exist yet, then is_authorised is true, if 
      -- the teacher is the head of the department
      -- IFNULL(teach_dep.is_authorised, dep.head_id = p_teacher_id) as is_authorised
	  dep.head_id = p_teacher_id as is_authorised
    FROM auth_user as user    
    INNER JOIN sow_department as dep
    INNER JOIN sow_institute as ins ON ins.id = dep.institute_id
    LEFT JOIN sow_department__has__teacher as teach_dep 
		ON teach_dep.auth_user_id = user.id and teach_dep.department_id = dep.id
	WHERE user.id = p_teacher_id and dep.institute_id = p_institute_id and (teach_dep.department_id = p_department_id or dep.head_id = p_teacher_id);
    
END;
//

DELIMITER ;

CALL teacher__get(2,5,2);