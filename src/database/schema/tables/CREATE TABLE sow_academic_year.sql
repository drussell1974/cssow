/* DROP TABLE `sow_academic_year_period`; DROP TABLE `sow_academic_year`; */

CREATE TABLE `sow_academic_year` (
  `year` INT NOT NULL,
  `institute_id` INT NOT NULL,
  `start_date` datetime NOT NULL,
  `end_date` datetime NOT NULL,
  `created` datetime DEFAULT CURRENT_TIMESTAMP,
  `created_by` int unsigned NOT NULL DEFAULT '0',
  `modified` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  `modified_by` int unsigned NOT NULL DEFAULT '0',
  `published` int NOT NULL DEFAULT '1',
  PRIMARY KEY (`year`, `institute_id`)
);

ALTER TABLE `sow_academic_year` 
ADD CONSTRAINT `fk_sow_academic_year__has__department`
  FOREIGN KEY (`institute_id`)
  REFERENCES `sow_institute` (`id`)
  ON DELETE CASCADE
  ON UPDATE CASCADE;

CREATE TABLE `sow_academic_year_period` (
  `time` time NOT NULL,
  `name` VARCHAR(20) NOT NULL,
  `academic_year` INT NOT NULL,
  `institute_id` INT NOT NULL,
  `created` datetime DEFAULT CURRENT_TIMESTAMP,
  `created_by` int unsigned NOT NULL DEFAULT '0',
  `modified` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  `modified_by` int unsigned NOT NULL DEFAULT '0',
  `published` int NOT NULL DEFAULT '1'
  PRIMARY KEY (`academic_year`, `time`, `institute_id`)
);

ALTER TABLE `sow_academic_year_period` 
ADD CONSTRAINT `fk_sow_academic_year_period__has__academic_year`
  FOREIGN KEY (`institute_id`, `academic_year`)
  REFERENCES `sow_academic_year` (`institute_id`, `year`)
  ON DELETE CASCADE
  ON UPDATE CASCADE;



ALTER TABLE `sow_academic_year_period`
ADD COLUMN `published` int NOT NULL DEFAULT '1';

ALTER TABLE `sow_academic_year`
ADD COLUMN `published` int NOT NULL DEFAULT '1';

SET @inst = 3;
SET @yr = 2021;

-- INSERT INTO `sow_academic_year` (`year`, `institute_id`, `start_date`, `end_date`) VALUES (2019, @inst, '2020-09-01 00:00', '2021-07-07 00:00');

INSERT INTO `sow_academic_year_period` (`time`, `name`, `academic_year`, `institute_id`) VALUES ("09:00", "Period 1", @yr, @inst); 
INSERT INTO `sow_academic_year_period` (`time`, `name`, `academic_year`, `institute_id`) VALUES ("10:00", "Period 2", @yr, @inst); 
INSERT INTO `sow_academic_year_period` (`time`, `name`, `academic_year`, `institute_id`) VALUES ("11:00", "Break", @yr, @inst); 
INSERT INTO `sow_academic_year_period` (`time`, `name`, `academic_year`, `institute_id`) VALUES ("11:15", "Period 3", @yr, @inst); 
INSERT INTO `sow_academic_year_period` (`time`, `name`, `academic_year`, `institute_id`) VALUES ("12:15", "Lunch", @yr, @inst); 
INSERT INTO `sow_academic_year_period` (`time`, `name`, `academic_year`, `institute_id`) VALUES ("13:15", "Period 4", @yr, @inst); 
INSERT INTO `sow_academic_year_period` (`time`, `name`, `academic_year`, `institute_id`) VALUES ("14:15", "Period 5", @yr, @inst); 
INSERT INTO `sow_academic_year_period` (`time`, `name`, `academic_year`, `institute_id`) VALUES ("15:15", "Period 6", @yr, @inst); 
INSERT INTO `sow_academic_year_period` (`time`, `name`, `academic_year`, `institute_id`) VALUES ("16:15", "Homework club", @yr, @inst);
