ALTER TABLE `sow_year`
ADD COLUMN `year_num` INT NOT NULL DEFAULT 1 AFTER `name`;

-- Manually update

ALTER TABLE `sow_year`
ADD UNIQUE INDEX `fk_sow_year__uidx` (`key_stage_id` ASC, `year_num` ASC);
