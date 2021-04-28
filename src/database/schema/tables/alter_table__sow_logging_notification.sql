ALTER TABLE `drussell1974$cssow_api`.`sow_logging_notification`
CHANGE COLUMN `message` `message` VARCHAR(135) NULL DEFAULT NULL,
ADD UNIQUE INDEX `uix_sow_logging_notification_message` (`message` ASC);
;