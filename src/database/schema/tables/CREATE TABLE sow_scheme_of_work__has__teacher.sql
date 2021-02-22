#DROP TABLE IF EXISTS sow_scheme_of_work__has__teacher;

CREATE TABLE sow_scheme_of_work__has__teacher
(   
	scheme_of_work_id INT(11) NOT NULL, 
    auth_user_id INT(11) NOT NULL,
    department_permission INT(11) DEFAULT 0 NOT NULL,
    scheme_of_work_permission INT(11) DEFAULT 0 NOT NULL,
    lesson_permission INT(11) DEFAULT 0 NOT NULL,
    is_authorised BOOLEAN NOT NULL default False,
	created datetime DEFAULT CURRENT_TIMESTAMP,
	modified datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (scheme_of_work_id, auth_user_id),
    FOREIGN KEY (scheme_of_work_id) REFERENCES sow_scheme_of_work (id) ON DELETE CASCADE,
    FOREIGN KEY (auth_user_id) REFERENCES auth_user (id) ON DELETE CASCADE
);
