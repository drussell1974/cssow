ALTER TABLE `sow_lesson__has__key_words` 
DROP PRIMARY KEY,
ADD PRIMARY KEY (`key_word_id`, `lesson_id`),
DROP COLUMN key_word,
DROP COLUMN id
;
-- ADD INDEX `sow_lesson__has__keyword_idx` (`key_word_id` ASC, `lesson_id` ASC) VISIBLE;sow_lesson__has__key_words