ALTER TABLE sow_learning_episode
ADD COLUMN key_words TEXT NULL after topic_id;

ALTER TABLE sow_learning_episode
ADD COLUMN summary varchar(100) NULL after topic_id;