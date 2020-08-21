ALTER TABLE sow_lesson ADD IF NOT EXISTS content_id int(11) NOT NULL default (0) after scheme_of_work_id;

