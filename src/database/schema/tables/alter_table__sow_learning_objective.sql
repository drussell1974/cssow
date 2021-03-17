-- ALTER TABLE sow_learning_objective 
-- ADD COLUMN missing_words_challenge varchar(140) NOT NULL default ('') after notes;
ALTER TABLE `sow_learning_objective` 
DROP FOREIGN KEY `fk_sow_learning_objective_content`;

ALTER TABLE `sow_learning_objective` 
ADD CONSTRAINT `fk_sow_learning_objective_content`
  FOREIGN KEY (`content_id`)
  REFERENCES `drussell1974$cssow_api`.`sow_content` (`id`)
  ON DELETE CASCADE
  ON UPDATE CASCADE;
