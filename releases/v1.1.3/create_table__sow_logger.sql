CREATE TABLE `sow_logging` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `details` text,
  `created` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  PRIMARY KEY (`id`)
)