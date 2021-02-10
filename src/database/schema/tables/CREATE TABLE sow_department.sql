DROP TABLE `sow_department`;

CREATE TABLE `sow_department` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(70) NOT NULL,
  `head_id` INT NOT NULL,
  `institute_id` INT DEFAULT NULL,
  `created` datetime NOT NULL DEFAULT '1999-12-31 23:59:59',
  `created_by` int unsigned NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `name_UNIQUE` (`name`, `institute_id`)
);

ALTER TABLE `sow_department` 
ADD CONSTRAINT `sow_department__has__teacher`
  FOREIGN KEY (`head_id`)
  REFERENCES `auth_user` (`id`)
  ON DELETE CASCADE
  ON UPDATE CASCADE;

ALTER TABLE `sow_department`
   DROP INDEX name_UNIQUE, 
   ADD UNIQUE KEY `name_UNIQUE` (`name`, `institute_id`);

ALTER TABLE sow_department RENAME COLUMN school_id TO institute_id;