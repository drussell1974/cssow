DROP TABLE `sow_learning_episode__has__references`;

CREATE TABLE `sow_learning_episode__has__references` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `reference_id` int(11) NOT NULL,
  `learning_episode_id` int(11) NOT NULL,
  `page_notes` varchar(250) DEFAULT NULL,
  `page_uri` varchar(2083) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT '',
  PRIMARY KEY (`id`),
  KEY `sow_learning_episode_has_references__has__learning_episode` (`learning_episode_id`),
  KEY `sow_learning_episode_has_references__has__reference` (`reference_id`),
  CONSTRAINT `sow_learning_episode_has_references__has__learning_episode` FOREIGN KEY (`learning_episode_id`) REFERENCES `sow_learning_episode` (`id`) ON DELETE CASCADE,
  CONSTRAINT `sow_learning_episode_has_references__has__reference` FOREIGN KEY (`reference_id`) REFERENCES `sow_reference` (`id`)
);