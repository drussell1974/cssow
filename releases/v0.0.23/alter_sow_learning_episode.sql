ALTER TABLE sow_learning_episode
ADD COLUMN related_topic_ids varchar(100) NULL after topic_id;

ALTER TABLE sow_learning_episode
MODIFY COLUMN related_topic_ids varchar(100) NULL default '';

SELECT * FROM sow_learning_episode;
ALTER TABLE sow_learning_episode
MODIFY COLUMN key_words varchar(1000) NULL default '',
MODIFY COLUMN summary varchar(100) NULL default '';

UPDATE sow_learning_episode
SET key_words = ''
WHERE key_words is null and id > 0;

UPDATE sow_learning_episode
SET related_topic_ids = ''
WHERE related_topic_ids is null and id > 0;

UPDATE sow_learning_episode
SET summary = ''
WHERE summary is null and id > 0;
