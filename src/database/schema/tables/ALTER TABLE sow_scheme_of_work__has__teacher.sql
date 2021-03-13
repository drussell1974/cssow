ALTER TABLE `drussell1974$cssow_api`.`sow_scheme_of_work__has__teacher` 
CHANGE COLUMN `is_authorised` `is_authorised` TINYINT(1) NOT NULL DEFAULT '0' ,
DROP PRIMARY KEY,
ADD PRIMARY KEY (`scheme_of_work_id`, `auth_user_id`, `is_authorised`);
;
