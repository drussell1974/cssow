UPDATE sow_content SET created = '1999-12-31 23:59:59' WHERE id < 57;

-- ALTER TABLE `drussell1974$cssow_api`.`sow_content` 
-- MODIFY COLUMN modified DATETIME DEFAULT CURRENT_TIMESTAMP;
-- DROP FOREIGN KEY `fk_sow_content_key_stage`;
ALTER TABLE `drussell1974$cssow_api`.`sow_content` 
DROP FOREIGN KEY `fk_sow_content_key_stage`;
ALTER TABLE `drussell1974$cssow_api`.`sow_content` 
ADD CONSTRAINT `fk_sow_content_key_stage`
  FOREIGN KEY (`key_stage_id`)
  REFERENCES `drussell1974$cssow_api`.`sow_key_stage` (`id`)
  ON DELETE CASCADE
  ON UPDATE RESTRICT;


SELECT * FROM sow_content WHERE key_stage_id NOT IN (SELECT id FROM sow_key_stage);