CREATE TABLE IF NOT EXISTS `sow_learning_episode` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `order_of_delivery_id` int(11) DEFAULT NULL,
  `scheme_of_work_id` int(11) DEFAULT NULL,
  `created` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  `created_by` int(10) unsigned NOT NULL DEFAULT '0',
  `published` tinyint(4) NOT NULL DEFAULT '1',
  PRIMARY KEY (`id`),
  KEY `scheme_of_work_id__idx` (`scheme_of_work_id`),
  CONSTRAINT `sow_learning_episode_ibfk_1` FOREIGN KEY (`scheme_of_work_id`) REFERENCES `sow_scheme_of_work` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

ALTER TABLE `sow_learning_episode`
  ADD COLUMN `created` datetime NOT NULL DEFAULT '0000-00-00 00:00:00' after scheme_of_work_id,
  ADD COLUMN `created_by` int(10) unsigned NOT NULL DEFAULT '0' after created,
  ADD COLUMN `published` tinyint(4) NOT NULL DEFAULT '1' after created_by;
    
CREATE TABLE `sow_learning_objective__has__learning_episode` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `learning_objective_id` int(11) DEFAULT NULL,
  `learning_episode_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `sow_learning_episode__unique__idx` (`learning_objective_id`, `learning_episode_id`),
  CONSTRAINT `sow_learning_objective__has__learning_episode_ibfk_1` FOREIGN KEY (`learning_objective_id`) REFERENCES `sow_learning_objective` (`id`) ON DELETE CASCADE,
  CONSTRAINT `sow_learning_objective__has__learning_episode_ibfk_2` FOREIGN KEY (`learning_episode_id`) REFERENCES `sow_learning_episode` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;
