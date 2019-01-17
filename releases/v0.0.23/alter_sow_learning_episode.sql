ALTER TABLE sow_learning_episode
ADD COLUMN related_topic_ids varchar(100) NULL after topic_id;

ALTER TABLE sow_learning_episode
MODIFY COLUMN related_topic_ids varchar(100) NULL;

ALTER TABLE sow_learning_episode
MODIFY COLUMN key_words varchar(1000) NULL,
MODIFY COLUMN summary varchar(100) NULL;

UPDATE sow_learning_episode
SET key_words = null
WHERE (key_words = '') and id > 0;

UPDATE sow_learning_episode
SET related_topic_ids = null
WHERE (related_topic_ids = '') and id > 0;

UPDATE sow_learning_episode
SET summary = null
WHERE (summary = '') and id > 0;
