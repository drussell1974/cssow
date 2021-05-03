SELECT * FROM drussell1974$cssow_api.sow_resource WHERE lesson_id NOT IN (SELECT id FROM sow_lesson);

ALTER TABLE `drussell1974$cssow_api`.`sow_resource` 
ADD INDEX `fk_sow_resource__has__lesson_idx` (`lesson_id` ASC) VISIBLE;
;
ALTER TABLE `drussell1974$cssow_api`.`sow_resource` 
ADD CONSTRAINT `fk_sow_resource__has__lesson`
  FOREIGN KEY (`lesson_id`)
  REFERENCES `drussell1974$cssow_api`.`sow_lesson` (`id`)
  ON DELETE CASCADE
  ON UPDATE RESTRICT;