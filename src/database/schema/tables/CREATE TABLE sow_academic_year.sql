/* DROP TABLE `sow_academic_year_period`; DROP TABLE `sow_academic_year`; */

CREATE TABLE `sow_academic_year` (
  `year` INT NOT NULL,
  `department_id` INT NOT NULL,
  `start_date` datetime NOT NULL,
  `end_date` datetime NOT NULL,
  `created` datetime DEFAULT CURRENT_TIMESTAMP,
  `created_by` int unsigned NOT NULL DEFAULT '0',
  `modified` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  `modified_by` int unsigned NOT NULL DEFAULT '0',
  PRIMARY KEY (`year`, `department_id`)
);

ALTER TABLE `sow_academic_year` 
ADD CONSTRAINT `fk_sow_academic_year__has__department`
  FOREIGN KEY (`department_id`)
  REFERENCES `sow_department` (`id`)
  ON DELETE CASCADE
  ON UPDATE CASCADE;

CREATE TABLE `sow_academic_year_period` (
  `time` time NOT NULL,
  `name` VARCHAR(20) NOT NULL,
  `academic_year` INT NOT NULL,
  `department_id` INT NOT NULL,
  `created` datetime DEFAULT CURRENT_TIMESTAMP,
  `created_by` int unsigned NOT NULL DEFAULT '0',
  `modified` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  `modified_by` int unsigned NOT NULL DEFAULT '0',
  PRIMARY KEY (`academic_year`, `name`)
);

ALTER TABLE `sow_academic_year_period` 
ADD CONSTRAINT `fk_sow_academic_year_period__has__academic_year`
  FOREIGN KEY (`department_id`, `academic_year`)
  REFERENCES `sow_academic_year` (`department_id`, `year`)
  ON DELETE CASCADE
  ON UPDATE CASCADE;

INSERT INTO `sow_academic_year` (`year`, `department_id`, `start_date`, `end_date`) VALUES (2019, '5', '2019-09-01 00:00', '2020-07-07 00:00');
INSERT INTO `sow_academic_year` (`year`, `department_id`, `start_date`, `end_date`) VALUES (2020, '5', '2020-09-03 00:00', '2021-07-15 00:00');
INSERT INTO `sow_academic_year` (`year`, `department_id`, `start_date`, `end_date`) VALUES (2021, '5', '2021-09-06 00:00', '2022-07-21 00:00');

INSERT INTO `sow_academic_year_period` (`time`, `name`, `academic_year`, `department_id`) VALUES ("09:00", "Period 1", 2020, 5); 
INSERT INTO `sow_academic_year_period` (`time`, `name`, `academic_year`, `department_id`) VALUES ("10:00", "Period 2", 2020, 5); 
INSERT INTO `sow_academic_year_period` (`time`, `name`, `academic_year`, `department_id`) VALUES ("11:00", "Break", 2020, 5); 
INSERT INTO `sow_academic_year_period` (`time`, `name`, `academic_year`, `department_id`) VALUES ("11:15", "Period 3", 2020, 5); 
INSERT INTO `sow_academic_year_period` (`time`, `name`, `academic_year`, `department_id`) VALUES ("12:15", "Lunch", 2020, 5); 
INSERT INTO `sow_academic_year_period` (`time`, `name`, `academic_year`, `department_id`) VALUES ("13:15", "Period 4", 2020, 5); 
INSERT INTO `sow_academic_year_period` (`time`, `name`, `academic_year`, `department_id`) VALUES ("14:15", "Period 5", 2020, 5); 
INSERT INTO `sow_academic_year_period` (`time`, `name`, `academic_year`, `department_id`) VALUES ("15:15", "Period 6", 2020, 5); 
INSERT INTO `sow_academic_year_period` (`time`, `name`, `academic_year`, `department_id`) VALUES ("16:15", "Homework club", 2020, 5);
