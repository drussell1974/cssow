/*
ALTER TABLE sow_key_word ADD COLUMN scheme_of_work_id INT after definition;
ALTER TABLE sow_key_word ADD COLUMN published INT after scheme_of_work_id;

UPDATE sow_key_word as t1 
INNER JOIN sow_lesson__has__key_words as t2 ON t1.id = t2.key_word_id 
INNER JOIN sow_lesson as t3 ON t2.lesson_id = t3.id
SET t1.scheme_of_work_id = t3.scheme_of_work_id;

-- UPDATE sow_key_word SET scheme_of_work_id = 11, published = 0 WHERE scheme_of_work_id is NULL;

-- UPDATE sow_key_word SET published = 1 WHERE id IN (SELECT min(id) FROM sow_key_word GROUP BY name, scheme_of_work_id);
*/
ALTER TABLE sow_key_word DROP FOREIGN KEY sow_key_word_ibfk_1;
ALTER TABLE sow_key_word DROP FOREIGN KEY sow_scheme_of_work__has_keyword;
ALTER TABLE sow_key_word DROP FOREIGN KEY sow_key_word__has__scheme_of_work;
ALTER TABLE sow_key_word DROP FOREIGN KEY sow_key_word__has__sow_scheme_of_work;

ALTER TABLE sow_key_word 
ADD CONSTRAINT sow_key_word__has__sow_scheme_of_work
    FOREIGN KEY (scheme_of_work_id) REFERENCES sow_scheme_of_work (id) ON DELETE CASCADE;

ALTER TABLE sow_lesson__has__key_words DROP FOREIGN KEY sow_lesson__has__key_words__has__sow_key_words;
ALTER TABLE sow_lesson__has__key_words 
ADD CONSTRAINT sow_lesson__has__key_words__has__sow_key_words
    FOREIGN KEY (key_word_id) REFERENCES sow_key_word (id) ON DELETE CASCADE; 

CREATE TABLE IF NOT EXISTS sow_key_word__archive (
    id int,
    name varchar(100),
    definition text,
    scheme_of_work_id int
);

CREATE TABLE IF NOT EXISTS sow_lesson__has__key_words__archive (
    key_word_id INT,
    lesson_id INT
);