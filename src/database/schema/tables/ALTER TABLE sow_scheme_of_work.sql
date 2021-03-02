ALTER TABLE `sow_scheme_of_work` 
ADD INDEX `fk_sow_scheme_of_work__has__created_by_user_idx` (`created_by` ASC);

ALTER TABLE `sow_scheme_of_work` 
ADD INDEX `fk_sow_scheme_of_work__has__modified_by_user_idx` (`modified_by` ASC);

ALTER TABLE `sow_scheme_of_work` 
ADD CONSTRAINT `fk_sow_scheme_of_work__has__created_by_user`
  FOREIGN KEY (`created_by`)
  REFERENCES `auth_user` (`id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;

ALTER TABLE `sow_scheme_of_work` 
ADD CONSTRAINT `fk_sow_scheme_of_work__has__modified_by_user`
  FOREIGN KEY (`modified_by`)
  REFERENCES `auth_user` (`id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;
