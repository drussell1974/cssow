ALTER TABLE sow_learning_objective
MODIFY COLUMN key_words varchar(1000) NULL default '',
MODIFY COLUMN notes varchar(4000) NULL default '';

UPDATE sow_learning_objective
SET key_words = null
WHERE key_words = '' and id > 0;

UPDATE sow_learning_objective
SET notes = null
WHERE (notes = '') and id > 0;