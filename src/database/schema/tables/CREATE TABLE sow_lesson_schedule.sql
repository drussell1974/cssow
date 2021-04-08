#DROP TABLE `sow_lesson_schedule`;

CREATE TABLE `sow_lesson_schedule` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `start_date` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  `class_code` CHAR(6) NOT NULL UNIQUE,
  `institute_id` INT NOT NULL,
  `department_id` INT NOT NULL,
  `scheme_of_work_id` INT NOT NULL,
  `lesson_id` INT NOT NULL,
  `created` datetime DEFAULT CURRENT_TIMESTAMP,
  `created_by` int unsigned NOT NULL DEFAULT '0',
  `published` INT DEFAULT '1',
  `modified` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  `modified_by` int unsigned NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
);

ALTER TABLE `drussell1974$cssow_api`.`sow_lesson_schedule` 
ADD INDEX `fk_sow_lesson_schedule__has__lesson_idx` (`lesson_id` ASC) VISIBLE;

ALTER TABLE `drussell1974$cssow_api`.`sow_lesson_schedule` 
ADD CONSTRAINT `fk_sow_lesson_schedule__has__lesson`
  FOREIGN KEY (`lesson_id`)
  REFERENCES `drussell1974$cssow_api`.`sow_lesson` (`id`)
  ON DELETE CASCADE
  ON UPDATE CASCADE;
