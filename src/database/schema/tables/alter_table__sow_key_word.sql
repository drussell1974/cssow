
SET SQL_SAFE_UPDATES=0;
DELETE FROM sow_lesson__has__key_words WHERE key_word_id NOT IN (SELECT id FROM sow_key_word);
SET SQL_SAFE_UPDATES=1;

ALTER TABLE `sow_lesson__has__key_words` 
ADD CONSTRAINT `fk_sow_lesson__has__key_words__has__keyword`
  FOREIGN KEY (`key_word_id`)
  REFERENCES `sow_key_word` (`id`)
  ON DELETE CASCADE
  ON UPDATE CASCADE;
