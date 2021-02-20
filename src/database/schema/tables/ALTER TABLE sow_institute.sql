
ALTER TABLE `sow_institute` 
ADD COLUMN department_permission SMALLINT DEFAULT 0 NOT NULL after name,
ADD COLUMN scheme_of_work_permission SMALLINT DEFAULT 0 NOT NULL after department_permission,
ADD COLUMN lesson_permission SMALLINT DEFAULT 0 NOT NULL after scheme_of_work_permission;