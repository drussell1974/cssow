
ALTER TABLE `sow_department` 
ADD COLUMN department_permission SMALLINT DEFAULT 0 NOT NULL after institute_id,
ADD COLUMN scheme_of_work_permission SMALLINT DEFAULT 0 NOT NULL after department_permission,
ADD COLUMN lesson_permission SMALLINT DEFAULT 0 NOT NULL after scheme_of_work_permission;