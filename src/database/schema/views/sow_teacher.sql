DROP VIEW IF EXISTS sow_teacher;

CREATE VIEW sow_teacher
AS
    SELECT 
		user.id AS auth_user_id, 
		user.first_name as first_name, 
        user.last_name as last_name,
        teach.scheme_of_work_id as scheme_of_work_id,
        teach.scheme_of_work_permission as scheme_of_work_permission, 
        teach.lesson_permission as lesson_permission,
        teach.department_permission as department_permission
    FROM auth_user AS user
    INNER JOIN sow_teacher_join_code AS teach_join ON teach_join.auth_user_id = user.id
	 LEFT JOIN sow_scheme_of_work__has__teacher AS teach ON teach.join_code = teach_join.join_code 
    WHERE user.is_active = 1;
/*
SELECT * FROM sow_teacher_join_code WHERE join_code IN (SELECT join_code FROM sow_scheme_of_work__has__teacher WHERE scheme_of_work_id = 11);
SELECT * FROM sow_scheme_of_work__has__teacher WHERE email = 'test@locahost';
SELECT * FROM sow_department__has__teacher WHERE email = 'test@locahost';*/