CREATE TABLE `sow_learning_objective__has__learning_episode` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `learning_objective_id` int(11) DEFAULT NULL,
  `learning_episode_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `sow_learning_episode__unique__idx` (`learning_objective_id`,`learning_episode_id`),
  KEY `learning_objective_id__idx` (`learning_objective_id`),
  KEY `learning_episode_id__idx` (`learning_episode_id`),
  CONSTRAINT `sow_learning_objective__has__learning_episode_ibfk_1` FOREIGN KEY (`learning_objective_id`) REFERENCES `sow_learning_objective` (`id`) ON DELETE CASCADE,
  CONSTRAINT `sow_learning_objective__has__learning_episode_ibfk_2` FOREIGN KEY (`learning_episode_id`) REFERENCES `sow_learning_episode` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=669 DEFAULT CHARSET=utf8;
