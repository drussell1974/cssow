'ALTER TABLE sow_learning_episode
DROP COLUMN short_title;'

ALTER TABLE sow_learning_episode
ADD COLUMN short_title VARCHAR(25) NOT NULL default '' after id;