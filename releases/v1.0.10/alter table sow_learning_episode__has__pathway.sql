ALTER TABLE `sow_learning_episode__has__pathway` 
DROP FOREIGN KEY `sow_learning_objective__has__pathway_le`;

ALTER TABLE `sow_learning_episode__has__pathway`
ADD CONSTRAINT `sow_learning_objective__has__pathway_le` FOREIGN KEY (`learning_episode_id`) REFERENCES `sow_learning_episode` (`id`) ON DELETE CASCADE;


ALTER TABLE `sow_learning_episode__has__ks123_pathway`
DROP FOREIGN KEY fk_sow_learning_episode__has__ks123_pathway__learning_obje_id;

ALTER TABLE `sow_learning_episode__has__ks123_pathway`
ADD CONSTRAINT `fk_sow_learning_episode__has__ks123_pathway__learning_obje_id` FOREIGN KEY (`learning_episode_id`) REFERENCES `sow_learning_episode` (`id`) ON DELETE CASCADE;


ALTER TABLE `sow_learning_episode__has__references`
DROP FOREIGN KEY sow_learning_episode_has_references__has__learning_episode;

ALTER TABLE `sow_learning_episode__has__references`
ADD CONSTRAINT `sow_learning_episode_has_references__has__learning_episode` FOREIGN KEY (`learning_episode_id`) REFERENCES `sow_learning_episode` (`id`) ON DELETE CASCADE;


ALTER TABLE `sow_learning_episode__has__topics` 
DROP FOREIGN KEY sow_learning_episode__has__topics__learning_episode_id;

ALTER TABLE `sow_learning_episode__has__topics` 
ADD CONSTRAINT `sow_learning_episode__has__topics__learning_episode_id` FOREIGN KEY (`learning_episode_id`) REFERENCES `sow_learning_episode` (`id`) ON DELETE CASCADE;

