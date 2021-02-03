
ALTER TABLE `drussell1974$cssow_api`.`sow_scheme_of_work` 
CHANGE COLUMN `created` `created` DATETIME NOT NULL DEFAULT '1999-12-31 23:59:59' ;

ALTER TABLE sow_scheme_of_work ADD COLUMN department_id INT(11) after exam_board_id;

ALTER TABLE `sow_scheme_of_work` 
ADD CONSTRAINT `sow_scheme_of_work__has__department`
  FOREIGN KEY (`department_id`)
  REFERENCES `sow_department` (`id`)
  ON DELETE CASCADE
  ON UPDATE CASCADE;

SET SQL_SAFE_UPDATES = 0;
UPDATE sow_scheme_of_work as sow
SET sow.department_id = sow.created_by; 
SET SQL_SAFE_UPDATES = 1;
