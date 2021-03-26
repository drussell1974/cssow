ALTER TABLE `sow_key_stage` 
ADD COLUMN department_id INT after name,
ADD COLUMN pathway_template_id INT after name,
ADD COLUMN year_of_study INT DEFAULT 1 after name;

-- NEEDS REVISING OR MANUALLY

-- UPDATE sow_key_stage as ks
-- INNER JOIN sow_scheme_of_work as sow ON ks.id = sow.key_stage_id
-- SET
-- ks.pathway_template_id = (SELECT pathway_template_id FROM sow_pathway_template_key_stages WHERE name = ks.name LIMIT 1), 
-- ks.department_id = sow.department_id,
-- ks.created = '1999-12-31 23:59:59';

ALTER TABLE `sow_key_stage` 
ADD CONSTRAINT `fk_sow_key_stage__has__department`
  FOREIGN KEY (`department_id`)
  REFERENCES `sow_department` (`id`)
  ON DELETE CASCADE
  ON UPDATE CASCADE;

ALTER TABLE `drussell1974$cssow_api`.`sow_key_stage` 
DROP FOREIGN KEY `fk_sow_key_stage__has__department`;

ALTER TABLE `drussell1974$cssow_api`.`sow_key_stage` 
DROP COLUMN `pathway_template_id`;

ALTER TABLE `drussell1974$cssow_api`.`sow_key_stage` 
DROP INDEX `fk_sow_key_stage__department_template_uidx`;


ALTER TABLE `drussell1974$cssow_api`.`sow_key_stage` 
ADD CONSTRAINT `fk_sow_key_stage__has__department`
  FOREIGN KEY (`department_id`)
  REFERENCES `drussell1974$cssow_api`.`sow_department` (`id`)
  ON DELETE CASCADE
  ON UPDATE CASCADE,
ADD CONSTRAINT `fk_sow_key_stage__has__pathway_template`
  FOREIGN KEY (`pathway_template_id`)
  REFERENCES `drussell1974$cssow_api`.`sow_pathway_template` (`id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;