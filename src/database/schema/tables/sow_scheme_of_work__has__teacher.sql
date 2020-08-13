DROP TABLE IF EXISTS sow_scheme_of_work__has__teacher;

CREATE TABLE sow_scheme_of_work__has__teacher
(   scheme_of_work_id INT(11) NOT NULL, 
    auth_user_id INT(11) NOT NULL,
    PRIMARY KEY (scheme_of_work_id, auth_user_id),
    FOREIGN KEY (scheme_of_work_id) REFERENCES sow_scheme_of_work (id) ON DELETE CASCADE,
    FOREIGN KEY (auth_user_id) REFERENCES auth_user (id) ON DELETE CASCADE
);

-- add all users as teachers

INSERT INTO sow_scheme_of_work__has__teacher (scheme_of_work_id, auth_user_id)
SELECT sow_scheme_of_work.id, auth_user.id
FROM sow_scheme_of_work, auth_user
