ALTER TABLE `sow_topic` 
MODIFY COLUMN created DATETIME DEFAULT CURRENT_TIMESTAMP,
MODIFY COLUMN modified DATETIME ON UPDATE CURRENT_TIMESTAMP after created_by,
ADD INDEX `fk_sow_topic__has__created_by_user_idx` (`created_by` ASC) VISIBLE,
ADD INDEX `fk_sow_topic__has__modified_by_user_idx` (`modified_by` ASC) VISIBLE,
ADD CONSTRAINT `fk_sow_topic__has__parent_topic_id`
  FOREIGN KEY (`parent_id`)
  REFERENCES `sow_topic` (`id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;
