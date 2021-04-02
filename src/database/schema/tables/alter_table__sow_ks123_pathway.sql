ALTER TABLE sow_ks123_pathway 
ADD COLUMN department_id INT after objective;

UPDATE sow_ks123_pathway SET department_id = 2, created = '1999-12-13 23:59:59' WHERE id > 0;

ALTER TABLE `sow_ks123_pathway` 
ADD CONSTRAINT `fk_sow_ks123_pathway__has__department`
  FOREIGN KEY (`department_id`)
  REFERENCES `sow_department` (`id`)
  ON DELETE CASCADE
  ON UPDATE CASCADE;