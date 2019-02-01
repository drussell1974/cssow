CREATE TABLE `sow_reference_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(15) NOT NULL,
  `created` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  `created_by` int(10) unsigned NOT NULL DEFAULT '0',
  `published` tinyint(4) NOT NULL DEFAULT '1',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

INSERT INTO sow_reference_type (name) VALUES ('Book'),('Video'),('Website');

ALTER TABLE sow_reference
ADD COLUMN reference_type_id INT(11) NOT NULL after id;

ALTER TABLE sow_reference
ADD CONSTRAINT sow_reference__has__reference_type FOREIGN KEY (reference_type_id) REFERENCES sow_reference_type (id);
