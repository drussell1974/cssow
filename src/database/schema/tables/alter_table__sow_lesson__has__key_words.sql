ALTER TABLE sow_lesson__has__key_words
DROP COLUMN id;

ALTER TABLE sow_lesson__has__key_words
ADD PRIMARY KEY(key_word_id, lesson_id);
	
ALTER TABLE sow_lesson__has__key_words
DROP COLUMN key_word;

SET SQL_SAFE_UPDATES=0;
DELETE FROM sow_lesson__has__key_words WHERE key_word_id NOT IN (SELECT id FROM sow_key_word);

SET SQL_SAFE_UPDATES=1;

ALTER TABLE sow_lesson__has__key_words
ADD CONSTRAINT sow_lesson_has_keyword__has__key_word
    FOREIGN KEY (key_word_id) REFERENCES sow_key_word (id) ON DELETE CASCADE;