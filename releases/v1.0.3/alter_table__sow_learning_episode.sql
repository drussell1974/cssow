ALTER TABLE `sow_learning_episode`
ADD COLUMN year_id int(11) NOT NULL default 1,
ADD CONSTRAINT `sow_learning_episode__has__year_id` FOREIGN KEY (`year_id`) REFERENCES `sow_year` (`id`);