ALTER TABLE `drussell1974$cssow_api`.`sow_lesson` 
DROP FOREIGN KEY `sow_lesson_has_scheme_of_work`;
ALTER TABLE `drussell1974$cssow_api`.`sow_lesson` 
ADD CONSTRAINT `sow_lesson_has_scheme_of_work`
  FOREIGN KEY (`scheme_of_work_id`)
  REFERENCES `drussell1974$cssow_api`.`sow_scheme_of_work` (`id`)
  ON DELETE CASCADE
  ON UPDATE RESTRICT;
