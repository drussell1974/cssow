ALTER TABLE sow_learning_objective
ADD COLUMN parent_id INT(11) NULL;

ALTER TABLE sow_learning_objective
ADD CONSTRAINT fk_sow_learning_objective_parent_id
    FOREIGN KEY (parent_id)
    REFERENCES sow_learning_objective (id);