
ALTER TABLE sow_logging ADD COLUMN `scheme_of_work_id` int(11) NOT NULL DEFAULT 0;
ALTER TABLE sow_logging ADD COLUMN `message` varchar(50) DEFAULT NULL after scheme_of_work_id;
ALTER TABLE sow_logging ADD COLUMN `category` varchar(50) DEFAULT NULL after message;
ALTER TABLE sow_logging ADD COLUMN `subcategory` varchar(50) DEFAULT after category;
