#DROP TABLE IF EXISTS sow_scheme_of_work__has__teacher;
DROP TABLE IF EXISTS sow_department__has__scheme_of_work;

ALTER TABLE sow_scheme_of_work__has__teacher
MODIFY is_authorised BIT NOT NULL default False;

UPDATE sow_scheme_of_work__has__teacher
SET is_authorised = 1 WHERE auth_user_id > 0;
