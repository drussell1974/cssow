CREATE TABLE `sow_reference_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(15) NOT NULL,
  `created` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  `created_by` int(10) unsigned NOT NULL DEFAULT '0',
  `published` tinyint(4) NOT NULL DEFAULT '1',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

INSERT INTO sow_reference_type (name) VALUES ('Book'),('Video'),('Website');

CREATE TABLE `sow_learning_episode__has__references` (
  `reference_id` int(11) NOT NULL AUTO_INCREMENT,
  `learning_episode_id` int(11) NOT NULL,
  `page_notes` varchar(250) DEFAULT NULL,
  `page_uri` varchar(2083) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT '',
  PRIMARY KEY (`reference_id`,`learning_episode_id`),
  KEY `sow_learning_episode_has_references__has__learning_episode` (`learning_episode_id`),
  CONSTRAINT `sow_learning_episode_has_references__has__learning_episode` FOREIGN KEY (`learning_episode_id`) REFERENCES `sow_learning_episode` (`id`),
  CONSTRAINT `sow_learning_episode_has_references__has__reference` FOREIGN KEY (`reference_id`) REFERENCES `sow_reference` (`id`)
);


ALTER TABLE sow_reference
ADD COLUMN reference_type_id INT(11) NOT NULL after id;

ALTER TABLE sow_reference
ADD CONSTRAINT sow_reference__has__reference_type FOREIGN KEY (reference_type_id) REFERENCES sow_reference_type (id);


