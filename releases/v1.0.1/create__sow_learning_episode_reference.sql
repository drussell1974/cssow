#DROP TABLE sow_learning_episode_reference;
CREATE TABLE sow_learning_episode_reference (
  reference_id int(11) NOT NULL AUTO_INCREMENT,
  learning_episode_id int(11) NOT NULL,
  pages varchar(30) NULL,
  uri nvarchar(2083) NULL default '',
  PRIMARY KEY (reference_id, learning_episode_id),
  CONSTRAINT sow_learning_episode_reference__has__learning_episode FOREIGN KEY (learning_episode_id) REFERENCES sow_learning_episode (id),
  CONSTRAINT sow_learning_episode_reference__has__reference FOREIGN KEY (reference_id) REFERENCES sow_reference (id)
);
