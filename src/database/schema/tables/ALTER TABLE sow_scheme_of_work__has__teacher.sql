
ALTER TABLE sow_scheme_of_work__has__teacher
DROP COLUMN site_permission;

ALTER TABLE sow_scheme_of_work__has__teacher
ADD COLUMN department_permission INT(11) DEFAULT 7 NOT NULL;

ALTER TABLE sow_scheme_of_work__has__teacher
ALTER lesson_permission SET DEFAULT 7;

ALTER TABLE sow_scheme_of_work__has__teacher
ALTER scheme_of_work_permission SET DEFAULT 7;

ALTER TABLE sow_scheme_of_work__has__teacher
ADD COLUMN is_authorised BOOLEAN DEFAULT True after auth_user_id;