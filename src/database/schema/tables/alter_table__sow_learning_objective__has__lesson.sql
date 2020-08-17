ALTER TABLE sow_learning_objective__has__lesson ADD IF NOT EXISTS (published tinyint(4) NOT NULL default (1));
