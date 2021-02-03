DROP TABLE `sow_department`;

CREATE TABLE `sow_department` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(70) NOT NULL,
  `head_id` INT NOT NULL,
  `school_id` INT DEFAULT NULL,
  `created` datetime NOT NULL DEFAULT '1999-12-31 23:59:59',
  `created_by` int unsigned NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `name_UNIQUE` (`name`)
);

ALTER TABLE `sow_department` 
ADD CONSTRAINT `sow_department__has__teacher`
  FOREIGN KEY (`head_id`)
  REFERENCES `auth_user` (`id`)
  ON DELETE CASCADE
  ON UPDATE CASCADE;
  
INSERT INTO `sow_department` (`name`, `head_id`) 
SELECT `username`, `id` FROM `auth_user`;