CREATE TABLE `sow_learning_episode__has__ks123_pathway` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `learning_episode_id` int(11) NOT NULL,
  `ks123_pathway_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_sow_learning_episode__has__ks123_pathway__learning_obje_idx` (`learning_episode_id`),
  KEY `fk_sow_learning_episode__has__ks123_pathway__ks123_pathway_idx` (`ks123_pathway_id`),
  CONSTRAINT `fk_sow_learning_episode__has__ks123_pathway__learning_obje_id` FOREIGN KEY (`learning_episode_id`) REFERENCES `sow_learning_episode` (`id`),
  CONSTRAINT `fk_sow_learning_episode__has__ks123_pathway__ks123_pathway_id` FOREIGN KEY (`ks123_pathway_id`) REFERENCES `sow_ks123_pathway` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE sow_learning_objective__has__ks123_pathway;