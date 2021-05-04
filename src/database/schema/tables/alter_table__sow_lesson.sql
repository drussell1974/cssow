ALTER TABLE `sow_lesson` 
DROP FOREIGN KEY `sow_learning_episode__has__year_id`;
ALTER TABLE `drussell1974$cssow_api`.`sow_lesson` 
ADD CONSTRAINT `sow_lesson__has__year_id`
  FOREIGN KEY (`year_id`)
  REFERENCES `drussell1974$cssow_api`.`sow_year` (`id`)
  ON DELETE CASCADE
  ON UPDATE RESTRICT;
