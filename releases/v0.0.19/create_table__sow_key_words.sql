CREATE TABLE sow_key_word (
  id int(11) NOT NULL AUTO_INCREMENT,
  name varchar(100) NOT NULL,
  definition text NULL,
  `created` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  `created_by` int(10) unsigned NOT NULL DEFAULT '0',
  `published` tinyint(4) NOT NULL DEFAULT '1',
  PRIMARY KEY (`id`)
);
