DROP VIEW IF EXISTS sow_teacher;

CREATE VIEW sow_teacher
AS
    -- super users are omnipotent
    -- SELECT user.id AS auth_user_id, NULL as scheme_of_work_id, user.first_name as first_name, user.last_name as last_name, 0 as scheme_of_work_permission, 0 as lesson_permission, 0 as department_permission
    -- FROM auth_user AS user
    -- WHERE user.is_active = 1 AND user.is_superuser = 1
    -- UNION
    -- is the user as teacher of this this scheme of work
    SELECT 
		user.id AS auth_user_id, 
		-- teach.scheme_of_work_id AS scheme_of_work_id, 
        user.first_name as first_name, 
        user.last_name as last_name, 
        teach.scheme_of_work_permission as scheme_of_work_permission, 
        teach.lesson_permission as lesson_permission,
        teach.department_permission as department_permission
    FROM auth_user AS user
	 LEFT JOIN sow_scheme_of_work__has__teacher AS teach ON user.id = teach.auth_user_id 
    WHERE user.is_active = 1;
    
SELECT * FROM sow_teacher;