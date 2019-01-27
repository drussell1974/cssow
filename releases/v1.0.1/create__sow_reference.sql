#DROP TABLE sow_reference;
CREATE TABLE sow_reference (
  id int(11) NOT NULL AUTO_INCREMENT,
  title varchar(300) NOT NULL,
  authors nvarchar(200) NULL default '',
  publisher nvarchar(70) NOT NULL,
  year_published int(4) NOT NULL,
  uri nvarchar(2083) NULL default '',
  last_accessed datetime NULL DEFAULT '0000-00-00 00:00:00',
  scheme_of_work_id int(11) NOT NULL,
  created datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  created_by int(10) unsigned NOT NULL DEFAULT '0',
  published tinyint(4) NOT NULL DEFAULT '1',
  PRIMARY KEY (`id`),
  CONSTRAINT sow_reference__has__scheme_of_work FOREIGN KEY (scheme_of_work_id) REFERENCES sow_scheme_of_work (id)
);

