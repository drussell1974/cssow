ALTER TABLE `sow_learning_episode__has__topics`
DROP FOREIGN KEY `sow_learning_episode__has__topics__learning_episode_id`;

ALTER TABLE `sow_learning_episode__has__topics` 
ADD CONSTRAINT `sow_learning_episode__has__topics__learning_episode_id` FOREIGN KEY (`learning_episode_id`) REFERENCES `sow_learning_episode` (`id`)  ON DELETE CASCADE;
