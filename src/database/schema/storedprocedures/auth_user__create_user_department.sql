DELIMITER $$

-- AFTER INSERT

DROP TRIGGER IF EXISTS `auth_user_AFTER_INSERT` $$

CREATE DEFINER = CURRENT_USER TRIGGER `auth_user_AFTER_INSERT` AFTER INSERT ON `auth_user` FOR EACH ROW
BEGIN
		INSERT INTO sow_department(name, head_id)
        VALUES (NEW.first_name, NEW.id);
        
        INSERT INTO sow_department__has__teacher (auth_user_id, department_id) 
        VALUES (NEW.id, last_insert_id());
END$$