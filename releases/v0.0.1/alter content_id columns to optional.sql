ALTER TABLE `sow_learning_objective` 
MODIFY COLUMN `content_id` int(11) NULL;

UPDATE sow_learning_objective SET content_id = null WHERE content_id < 1;

DELETE from sow_content WHERE id < 1;