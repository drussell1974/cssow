#DROP TABLE `sow_lesson_schedule`;

CREATE TABLE `sow_lesson_schedule` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `class_code` CHAR(6) NOT NULL,
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
