INSERT INTO sow_learning_objective (id, description, solo_taxonomy_id, topic_id, content_id, exam_board_id)
SELECT id, description, solo_taxonomy_id, topic_id, content_id, exam_board_id FROM sow_learning_objective_imported WHERE id NOT IN
(SELECT id FROM sow_learning_objective);