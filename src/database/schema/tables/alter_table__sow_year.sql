SELECT * FROM sow_year WHERE key_stage_id NOT IN (SELECT id FROM sow_key_stage);

ALTER TABLE `sow_year` 
ADD INDEX `fk_sow_year__has__key_stage_idx` (`key_stage_id` ASC);
;
ALTER TABLE `sow_year` 
ADD CONSTRAINT `fk_sow_year__has__key_stage`
  FOREIGN KEY (`key_stage_id`)
  REFERENCES `sow_key_stage` (`id`)
  ON DELETE CASCADE
  ON UPDATE RESTRICT;