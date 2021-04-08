ALTER TABLE `sow_lesson_schedule`
ADD COLUMN `start_date` datetime DEFAULT CURRENT_TIMESTAMP after id,
ADD COLUMN `class_name` varchar(10) after id;