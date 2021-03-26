ALTER TABLE `sow_key_stage` 
ADD COLUMN department_id INT after name,
-- ADD COLUMN pathway_template_id INT after name,
ADD COLUMN year_of_study INT DEFAULT 1 after name;

-- NEEDS REVISING OR MANUALLY

ALTER TABLE `sow_key_stage` 
ADD CONSTRAINT `fk_sow_key_stage__has__department`
  FOREIGN KEY (`department_id`)
  REFERENCES `sow_department` (`id`)
  ON DELETE CASCADE
  ON UPDATE CASCADE;
