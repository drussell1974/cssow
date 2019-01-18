ALTER TABLE sow_learning_objective
MODIFY COLUMN key_words varchar(1000) NULL default '',
MODIFY COLUMN notes varchar(4000) NULL default '';

SELECT * FROM sow_learning_objective;

UPDATE sow_learning_objective
SET key_words = ''
WHERE (key_words is null) and id > 0;

UPDATE sow_learning_objective
SET notes = ''
WHERE (notes is null) and id > 0;