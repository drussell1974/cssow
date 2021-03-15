DROP TABLE `sow_department__has__teacher`;

CREATE TABLE `sow_department__has__teacher` (
  `auth_user_id` INT NOT NULL,
  `department_id` INT(11) NOT NULL,
  `department_permission` SMALLINT NOT NULL DEFAULT 64,
  `scheme_of_work_permission` SMALLINT NOT NULL DEFAULT 64,
  `lesson_permission` SMALLINT NOT NULL DEFAULT 64,
  PRIMARY KEY (`auth_user_id`, `department_id`),
  INDEX `fk_sow_department__has__teacher__has__department_id` (`department_id` ASC),
  CONSTRAINT `fk_sow_department__has__teacher__has__department_id`
    FOREIGN KEY (`department_id`)
    REFERENCES `sow_department` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_sow_department__has__teacher__has__auth_user_id`
    FOREIGN KEY (`auth_user_id`)
    REFERENCES `auth_user` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE);
    
ALTER TABLE sow_department__has__teacher ADD COLUMN `lesson_permission` SMALLINT NOT NULL DEFAULT 64 after department_id;    
ALTER TABLE sow_department__has__teacher ADD COLUMN `scheme_of_work_permission` SMALLINT NOT NULL DEFAULT 64 after department_id;
ALTER TABLE sow_department__has__teacher ADD COLUMN `department_permission` SMALLINT NOT NULL DEFAULT 64 after department_id;


ALTER TABLE sow_department__has__teacher
DROP COLUMN created_by;

ALTER TABLE sow_department__has__teacher
DROP COLUMN created;

ALTER TABLE sow_department__has__teacher
DROP COLUMN modified;

ALTER TABLE sow_department__has__teacher
ADD COLUMN created_by INT DEFAULT 0 after department_permission;

ALTER TABLE sow_department__has__teacher
ADD COLUMN modified_by INT DEFAULT 0 after created;

ALTER TABLE sow_department__has__teacher
ADD COLUMN created DATETIME DEFAULT CURRENT_TIMESTAMP after created_by;

ALTER TABLE sow_department__has__teacher
ADD COLUMN modified DATETIME ON UPDATE CURRENT_TIMESTAMP after created;

