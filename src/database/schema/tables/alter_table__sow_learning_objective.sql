ALTER TABLE sow_learning_objective 
ADD COLUMN missing_words_challenge varchar(140) NOT NULL default ('') after notes;
