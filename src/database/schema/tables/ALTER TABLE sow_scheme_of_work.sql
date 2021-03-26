ALTER TABLE `sow_scheme_of_work`
ADD COLUMN `study_duration` INT DEFAULT 1 after name,
ADD COLUMN `start_study_in_year` INT DEFAULT 1 after `study_duration`;