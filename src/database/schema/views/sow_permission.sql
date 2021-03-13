DROP VIEW IF EXISTS `sow_permission`;

CREATE VIEW `sow_permission` AS
SELECT 
        sow_teach.auth_user_id as teacher_id,
        teach.first_name as teacher_name,
		sow_teach.scheme_of_work_id as scheme_of_work_id,
        sow.name as scheme_of_work_name,
		hod.id as hod_id,
        hod.first_name as hod_name,
		inst.id as institute_id,
        inst.name as institute_name,
        dep.id as department_id,
        dep.name as department_name,
        COALESCE(dep_teach.department_permission, inst.department_permission, inst.department_permission, 0) as department_permission,
		COALESCE(sow_teach.scheme_of_work_permission, dep_teach.scheme_of_work_permission, inst.scheme_of_work_permission, 0) as scheme_of_work_permission,
        COALESCE(sow_teach.lesson_permission, dep_teach.lesson_permission, inst.lesson_permission, 0) as lesson_permission,
        IF(dep.head_id = teach.id, True, sow_teach.is_authorised) as is_authorised -- the head of department is immediately approved
    FROM sow_institute as inst 
    LEFT JOIN sow_department as dep ON dep.institute_id = inst.id
		LEFT JOIN sow_department__has__teacher as dep_teach
			ON dep_teach.department_id = dep.id -- link department teachers to department
		LEFT JOIN auth_user as hod
			ON hod.id = dep.head_id -- get head of department details from auth_user
    LEFT JOIN sow_scheme_of_work__has__teacher as sow_teach 
		ON sow_teach.auth_user_id = dep_teach.auth_user_id -- link schemes of work to department teachers
		LEFT JOIN sow_scheme_of_work as sow ON sow.id = sow_teach.scheme_of_work_id
			INNER JOIN auth_user as teach
				ON teach.id = sow_teach.auth_user_id -- get teacher details from auth_user
	WHERE teach.is_active = True and hod.is_active = True;

SELECT * FROM sow_permission;