CREATE TABLE sow_learning_episode__has__topics (
 id INT(11) NOT NULL AUTO_INCREMENT,
 learning_episode_id INT(11) NOT NULL,
 topic_id INT(11) NOT NULL,
PRIMARY KEY (id),
UNIQUE INDEX (learning_episode_id, topic_id),
CONSTRAINT sow_learning_episode__has__topics__learning_episode_id FOREIGN KEY (learning_episode_id) REFERENCES sow_learning_episode (id),
CONSTRAINT sow_learning_episode__has__topics__topic_id FOREIGN KEY (topic_id) REFERENCES sow_topic (id)
);