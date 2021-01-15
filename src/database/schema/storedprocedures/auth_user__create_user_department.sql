DELIMITER $$

-- AFTER INSERT

DROP TRIGGER IF EXISTS `drussell1974$cssow_api`.`auth_user_AFTER_INSERT` $$

CREATE DEFINER = CURRENT_USER TRIGGER `drussell1974$cssow_api`.`auth_user_AFTER_INSERT` AFTER INSERT ON `auth_user` FOR EACH ROW
BEGIN
		INSERT INTO sow_department(name, head_id)
        VALUES (NEW.first_name, NEW.id);
        
        INSERT INTO sow_department__has__teacher (auth_user_id, department_id) 
        VALUES (NEW.id, last_insert_id());
END$$