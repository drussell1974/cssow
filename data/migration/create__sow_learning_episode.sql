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