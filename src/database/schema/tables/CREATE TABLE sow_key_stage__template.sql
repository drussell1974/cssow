CREATE TABLE `sow_pathway_template` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `created` datetime DEFAULT CURRENT_TIMESTAMP,
  `created_by` int unsigned NOT NULL DEFAULT '0',
  `modified` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  `modified_by` int unsigned DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `fk_sow_pathway_template__has__created_by_user_idx` (`created_by`),
  KEY `fk_sow_pathway_template__has__modified_by_user_idx` (`modified_by`)
);


CREATE TABLE `sow_pathway_template_key_stages` (
  `id` int NOT NULL AUTO_INCREMENT,
  `show_order` int NOT NULL DEFAULT 1,	
  `name` varchar(20) NOT NULL,
  `pathway_template_id` INT NOT NULL,
  `created` datetime DEFAULT CURRENT_TIMESTAMP,
  `created_by` int unsigned NOT NULL DEFAULT '0',
  `modified` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  `modified_by` int DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `fk_sow_key_stage__has__created_by_user_idx` (`created_by`),
  KEY `fk_ssow_key_stage__has__modified_by_user_idx` (`modified_by`),
  CONSTRAINT `ssow_pathway_template_key_stages__has__pathway_template` FOREIGN KEY (`pathway_template_id`) REFERENCES `sow_pathway_template` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
);

	
ALTER TABLE `drussell1974$cssow_api`.`sow_pathway_template` 
ADD COLUMN `show_order` INT NOT NULL DEFAULT 1 AFTER `name`;


INSERT INTO `sow_pathway_template` (`id`, `name`, `show_order`) VALUES (3, 'GCSE', 5);
INSERT INTO `sow_pathway_template` (`id`, `name`, `show_order`) VALUES (4, 'BTEC', 7);
INSERT INTO `sow_pathway_template` (`id`, `name`, `show_order`) VALUES (5, 'KS3', 4);
INSERT INTO `sow_pathway_template` (`id`, `name`, `show_order`) VALUES (6, 'A-level', 6);

INSERT INTO `sow_pathway_template_key_stages` (`id`, `pathway_template_id`, `name`, `created_by`, `modified_by`) VALUES ('9', '3', 'KS1', '0', '0');
INSERT INTO `sow_pathway_template_key_stages` (`id`, `pathway_template_id`, `name`, `created_by`, `modified_by`) VALUES ('10', '3', 'KS2', '0', '0');
INSERT INTO `sow_pathway_template_key_stages` (`id`, `pathway_template_id`, `name`, `created_by`, `modified_by`) VALUES ('11', '3', 'KS3', '0', '0');
INSERT INTO `sow_pathway_template_key_stages` (`id`, `pathway_template_id`, `name`, `created_by`, `modified_by`) VALUES ('12', '3', 'KS4', '0', '0');

INSERT INTO `sow_pathway_template_key_stages` (`id`, `pathway_template_id`, `name`, `created_by`, `modified_by`) VALUES ('13', '5', 'KS1', '0', '0');
INSERT INTO `sow_pathway_template_key_stages` (`id`, `pathway_template_id`, `name`, `created_by`, `modified_by`) VALUES ('14', '5', 'KS2', '0', '0');
INSERT INTO `sow_pathway_template_key_stages` (`id`, `pathway_template_id`, `name`, `created_by`, `modified_by`) VALUES ('15', '5', 'KS3', '0', '0');

INSERT INTO `sow_pathway_template_key_stages` (`id`, `pathway_template_id`, `name`, `created_by`, `modified_by`) VALUES ('16', '6', 'KS1', '0', '0');
INSERT INTO `sow_pathway_template_key_stages` (`id`, `pathway_template_id`, `name`, `created_by`, `modified_by`) VALUES ('17', '6', 'KS2', '0', '0');
INSERT INTO `sow_pathway_template_key_stages` (`id`, `pathway_template_id`, `name`, `created_by`, `modified_by`) VALUES ('18', '6', 'KS3', '0', '0');
INSERT INTO `sow_pathway_template_key_stages` (`id`, `pathway_template_id`, `name`, `created_by`, `modified_by`) VALUES ('19', '6', 'KS4', '0', '0');
INSERT INTO `sow_pathway_template_key_stages` (`id`, `pathway_template_id`, `name`, `created_by`, `modified_by`) VALUES ('20', '6', 'KS5', '0', '0');
-- DELETE FROM `sow_pathway_template_key_stages` WHERE (`id` = '5');

INSERT INTO `sow_pathway_template_key_stages` (`id`, `pathway_template_id`, `name`, `created_by`, `modified_by`) VALUES ('21', '4', 'KS1', '0', '0');
INSERT INTO `sow_pathway_template_key_stages` (`id`, `pathway_template_id`, `name`, `created_by`, `modified_by`) VALUES ('22', '4', 'KS2', '0', '0');
INSERT INTO `sow_pathway_template_key_stages` (`id`, `pathway_template_id`, `name`, `created_by`, `modified_by`) VALUES ('23', '4', 'KS3', '0', '0');
INSERT INTO `sow_pathway_template_key_stages` (`id`, `pathway_template_id`, `name`, `created_by`, `modified_by`) VALUES ('24', '4', 'KS4', '0', '0');
INSERT INTO `sow_pathway_template_key_stages` (`id`, `pathway_template_id`, `name`, `created_by`, `modified_by`) VALUES ('25', '4', 'KS5', '0', '0');



ALTER TABLE `drussell1974$cssow_api`.`sow_pathway_template_key_stages` 
ADD INDEX `cssow_pathway_template_key_stages__has__pathway_template` (`pathway_template_id` ASC);
;
ALTER TABLE `drussell1974$cssow_api`.`sow_pathway_template_key_stages` 
ADD CONSTRAINT `cssow_pathway_template_key_stages__has__pathway_template`
  FOREIGN KEY (`pathway_template_id`)
  REFERENCES `drussell1974$cssow_api`.`sow_pathway_template` (`id`)
  ON DELETE CASCADE
  ON UPDATE CASCADE;

