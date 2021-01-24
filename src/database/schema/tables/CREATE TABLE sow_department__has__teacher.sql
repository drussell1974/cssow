DROP TABLE `sow_department__has__teacher`;

CREATE TABLE `sow_department__has__teacher` (
  `auth_user_id` INT NOT NULL,
  `department_id` INT(11) NOT NULL,
  `scheme_of_work_permission` SMALLINT NOT NULL DEFAULT 64,
  `lesson_permission` SMALLINT NOT NULL DEFAULT 64,
  `department_permission` SMALLINT NOT NULL DEFAULT 64,
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
  
INSERT INTO `sow_department__has__teacher` (`department_id`, `auth_user_id`, `scheme_of_work_permission`, `lesson_permission`, `department_permission`) 
SELECT dep.`id`, user.`id`, 64, 64, 64
FROM `sow_department` as dep, `auth_user` as user;
