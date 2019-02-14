ALTER TABLE `sow_learning_episode__has__pathway` 
DROP FOREIGN KEY `sow_learning_objective__has__pathway_le`;


ALTER TABLE `sow_learning_episode__has__pathway`
ADD CONSTRAINT `sow_learning_objective__has__pathway_le` FOREIGN KEY (`learning_episode_id`) REFERENCES `sow_learning_episode` (`id`) ON DELETE CASCADE;
