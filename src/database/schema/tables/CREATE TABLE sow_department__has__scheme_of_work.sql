CREATE TABLE `sow_department__has__scheme_of_work` (
  `scheme_of_work_id` INT NOT NULL,
  `department_id` INT(11) NOT NULL,
  PRIMARY KEY (`scheme_of_work_id`, `department_id`),
  INDEX `fk_sow_department__has__scheme_of_work__has__department_id` (`department_id` ASC),
  CONSTRAINT `fk_sow_department__has__scheme_of_work__has__department_id`
    FOREIGN KEY (`department_id`)
    REFERENCES `sow_department` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_sow_department__has__scheme_of_work__has__scheme_of_work_id`
    FOREIGN KEY (`scheme_of_work_id`)
    REFERENCES `sow_scheme_of_work` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);

INSERT INTO `sow_department__has__scheme_of_work` (`department_id`, `scheme_of_work_id`) 
SELECT dep.`id`, sow.`id` 
FROM `sow_department` as dep 
INNER JOIN `sow_scheme_of_work` as sow ON dep.`head_id` = sow.`created_by`;