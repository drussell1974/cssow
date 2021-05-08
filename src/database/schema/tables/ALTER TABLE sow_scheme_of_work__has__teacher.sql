ALTER TABLE `sow_scheme_of_work__has__teacher` DROP foreign key `scheme_of_work_permission__has__teacher_join_code`;
ALTER TABLE `sow_department__has__teacher` DROP foreign key `department_permission__has__teacher_join_code`;

ALTER TABLE `sow_scheme_of_work__has__teacher` 
DROP COLUMN `join_code`,
DROP COLUMN `email`;
-- DROP COLUMN `is_authorised`;

ALTER TABLE `sow_department__has__teacher` 
DROP COLUMN `join_code`,
DROP COLUMN `email`;

-- CREATE

ALTER TABLE `drussell1974$cssow_api`.`sow_scheme_of_work__has__teacher` 
ADD COLUMN `join_code` CHAR(8) NOT NULL DEFAULT '' after auth_user_id,
ADD COLUMN `email` VARCHAR(254) NOT NULL DEFAULT '' after auth_user_id
;

ALTER TABLE `drussell1974$cssow_api`.`sow_department__has__teacher` 
ADD COLUMN `join_code` CHAR(8) NOT NULL DEFAULT '' after auth_user_id,
ADD COLUMN `email` VARCHAR(254) NOT NULL DEFAULT '' after auth_user_id
;

SET SQL_SAFE_UPDATES=0;

UPDATE sow_scheme_of_work__has__teacher as T1
INNER JOIN auth_user as T2 ON T1.auth_user_id = T2.id
SET T1.email = T2.email 
WHERE T1.auth_user_id = T2.id;

UPDATE sow_department__has__teacher as T1
INNER JOIN auth_user as T2 ON T1.auth_user_id = T2.id
SET T1.email = T2.email 
WHERE T1.auth_user_id = T2.id;

SET SQL_SAFE_UPDATES=1;

DROP TABLE `sow_teacher_join_code`;

CREATE TABLE `sow_teacher_join_code` (
  `join_code` char(8) NOT NULL,
  `email` varchar(254) NOT NULL,
  `auth_user_id` int NULL,
  `is_authorised` BOOLEAN NOT NULL DEFAULT TRUE,
  PRIMARY KEY (`join_code`)
);

INSERT INTO sow_teacher_join_code (join_code, email, auth_user_id, is_authorised)
SELECT CONCAT(
	substring('ABCDEFGHIJKLMNOPQRSTUVWXYZ', FLOOR(RAND()*25), 1),
    substring('ABCDEFGHIJKLMNOPQRSTUVWXYZ', FLOOR(RAND()*25), 1),
    substring('ABCDEFGHIJKLMNOPQRSTUVWXYZ', FLOOR(RAND()*25), 1),
    substring('ABCDEFGHIJKLMNOPQRSTUVWXYZ', FLOOR(RAND()*25), 1),
	substring('ABCDEFGHIJKLMNOPQRSTUVWXYZ', FLOOR(RAND()*25), 1),
    substring('ABCDEFGHIJKLMNOPQRSTUVWXYZ', FLOOR(RAND()*25), 1),
    substring('ABCDEFGHIJKLMNOPQRSTUVWXYZ', FLOOR(RAND()*25), 1),
    substring('ABCDEFGHIJKLMNOPQRSTUVWXYZ', FLOOR(RAND()*25), 1)
    ) AS join_code,
    email as email,
    auth_user_id as auth_user_id,
    TRUE as is_authorised
FROM sow_department__has__teacher;


SET SQL_SAFE_UPDATES=0;
UPDATE sow_teacher_join_code SET is_authorised = True;
SET SQL_SAFE_UPDATES=1;

SET SQL_SAFE_UPDATES=0;

UPDATE sow_scheme_of_work__has__teacher as T1
INNER JOIN sow_teacher_join_code as T2 ON T1.email = T2.email
SET T1.join_code = T2.join_code 
WHERE T1.email = T2.email;

UPDATE sow_department__has__teacher as T1
INNER JOIN sow_teacher_join_code as T2 ON T1.email = T2.email
SET T1.join_code = T2.join_code 
WHERE T1.email = T2.email;

SET SQL_SAFE_UPDATES=1;

ALTER TABLE sow_scheme_of_work__has__teacher
ADD CONSTRAINT `scheme_of_work__has__teacher_join_code` FOREIGN KEY (`join_code`) REFERENCES `sow_teacher_join_code` (`join_code`) ON UPDATE CASCADE ON DELETE CASCADE;

ALTER TABLE sow_department__has__teacher
ADD CONSTRAINT `department__has__teacher_join_code` FOREIGN KEY (`join_code`) REFERENCES `sow_teacher_join_code` (`join_code`) ON UPDATE CASCADE ON DELETE CASCADE;

SELECT * FROM sow_scheme_of_work__has__teacher;

ALTER TABLE sow_scheme_of_work__has__teacher DROP FOREIGN KEY sow_scheme_of_work__has__teacher_ibfk_2; -- find name of fk to sow_scheme_of_work
ALTER TABLE sow_scheme_of_work__has__teacher DROP FOREIGN KEY sow_scheme_of_work__has__teacher_ibfk_1; -- find name of fk to 
ALTER TABLE sow_department__has__teacher DROP FOREIGN KEY fk_sow_department__has__teacher__has__auth_user_id;

ALTER TABLE `sow_department__has__teacher`
DROP PRIMARY KEY,
DROP COLUMN `auth_user_id`;

ALTER TABLE `sow_department__has__teacher` 
ADD PRIMARY KEY(department_id, join_code);

ALTER TABLE `sow_scheme_of_work__has__teacher` 
DROP COLUMN `auth_user_id`,
DROP COLUMN `is_authorised`,
DROP PRIMARY KEY,
ADD PRIMARY KEY (`scheme_of_work_id`, `join_code`);
;

SELECT * FROM sow_scheme_of_work__has__teacher WHERE join_code = 'LBXPHSVB';
SELECT * FROM drussell1974$cssow_api.sow_teacher_join_code;

UPDATE sow_department__has__teacher SET join_code = 'LBXPHSVC' WHERE join_code = 'LBXPHSVB' and created_by = 4;

SELECT * FROM auth_user WHERE id IN (4, 11);


ALTER TABLE sow_scheme_of_work__has__teacher
ADD CONSTRAINT `scheme_of_work__has__teacher_scheme_of_work` FOREIGN KEY (`scheme_of_work_id`) 
REFERENCES `sow_scheme_of_work` (`id`) ON UPDATE CASCADE ON DELETE CASCADE;

ALTER TABLE sow_scheme_of_work__has__teacher
ADD CONSTRAINT `scheme_of_work_permission__has__teacher_join_code` FOREIGN KEY (`join_code`) 
REFERENCES `sow_teacher_join_code` (`join_code`) ON UPDATE CASCADE ON DELETE CASCADE;
