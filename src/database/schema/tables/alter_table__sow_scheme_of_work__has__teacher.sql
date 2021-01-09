ALTER TABLE sow_scheme_of_work__has__teacher
DROP COLUMN lesson_permission;

ALTER TABLE sow_scheme_of_work__has__teacher
ADD COLUMN lesson_permission TINYINT NOT NULL default 0 after auth_user_id;

ALTER TABLE sow_scheme_of_work__has__teacher
DROP COLUMN scheme_of_work_permission;

ALTER TABLE sow_scheme_of_work__has__teacher
ADD COLUMN scheme_of_work_permission TINYINT NOT NULL default 0 after auth_user_id;