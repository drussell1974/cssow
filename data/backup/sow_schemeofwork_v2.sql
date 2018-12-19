ALTER TABLE `sow_scheme_of_work`
  ADD COLUMN `key_stage_id` int(11) NOT NULL AFTER `name`,
  ADD COLUMN `exam_board_id` int(11) NOT NULL AFTER `key_stage_id`,
  ADD COLUMN `description` text NULL AFTER `name`,
  ADD CONSTRAINT `sow_scheme_of_work__has__key_stage` FOREIGN KEY (`key_stage_id`) REFERENCES `sow_key_stage` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `sow_scheme_of_work__has__year` FOREIGN KEY (`exam_board_id`) REFERENCES `sow_exam_board` (`id`) ON DELETE CASCADE;
  
ALTER TABLE `sow_scheme_of_work`
  ADD COLUMN `description` text NULL AFTER `name`;
