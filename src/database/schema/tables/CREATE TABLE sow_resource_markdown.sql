
DROP TABLE `sow_resource_markdown`;

CREATE TABLE `sow_resource_markdown` (
  `resource_id` int NOT NULL,
  `markdown_content` text,
  PRIMARY KEY (`resource_id`)
);

ALTER TABLE `sow_resource_markdown` 
ADD CONSTRAINT ` fk_resource`
  FOREIGN KEY (`resource_id`)
  REFERENCES `drussell1974$cssow_api`.`sow_resource` (`id`)
  ON DELETE CASCADE
  ON UPDATE CASCADE;