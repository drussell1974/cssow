ALTER TABLE sow_logging
ADD COLUMN action VARCHAR(2083) after message;

CREATE TABLE `sow_logging_notification` (
  `user_id` int NOT NULL,
  `logging_id` int NOT NULL,
  PRIMARY KEY (`user_id`, `logging_id`)
);

ALTER TABLE `sow_logging_notification` 
ADD CONSTRAINT `fk_sow_logging_notification__has__user`
  FOREIGN KEY (`user_id`)
  REFERENCES `auth_user` (`id`)
  ON DELETE CASCADE
  ON UPDATE CASCADE,
ADD CONSTRAINT `fk_sow_logging_notification__has__logging`
  FOREIGN KEY (`logging_id`)
  REFERENCES `sow_logging` (`id`)
  ON DELETE CASCADE
  ON UPDATE CASCADE;

ALTER TABLE sow_logging_notification
ADD COLUMN `start_date` datetime DEFAULT CURRENT_TIMESTAMP;

ALTER TABLE sow_logging_notification
ADD COLUMN message VARCHAR(30) after logging_id,
ADD COLUMN action VARCHAR(2083) after message;

ALTER TABLE sow_logging
DROP COLUMN action;
