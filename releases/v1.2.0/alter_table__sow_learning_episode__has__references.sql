ALTER TABLE sow_learning_episode__has__references
ADD COLUMN task_icon varchar(80) NULL default '' after page_uri;

ALTER TABLE sow_learning_episode__has__references
CHANGE COLUMN pageurl page_url varchar(2083);

ALTER TABLE sow_reference
CHANGE COLUMN uri url varchar(2083);