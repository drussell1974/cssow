ALTER TABLE sow_lesson__has__key_words
DROP COLUMN id;

ALTER TABLE sow_lesson__has__key_words
ADD PRIMARY KEY(key_word_id, lesson_id);
	
ALTER TABLE sow_lesson__has__key_words
DROP COLUMN key_word;
