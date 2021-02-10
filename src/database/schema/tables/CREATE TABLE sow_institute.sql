ALTER TABLE `sow_department`
DROP CONSTRAINT sow_department__has__institute;

DROP TABLE `sow_institute`;

CREATE TABLE `sow_institute` (
  `id` int NOT NULL auto_increment,
  `name` varchar(70) NOT NULL,
  `created` datetime NOT NULL DEFAULT '1999-12-31 23:59:59',
  `created_by` int unsigned NOT NULL DEFAULT '0',
  `published` int unsigned NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `name_UNIQUE` (`name`)
);

ALTER TABLE sow_department MODIFY COLUMN institute_id INT;

ALTER TABLE sow_department MODIFY COLUMN published tinyint unsigned NOT NULL DEFAULT '0';

-- INSERT Insert id from departments
INSERT INTO sow_institute (id, name)
SELECT dep.institute_id, usr.first_name FROM sow_department as dep inner join auth_user as usr on usr.id = dep.head_id;

ALTER TABLE `sow_department` 
ADD CONSTRAINT `sow_department__has__institute`
  FOREIGN KEY (`institute_id`)
  REFERENCES `sow_institute` (`id`)
  ON DELETE CASCADE
  ON UPDATE CASCADE;
  