ALTER TABLE `sow_key_stage` 
ADD COLUMN department_id INT after name;

UPDATE sow_key_stage as ks
INNER JOIN sow_scheme_of_work as sow ON ks.id = sow.key_stage_id
SET ks.department_id = sow.department_id, created = '1999-12-31 23:59:59';

ALTER TABLE `sow_key_stage` 
ADD CONSTRAINT `fk_sow_key_stage__has__department`
  FOREIGN KEY (`department_id`)
  REFERENCES `sow_department` (`id`)
  ON DELETE CASCADE
  ON UPDATE CASCADE;

-- CREATE DEFAULT sow_key_stage for existing departments

