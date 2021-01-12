ALTER TABLE sow_scheme_of_work__has__teacher
DROP COLUMN lesson_permission;

ALTER TABLE sow_scheme_of_work__has__teacher
ADD COLUMN lesson_permission TINYINT NOT NULL default 0 after auth_user_id;

ALTER TABLE sow_scheme_of_work__has__teacher
DROP COLUMN scheme_of_work_permission;

ALTER TABLE sow_scheme_of_work__has__teacher
ADD COLUMN scheme_of_work_permission TINYINT NOT NULL default 0 after auth_user_id;

ALTER TABLE sow_scheme_of_work__has__teacher
ADD COLUMN department_permission TINYINT NOT NULL default 0 after auth_user_id;

UPDATE `drussell1974$cssow_api`.`sow_scheme_of_work__has__teacher` 
SET 
    `scheme_of_work_permission` = 64, 
    `lesson_permission` = 64, 
    `department_permission` = 64
WHERE (`scheme_of_work_id` = 11) and (`auth_user_id` = 2');
