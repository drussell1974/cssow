ALTER TABLE sow_key_word ADD COLUMN scheme_of_work_id INT after definition;

UPDATE sow_key_word as t1 
INNER JOIN sow_lesson__has__key_words as t2 ON t1.id = t2.key_word_id 
INNER JOIN sow_lesson as t3 ON t2.lesson_id = t3.id
SET t1.scheme_of_work_id = t3.scheme_of_work_id;

UPDATE sow_key_word SET scheme_of_work_id = 11, published = 0 WHERE scheme_of_work_id is NULL;

UPDATE sow_key_word SET published = 1 WHERE id IN (SELECT min(id) FROM sow_key_word GROUP BY name, scheme_of_work_id);

ALTER TABLE sow_key_word 
ADD CONSTRAINT
    FOREIGN KEY (scheme_of_work_id) REFERENCES sow_scheme_of_work (id) ON DELETE CASCADE;