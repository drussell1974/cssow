ALTER TABLE `sow_topic` 
ADD COLUMN department_id INT NOT NULL DEFAULT 2 after lvl,
ADD CONSTRAINT `fk_sow_topic__has__department_id`
  FOREIGN KEY (`department_id`)
  REFERENCES `sow_department` (`id`)
  ON DELETE CASCADE
  ON UPDATE CASCADE;

ALTER TABLE `drussell1974$cssow_api`.`sow_topic` 
DROP FOREIGN KEY `fk_sow_topic__has__parent_topic_id`;

ALTER TABLE `drussell1974$cssow_api`.`sow_topic` 
ADD CONSTRAINT `fk_sow_topic__has__parent_topic_id`
  FOREIGN KEY (`parent_id`)
  REFERENCES `drussell1974$cssow_api`.`sow_topic` (`id`)
  ON DELETE CASCADE
  ON UPDATE CASCADE;
