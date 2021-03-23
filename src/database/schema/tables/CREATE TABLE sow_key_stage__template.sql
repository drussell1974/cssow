CREATE TABLE `sow_delivery_template` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `created` datetime DEFAULT CURRENT_TIMESTAMP,
  `created_by` int unsigned NOT NULL DEFAULT '0',
  `modified` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  `modified_by` int unsigned DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `fk_sow_delivery_template__has__created_by_user_idx` (`created_by`),
  KEY `fk_sow_delivery_template__has__modified_by_user_idx` (`modified_by`)
);


CREATE TABLE `sow_delivery_template_key_stages` (
  `id` int NOT NULL AUTO_INCREMENT,
  `delivery_template_id` int NOT NULL,
  `name` varchar(20) NOT NULL,
  `created` datetime DEFAULT CURRENT_TIMESTAMP,
  `created_by` int unsigned NOT NULL DEFAULT '0',
  `modified` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  `modified_by` int DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `fk_sow_key_stage__has__created_by_user_idx` (`created_by`),
  KEY `fk_ssow_key_stage__has__modified_by_user_idx` (`modified_by`),
  CONSTRAINT `ssow_delivery_template_key_stages__has__delivery_template` FOREIGN KEY (`delivery_template_id`) REFERENCES `sow_delivery_template` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
);

INSERT INTO `drussell1974$cssow_api`.`sow_delivery_template` (`name`) VALUES ('GCSE');

INSERT INTO sow_delivery_template_key_stages (delivery_template_id, name)
SELECT last_insert_id(), name FROM sow_key_stage WHERE department_id = 5;

INSERT INTO `drussell1974$cssow_api`.`sow_delivery_template` (`name`) VALUES ('BTEC');

INSERT INTO sow_delivery_template_key_stages (delivery_template_id, name)
SELECT last_insert_id(), name FROM sow_key_stage WHERE department_id = 2;
