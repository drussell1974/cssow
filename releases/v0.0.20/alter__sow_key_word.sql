ALTER TABLE sow_key_word
ADD COLUMN topic_id int NULL,
ADD CONSTRAINT fk_topic_id
FOREIGN KEY (topic_id) REFERENCES sow_topic(id);