
ALTER TABLE `sow_institute` 
ADD COLUMN department_permission SMALLINT DEFAULT 0 NOT NULL after name,
ADD COLUMN scheme_of_work_permission SMALLINT DEFAULT 0 NOT NULL after department_permission,
ADD COLUMN lesson_permission SMALLINT DEFAULT 0 NOT NULL after scheme_of_work_permission;

ALTER TABLE sow_institute ADD COLUMN head_id int NOT NULL default 2 after name;

ALTER TABLE `sow_institute` 
ADD CONSTRAINT `sow_institute__has__head`
  FOREIGN KEY (`head_id`)
  REFERENCES `auth_user` (`id`)
  ON DELETE CASCADE
  ON UPDATE CASCADE;