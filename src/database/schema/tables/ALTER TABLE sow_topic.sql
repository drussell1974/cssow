ALTER TABLE `sow_topic` 
ADD COLUMN department_id INT NOT NULL DEFAULT 5,
ADD CONSTRAINT `fk_sow_topic__has__department_id`
  FOREIGN KEY (`department_id`)
  REFERENCES `sow_department` (`id`)
  ON DELETE CASCADE
  ON UPDATE CASCADE;
