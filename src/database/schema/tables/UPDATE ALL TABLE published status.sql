
ALTER TABLE sow_content MODIFY COLUMN published TINYINT DEFAULT 0;
UPDATE sow_content SET published = 64 WHERE published = 2 and id > 0;
UPDATE sow_content SET published = 32 WHERE published = 0 and id > 0;

ALTER TABLE `sow_content` 
ADD INDEX `fk_sow_content__has__created_by_user_idx` (`created_by` ASC),
ADD INDEX `fk_sow_content__has__modified_by_user_idx` (`modified_by` ASC);

ALTER TABLE sow_cs_concept MODIFY COLUMN published TINYINT DEFAULT 0;
UPDATE sow_cs_concept SET published = 64 WHERE published = 2 and id > 0;
UPDATE sow_cs_concept SET published = 32 WHERE published = 0 and id > 0;

ALTER TABLE `sow_cs_concept` 
ADD INDEX `fk_sow_cs_concept__has__created_by_user_idx` (`created_by` ASC),
ADD INDEX `fk_sow_cs_concept__has__modified_by_user_idx` (`modified_by` ASC);

ALTER TABLE sow_department MODIFY COLUMN published TINYINT DEFAULT 0;
UPDATE sow_department SET published = 64 WHERE published = 2 and id > 0;
UPDATE sow_department SET published = 32 WHERE published = 0 and id > 0;

ALTER TABLE `sow_department` 
ADD INDEX `fk_sow_department__has__created_by_user_idx` (`created_by` ASC),
ADD INDEX `fk_sow_department__has__modified_by_user_idx` (`modified_by` ASC);

ALTER TABLE sow_exam_board MODIFY COLUMN published TINYINT DEFAULT 0;
UPDATE sow_exam_board SET published = 64 WHERE published = 2 and id > 0;
UPDATE sow_exam_board SET published = 32 WHERE published = 0 and id > 0;

ALTER TABLE `sow_exam_board` 
ADD INDEX `fk_sow_exam_board__has__created_by_user_idx` (`created_by` ASC),
ADD INDEX `fk_sow_exam_board__has__modified_by_user_idx` (`modified_by` ASC);

ALTER TABLE sow_institute MODIFY COLUMN published TINYINT DEFAULT 0;
UPDATE sow_institute SET published = 64 WHERE published = 2 and id > 0;
UPDATE sow_institute SET published = 32 WHERE published = 0 and id > 0;

ALTER TABLE `sow_institute` 
ADD INDEX `fk_sow_institute__has__created_by_user_idx` (`created_by` ASC),
ADD INDEX `fk_sow_institute__has__modified_by_user_idx` (`modified_by` ASC);

ALTER TABLE sow_key_stage MODIFY COLUMN published TINYINT DEFAULT 0;
UPDATE sow_key_stage SET published = 64 WHERE published = 2 and id > 0;
UPDATE sow_key_stage SET published = 32 WHERE published = 0 and id > 0;

ALTER TABLE `sow_key_stage` 
ADD INDEX `fk_sow_key_stage__has__created_by_user_idx` (`created_by` ASC),
ADD INDEX `fk_ssow_key_stage__has__modified_by_user_idx` (`modified_by` ASC) ;

ALTER TABLE sow_key_word MODIFY COLUMN published TINYINT DEFAULT 0;
UPDATE sow_key_word SET published = 64 WHERE published = 2 and id > 0;
UPDATE sow_key_word SET published = 32 WHERE published = 0 and id > 0;

ALTER TABLE `sow_key_word` 
ADD INDEX `fk_sow_key_word__has__created_by_user_idx` (`created_by` ASC) ,
ADD INDEX `fk_sow_key_word__has__modified_by_user_idx` (`modified_by` ASC) ;

ALTER TABLE sow_ks123_pathway MODIFY COLUMN published TINYINT DEFAULT 0;
UPDATE sow_ks123_pathway SET published = 64 WHERE published = 2 and id > 0;
UPDATE sow_ks123_pathway SET published = 32 WHERE published = 0 and id > 0;

ALTER TABLE `sow_ks123_pathway` 
ADD INDEX `fk_sow_ks123_pathway__has__created_by_user_idx` (`created_by` ASC) ;

ALTER TABLE sow_learning_objective MODIFY COLUMN published TINYINT DEFAULT 0;
UPDATE sow_learning_objective SET published = 64 WHERE published = 2 and id > 0;
UPDATE sow_learning_objective SET published = 32 WHERE published = 0 and id > 0;

ALTER TABLE `sow_learning_objective` 
ADD INDEX `fk_sow_learning_objective__has__created_by_user_idx` (`created_by` ASC) ,
ADD INDEX `fk_sow_learning_objective__has__modified_by_user_idx` (`modified_by` ASC) ;

ALTER TABLE sow_learning_objective__has__lesson MODIFY COLUMN published TINYINT DEFAULT 0;
UPDATE sow_learning_objective__has__lesson SET published = 64 WHERE published = 2 and id > 0;
UPDATE sow_learning_objective__has__lesson SET published = 32 WHERE published = 0 and id > 0;

ALTER TABLE sow_lesson MODIFY COLUMN published TINYINT DEFAULT 0;
UPDATE sow_lesson SET published = 64 WHERE published = 2 and id > 0;
UPDATE sow_lesson SET published = 32 WHERE published = 0 and id > 0;

ALTER TABLE `sow_lesson` 
ADD INDEX `fk_sow_lesson__has__created_by_user_idx` (`created_by` ASC) ,
ADD INDEX `fk_sow_lesson__has__modified_by_user_idx` (`modified_by` ASC) ;

ALTER TABLE sow_menu MODIFY COLUMN published TINYINT DEFAULT 0;
UPDATE sow_menu SET published = 64 WHERE published = 2 and id > 0;
UPDATE sow_menu SET published = 32 WHERE published = 0 and id > 0;

ALTER TABLE `sow_menu` 
ADD INDEX `fk_sow_menu__has__created_by_user_idx` (`created_by` ASC) ,
ADD INDEX `fk_sow_menu__has__modified_by_user_idx` (`modified_by` ASC) ;

ALTER TABLE sow_play_based MODIFY COLUMN published TINYINT DEFAULT 0;
UPDATE sow_play_based SET published = 64 WHERE published = 2 and id > 0;
UPDATE sow_play_based SET published = 32 WHERE published = 0 and id > 0;

ALTER TABLE `sow_play_based` 
ADD INDEX `fk_sow_play_based__has__created_by_user_idx` (`created_by` ASC) ,
ADD INDEX `fk_sow_play_based__has__modified_by_user_idx` (`modified_by` ASC) ;

ALTER TABLE sow_resource MODIFY COLUMN published TINYINT DEFAULT 0;
UPDATE sow_resource SET published = 64 WHERE published = 2 and id > 0;
UPDATE sow_resource SET published = 32 WHERE published = 0 and id > 0;

ALTER TABLE `sow_resource` 
ADD INDEX `fk_sow_resource__has__created_by_user_idx` (`created_by` ASC) ,
ADD INDEX `fk_sow_resource__has__modified_by_user_idx` (`modified_by` ASC) ;

ALTER TABLE sow_resource_type MODIFY COLUMN published TINYINT DEFAULT 0;
UPDATE sow_resource_type SET published = 64 WHERE published = 2 and id > 0;
UPDATE sow_resource_type SET published = 32 WHERE published = 0 and id > 0;

ALTER TABLE `sow_resource_type` 
ADD INDEX `fk_sow_resource_type__has__created_by_user_idx` (`created_by` ASC) ,
ADD INDEX `fk_sow_resource_type__has__modified_by_user_idx` (`modified_by` ASC) ;

ALTER TABLE sow_scheme_of_work MODIFY COLUMN published TINYINT DEFAULT 0;
UPDATE sow_scheme_of_work SET published = 64 WHERE published = 2 and id > 0;
UPDATE sow_scheme_of_work SET published = 32 WHERE published = 0 and id > 0;

ALTER TABLE `sow_scheme_of_work` 
ADD INDEX `fk_sow_scheme_of_work__has__created_by_user_idx` (`created_by` ASC) ,
ADD INDEX `fk_sow_scheme_of_work__has__modified_by_user_idx` (`modified_by` ASC) ;

ALTER TABLE sow_solo_taxonomy MODIFY COLUMN published TINYINT DEFAULT 0;
UPDATE sow_solo_taxonomy SET published = 64 WHERE published = 2 and id > 0;
UPDATE sow_solo_taxonomy SET published = 32 WHERE published = 0 and id > 0;

ALTER TABLE `sow_solo_taxonomy` 
ADD INDEX `fk_sow_solo_taxonomy__has__created_by_user_idx` (`created_by` ASC) ,
ADD INDEX `fk_sow_solo_taxonomy__has__modified_by_user_idx` (`modified_by` ASC) ;

ALTER TABLE sow_subject_purpose MODIFY COLUMN published TINYINT DEFAULT 0;
UPDATE sow_subject_purpose SET published = 64 WHERE published = 2 and id > 0;
UPDATE sow_subject_purpose SET published = 32 WHERE published = 0 and id > 0;

ALTER TABLE `sow_subject_purpose` 
ADD INDEX `fk_sow_subject_purpose__has__created_by_user_idx` (`created_by` ASC) ,
ADD INDEX `fk_sow_subject_purpose__has__modified_by_user_idx` (`modified_by` ASC) ;

ALTER TABLE sow_topic MODIFY COLUMN published TINYINT DEFAULT 0;
UPDATE sow_topic SET published = 64 WHERE published = 2 and id > 0;
UPDATE sow_topic SET published = 32 WHERE published = 0 and id > 0;

ALTER TABLE `sow_topic` 
ADD INDEX `fk_sow_topic__has__created_by_user_idx` (`created_by` ASC) ,
ADD INDEX `fk_sow_topic__has__modified_by_user_idx` (`modified_by` ASC) ;

ALTER TABLE sow_year MODIFY COLUMN published TINYINT DEFAULT 0;
UPDATE sow_year SET published = 64 WHERE published = 2 and id > 0;
UPDATE sow_year SET published = 32 WHERE published = 0 and id > 0;

ALTER TABLE `sow_year` 
ADD INDEX `fk_sow_year__has__created_by_user_idx` (`created_by` ASC) ,
ADD INDEX `fk_sow_year__has__modified_by_user_idx` (`modified_by` ASC) ;