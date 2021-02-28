DELIMITER //

DROP PROCEDURE IF EXISTS lesson_learning_objective__get_all_pathway_objectives;

CREATE PROCEDURE lesson_learning_objective__get_all_pathway_objectives (
 IN p_key_stage_id INT,
 IN p_auth_user INT)
BEGIN
    SELECT 
		lob.id as id, 
		lob.description as description, 
		solo.id as solo_id, 
		solo.name as solo_taxonomy_name, 
		solo.lvl as solo_taxonomy_level,
		cnt.id as content_id, 
		cnt.description as content_description, 
		ks.id as key_stage_id, 
		ks.name as key_stage_name, 
		lob.key_words as key_words, 
		lob.group_name as group_name, 
		lob.created as created, 
		lob.created_by as created_by_id,
		user.first_name as created_by_name
    FROM sow_learning_objective as lob 
        LEFT JOIN sow_topic as top ON top.id = lob.topic_id 
        LEFT JOIN sow_topic as pnt_top ON pnt_top.id = top.parent_id 
        LEFT JOIN sow_solo_taxonomy as solo ON solo.id = lob.solo_taxonomy_id 
        LEFT JOIN sow_content as cnt ON cnt.id = lob.content_id 
        LEFT JOIN sow_key_stage as ks ON ks.id = cnt.key_stage_id 
        LEFT JOIN auth_user as user ON user.id = lob.created_by 
    WHERE ks.id < p_key_stage_id 
    ORDER BY ks.name DESC, solo.lvl;
END;
//

DELIMITER ;DELIMITER //

DROP PROCEDURE IF EXISTS department__get_context_model;

CREATE PROCEDURE department__get_context_model (
 IN p_department_id INT,
 IN p_institute_id INT)
BEGIN
	/* return data for lightweight Context model (id, name, parent_id, created_by, published) */
    SELECT 
        dep.id as id,
        dep.name as term,
		dep.institute_id as parent_id,
        dep.created_by as created_by,
        dep.published as published
    FROM 
        sow_department as dep
    WHERE
        dep.id = p_department_id
        AND dep.institute_id = p_institute_id;
END;
//

DELIMITER ;

CALL department__get_context_model(2, 5);DELIMITER //

DROP PROCEDURE IF EXISTS keyword__update;

CREATE PROCEDURE keyword__update (
 IN p_keyword_id INT,
 IN p_name VARCHAR(100),
 IN p_defintion TEXT,
 IN p_scheme_of_work_id INT,
 IN p_published INT,
 IN p_auth_user INT)
BEGIN
    UPDATE sow_key_word 
    SET
        name = p_name, 
        definition = p_defintion,
        scheme_of_work_id = p_scheme_of_work_id,
        published = p_published,
        modified_by = p_auth_user
    WHERE id = p_keyword_id;
END;
//

DELIMITER ;DELIMITER //

DROP PROCEDURE IF EXISTS scheme_of_work__get_all;

CREATE PROCEDURE scheme_of_work__get_all (
 IN p_key_stage_id INT,
 IN p_department_id INT,
 IN p_institute_id INT,
 IN p_show_published_state INT,
 IN p_auth_user INT)
BEGIN
    SELECT 
        sow.id as id,
        sow.name as name,
        sow.description as description,
        sow.exam_board_id as exam_board_id,
        exam.name as exam_board_name,
        sow.key_stage_id as key_stage_id,
        kys.name as key_stage_name,
        dep.id as department_id,
        dep.name as department_name,
        sow.created as created,
        sow.created_by as created_by_id,
        user.first_name as created_by_name,
        sow.published as published
    FROM sow_scheme_of_work as sow
        INNER JOIN sow_department as dep ON dep.id = sow.department_id	
        LEFT JOIN sow_exam_board as exam ON exam.id = sow.exam_board_id
        INNER JOIN sow_key_stage as kys ON kys.id = sow.key_stage_id
        INNER JOIN auth_user as user ON user.id = sow.created_by
    WHERE 
		sow.department_id = p_department_id 
		AND (sow.key_stage_id = p_key_stage_id or p_key_stage_id = 0)
        AND (p_show_published_state % sow.published = 0 #323 use p_show_published_state and remove subquery 
			or sow.created_by = p_auth_user)
    ORDER BY sow.key_stage_id;
END;
//

DELIMITER ;

CALL scheme_of_work__get_all(0,5,2,2,1);DELIMITER //
DROP PROCEDURE IF EXISTS lesson_learning_objective__delete_unpublished;

CREATE PROCEDURE lesson_learning_objective__delete_unpublished (
 IN p_scheme_of_work_id INT,
 IN p_lesson_id INT,
 IN p_auth_user INT)
BEGIN
    DELETE sow_learning_objective__has__lesson
    FROM sow_learning_objective__has__lesson 
    INNER JOIN sow_lesson AS l ON l.id = sow_learning_objective__has__lesson.lesson_id
    WHERE
        sow_learning_objective__has__lesson.published IN (32,64)
        AND l.scheme_of_work_id = p_scheme_of_work_id
        AND l.id = p_lesson_id;
END;
//

DELIMITER ;

DELIMITER //

DROP PROCEDURE IF EXISTS keyword__insert;

CREATE PROCEDURE keyword__insert (
 OUT p_institute_id INT,
 IN p_name VARCHAR(100)
 )
BEGIN
    INSERT INTO sow_institute
    (
        name, 
        definition,
        scheme_of_work_id,
        created,
        created_by,
        published
    ) 
    VALUES
    (
        p_name, 
        p_definition,
        p_scheme_of_work_id,
        NOW(),
        p_auth_user,
        p_published
    );

    SELECT LAST_INSERT_ID();
END;
//

DELIMITER ;DELIMITER //

DROP PROCEDURE IF EXISTS institute__get;

CREATE PROCEDURE institute__get (
 IN p_institute_id INT,
 IN p_auth_user INT)
BEGIN
    SELECT 
        ins.id as id,
        ins.name as name,
        ins.created as created,
        ins.created_by as created_by,
        usr.first_name as created_by_name,
        ins.published as published
    FROM 
        sow_institute as ins
        INNER JOIN auth_user as usr ON usr.id = ins.created_by
    WHERE
        ins.id = p_institute_id;
	-- ORDER BY ins.name;
END;
//

DELIMITER ;

CALL institute__get(2,2);DELIMITER //

DROP PROCEDURE IF EXISTS scheme_of_work__get_key_stage_id_only;

CREATE PROCEDURE scheme_of_work__get_key_stage_id_only (
 IN p_scheme_of_work_id INT,
 IN p_department_id INT,
 IN p_institute_id INT,
 IN p_auth_user INT)
BEGIN
    SELECT   
      sow.key_stage_id as key_stage_id  
    FROM sow_scheme_of_work as sow  
    LEFT JOIN auth_user as user ON user.id = sow.created_by  
      WHERE sow.department_id = p_department_id 
        AND sow.id = p_scheme_of_work_id 
        AND (sow.published = 1 
              or p_auth_user IN (SELECT auth_user_id 
                              FROM sow_teacher 
                              WHERE auth_user_id = p_auth_user AND scheme_of_work_id = sow.id)
        );
END;
//

DELIMITER ;DELIMITER //

DROP PROCEDURE IF EXISTS scheme_of_work__get_options;

CREATE PROCEDURE scheme_of_work__get_options (
 IN p_department_id INT,
 IN p_institute_id INT,
 IN p_show_published_state INT,
 IN p_auth_user INT
)
BEGIN
    SELECT 
        sow.id as id, 
        sow.name as name, 
        ks.name as key_stage_name 
    FROM sow_scheme_of_work as sow 
        LEFT JOIN sow_key_stage as ks ON ks.id = sow.key_stage_id 
    WHERE 
        sow.department_id = p_department_id 
        AND (p_show_published_state % sow.published = 0 #323 use p_show_published_state and remove subquery 
			or sow.created_by = p_auth_user)
	ORDER BY sow.key_stage_id;
END;
//

DELIMITER ;DELIMITER //

DROP PROCEDURE IF EXISTS ks123_pathway__get_options;

CREATE PROCEDURE ks123_pathway__get_options (
 IN p_key_stage_id INT,
 IN p_topic_id INT,
 IN p_show_published_state INT,
 IN p_auth_user INT)
BEGIN
    SELECT 
        pw.id, CONCAT(ks.name, " ", pw.objective)
    FROM 
        sow_ks123_pathway as pw
        INNER JOIN sow_year as yr ON yr.id = pw.year_id
        INNER JOIN sow_key_stage as ks ON ks.id = yr.key_stage_id
    WHERE 
        yr.key_stage_id BETWEEN p_key_stage_id - 2 and p_key_stage_id and 
        pw.topic_id = p_topic_id and
        (p_show_published_state % pw.published = 0 
			or pw.created_by = p_auth_user
        );
END;
//

DELIMITER ;

CALL ks123_pathway__get_options(4, 4, 1, 2);DELIMITER //

DROP PROCEDURE IF EXISTS department__delete;

CREATE PROCEDURE department__delete (
 OUT p_department_id INT,
 IN p_auth_user INT)
BEGIN
    DELETE FROM sow_department
    WHERE id = p_department_id and head_id = p_auth_user;
END;
//

DELIMITER ;DELIMITER //

DROP PROCEDURE IF EXISTS content__delete;

CREATE PROCEDURE content__delete (
 IN p_content_id INT,
 IN p_remove_published_state INT,
 IN p_auth_user INT)
BEGIN
    DELETE FROM sow_content 
    WHERE id = p_content_id 
		AND published = p_remove_published_state;
END;
//

DELIMITER ;DELIMITER //

DROP PROCEDURE IF EXISTS department__update;

CREATE PROCEDURE department__update (
 IN p_department_id INT,
 IN p_name VARCHAR(100),
 IN p_institute_id INT,
 IN p_published INT,
 IN p_auth_user INT)
BEGIN
    UPDATE sow_department
    SET
        name = p_name,
        institute_id = p_institute_id,
        published = p_published,
        modified_by = p_auth_user
    WHERE id = p_department_id;
END;
//

DELIMITER ;DELIMITER //

DROP PROCEDURE IF EXISTS lesson_resource__delete_unpublished;

CREATE PROCEDURE lesson_resource__delete_unpublished (
 IN p_lesson_id INT,
 IN p_auth_user INT)
BEGIN
  DELETE FROM sow_resource 
  WHERE lesson_id = p_lesson_id
    AND published IN (32,64);
END;
//

DELIMITER ;DELIMITER //

DROP PROCEDURE IF EXISTS department__get_context_name;

CREATE PROCEDURE department__get_context_name (
 IN p_department_id INT,
 IN p_institute_id INT,
 IN p_auth_user_id INT)
BEGIN
    SELECT 
      dep.name as department_name
	FROM sow_department as dep
	WHERE dep.id = p_department_id and dep.institute_id = p_institute_id
    LIMIT 1;
END;
//

DELIMITER ;

CALL department__get_context_name(1,5,2);DELIMITER //

DROP PROCEDURE IF EXISTS institute__update;

CREATE PROCEDURE institute__update (
 IN p_institute_id INT,
 IN p_name VARCHAR(100),
 IN p_teacher_id INT,
 IN p_published INT,
 IN p_auth_user INT)
BEGIN
    UPDATE sow_institute
    SET
        name = p_name, 
        head_id = p_teacher_id,
        published = p_published,
        modified_by = p_auth_user
    WHERE id = p_institute_id;
END;
//

DELIMITER ;DELIMITER //

DROP PROCEDURE IF EXISTS content__delete_unpublished;

CREATE PROCEDURE content__delete_unpublished (
 IN p_scheme_of_work_id INT,
 IN p_remove_published_state INT,
 IN p_auth_user INT)
BEGIN
    DELETE sow_content
    FROM sow_content
    INNER JOIN sow_scheme_of_work as sow ON sow.key_stage_id = sow_content.key_stage_id
    WHERE 
		sow.id = p_scheme_of_work_id
		AND sow_content.published = p_remove_published_state;
END;
//

DELIMITER ;DELIMITER //

DROP PROCEDURE IF EXISTS lesson__get_by_keyword;

CREATE PROCEDURE lesson__get_by_keyword (
 IN p_key_word_id INT,
 IN p_scheme_of_work_id INT,
 IN p_show_published_state INT,
 IN p_auth_user INT)
BEGIN
     SELECT  
        le.id as id, 
        le.title as title, 
        le.order_of_delivery_id as order_of_delivery_id, 
        le.scheme_of_work_id as scheme_of_work_id, 
        sow.name as scheme_of_work_name, 
        le.content_id as content_id,
        cnt.description as content_description,
        top.id as topic_id, 
        top.name as topic_name, 
        pnt_top.id as parent_topic_id, 
        pnt_top.name as parent_topic_name, 
        sow.key_stage_id as key_stage_id, 
        yr.id as year_id, yr.name as year_name, 
        le.summary as summary, 
        le.created as created, 
        le.created_by as created_by_id, 
        user.first_name as created_by_name, 
        le.published as published 
    FROM sow_lesson as le  
    INNER JOIN sow_lesson__has__key_words as lkw ON lkw.lesson_id = le.id
    INNER JOIN sow_scheme_of_work as sow ON sow.id = le.scheme_of_work_id 
    INNER JOIN sow_year as yr ON yr.id = le.year_id 
    LEFT JOIN sow_topic as top ON top.id = le.topic_id  
    LEFT JOIN sow_topic as pnt_top ON pnt_top.id = top.parent_id  
    LEFT JOIN sow_content as cnt ON cnt.id = le.content_id
    LEFT JOIN auth_user as user ON user.id = sow.created_by  
    WHERE 
		lkw.key_word_id = p_key_word_id
        AND 
        le.scheme_of_work_id = p_scheme_of_work_id
        AND (p_show_published_state % sow.published = 0 
				or p_show_published_state % le.published = 0 
                or sow.created_by = p_auth_user 
				or le.created_by = p_auth_user 
			)
    ORDER BY le.year_id, le.order_of_delivery_id;
END;
//

DELIMITER ;DELIMITER //

DROP PROCEDURE IF EXISTS scheme_of_work__get_context_model;

CREATE PROCEDURE scheme_of_work__get_context_model (
 IN p_scheme_of_work_id INT)
BEGIN
	/* return data for lightweight Context model (id, name, parent_id, created_by, published) */
    SELECT
        sow.id as id,
        sow.name as name,  
        sow.department_id as parent_id,
        sow.created_by as created_by_id,
        sow.published as published
    FROM sow_scheme_of_work as sow
	WHERE sow.id = p_scheme_of_work_id  
	;
END;
//

DELIMITER ;
CALL scheme_of_work__get_context_model(11);DELIMITER //

DROP PROCEDURE IF EXISTS scheme_of_work__get_schemeofwork_name_only;

CREATE PROCEDURE scheme_of_work__get_schemeofwork_name_only (
 IN p_scheme_of_work_id INT,
 IN p_department_id INT,
 IN p_institute_id INT,
 IN p_show_published_state INT,
 IN p_auth_user INT)
BEGIN
    SELECT
      sow.name as name
    FROM sow_scheme_of_work as sow
    LEFT JOIN auth_user as user ON user.id = sow.created_by
      WHERE
        sow.id = p_scheme_of_work_id 
        AND sow.department_id = p_department_id
        AND (p_show_published_state % sow.published = 0 
                or sow.created_by = p_auth_user
          );
END;
//

DELIMITER ;DELIMITER //

DROP PROCEDURE IF EXISTS lesson_learning_objective__get;

CREATE PROCEDURE lesson_learning_objective__get (
 IN p_learning_objective_id INT,
 IN p_auth_user INT)
BEGIN
    SELECT 
        lob.id as id, 
        lob.description as description, 
        solo.id as solo_id, 
        solo.name as solo_taxonomy_name, 
        solo.lvl as solo_taxonomy_level, 
        cnt.id as content_id, cnt.description as content_description, 
        le.id as lesson_id, 
        sow.key_stage_id as key_stage_id, 
        ks.name as key_stage_name, 
        lob.key_words as key_words, 
        lob.notes as notes, 
        lob.group_name as group_name, 
        lob.created as created, 
        lob.created_by as created_by_id, 
        user.first_name as created_by_name,  
        le_lo.published as published      
    FROM sow_scheme_of_work as sow 
        INNER JOIN sow_lesson as le ON le.scheme_of_work_id = sow.id
        INNER JOIN sow_learning_objective__has__lesson as le_lo ON le_lo.lesson_id = le.id
        INNER JOIN sow_learning_objective as lob ON lob.id = le_lo.learning_objective_id 
        LEFT JOIN sow_key_stage as ks ON ks.id = sow.key_stage_id 
        LEFT JOIN sow_solo_taxonomy as solo ON solo.id = lob.solo_taxonomy_id 
        LEFT JOIN sow_content as cnt ON cnt.id = lob.content_id 
        LEFT JOIN auth_user as user ON user.id = lob.created_by 
    WHERE lob.id = p_learning_objective_id
        AND (lob.published = 1
        or p_auth_user IN (SELECT auth_user_id 
                        FROM sow_teacher 
                        WHERE auth_user_id = p_auth_user AND scheme_of_work_id = sow.id)
        );
END;
//

DELIMITER ;DELIMITER //

DROP PROCEDURE IF EXISTS lesson_keyword__delete_unpublished;

CREATE PROCEDURE lesson_keyword__delete_unpublished (
 IN p_scheme_of_work_id INT,
 IN p_lesson_id INT,
 IN p_auth_user INT)
BEGIN
	DELETE FROM sow_lesson__has__key_words
    WHERE lesson_id = p_lesson_id 
		AND key_word_id IN (
			SELECT id FROM sow_key_word
			WHERE scheme_of_work_id = p_scheme_of_work_id 
					AND published IN (32,64) 
					AND p_auth_user IN 
							(SELECT auth_user_id 
							FROM sow_teacher 
							WHERE scheme_of_work_id = p_scheme_of_work_id)
			);
END;
//

DELIMITER ;DELIMITER //

DROP PROCEDURE IF EXISTS keyword__get;

CREATE PROCEDURE keyword__get (
 IN p_keyword_id INT,
 IN p_scheme_of_work_id INT,
 IN p_show_published_state INT,
 IN p_auth_user INT)
BEGIN
    SELECT 
        id as id,
        name as term,
        kw.definition as definition,
        kw.scheme_of_work_id as scheme_of_work_id,
        kw.published as published,
        kw.created as created
    FROM 
        sow_key_word as kw
    WHERE
        kw.id = p_keyword_id 
        AND kw.scheme_of_work_id = p_scheme_of_work_id
        AND (p_show_published_state % kw.published = 0
			or kw.created_by = p_auth_user)
	ORDER BY kw.name;
END;
//

DELIMITER ;DELIMITER //

DROP PROCEDURE IF EXISTS lesson_resource__get;

CREATE PROCEDURE lesson_resource__get (
 IN p_resource_id INT,
 IN p_show_published_state INT,
 IN p_auth_user INT)
BEGIN
    SELECT 
        res.id as id, 
        res.title as title, 
        res.publisher as publisher, 
        res.type_id as type_id, 
        res_typ.name as resource_type_name, 
        res_typ.task_icon as task_icon, 
        res.md_document_name as md_document_name,
        res.page_notes as page_notes,
        res.url as page_uri,  
        res.lesson_id as lesson_id,
        res.created as created,
        res.created_by as created_by_id,
        user.first_name as created_by_name,
        res.published as published
    FROM sow_resource AS res
      INNER JOIN sow_lesson as les ON les.id = res.lesson_id  
      INNER JOIN sow_scheme_of_work as sow ON sow.id = les.scheme_of_work_id
      LEFT JOIN sow_resource_type as res_typ ON res.type_id = res_typ.id
      LEFT JOIN auth_user AS user ON user.id = res.created_by
    WHERE res.id = p_resource_id  
        AND (p_show_published_state % res.published = 0 
             or res.created_by = p_auth_user
		 );
END;
//

DELIMITER ;DELIMITER //

DROP PROCEDURE IF EXISTS institute__get_number_of_departments;

CREATE PROCEDURE institute__get_number_of_departments (
 IN p_institute_id INT,
 IN p_auth_user INT)
BEGIN
    SELECT 
        count(id)
    FROM 
        sow_department
    WHERE
		institute_id = p_institute_id and (
	    published = 1 or p_auth_user IN (SELECT auth_user_id 
                                FROM sow_teacher 
	 							WHERE auth_user_id = p_auth_user));
END;
//

DELIMITER ;DELIMITER //

DROP PROCEDURE IF EXISTS scheme_of_work__get;

CREATE PROCEDURE scheme_of_work__get (
 IN p_scheme_of_work_id INT,
 IN p_department_id INT,
 IN p_institute_id INT,
 IN p_show_published_state INT,
 IN p_auth_user INT)
BEGIN
    SELECT
        sow.id as id,
        sow.name as name,  
        sow.description as description,
        sow.exam_board_id as exam_board_id,
        exam.name as exam_board_name,  
        sow.key_stage_id as key_stage_id,
        kys.name as key_stage_name,
        dep.id as department_id,
        dep.name as department_name,
        sow.created as created,
        sow.created_by as created_by_id,
        user.first_name as created_by_name,
        sow.published as published
    FROM sow_scheme_of_work as sow  
        LEFT JOIN sow_department as dep ON dep.id = sow.department_id
        LEFT JOIN sow_exam_board as exam ON exam.id = sow.exam_board_id
        INNER JOIN sow_key_stage as kys ON kys.id = sow.key_stage_id
        INNER JOIN auth_user as user ON user.id = sow.created_by   
    WHERE sow.department_id = p_department_id
        AND sow.id = p_scheme_of_work_id 
        AND (p_show_published_state % sow.published = 0 #323 use p_show_published_state and remove subquery 
			or sow.created_by = p_auth_user
        );
END;
//

DELIMITER ;DELIMITER //

DROP PROCEDURE IF EXISTS content__get_all;

CREATE PROCEDURE content__get_all (
 IN p_scheme_of_work_id INT,
 IN p_key_stage_id INT,
 IN p_auth_user INT)
BEGIN
    SELECT 
        id as id, 
        description as description, 
        letter as letter_prefix, 
        published as published 
    FROM sow_content 
    WHERE
        key_stage_id = p_key_stage_id 
        AND (published = 1 or
             p_auth_user IN 
                    (SELECT auth_user_id 
                    FROM sow_teacher 
                    WHERE scheme_of_work_id = p_scheme_of_work_id)
        )
    ORDER BY letter ASC;
END;
//

DELIMITER ;DELIMITER //

DROP PROCEDURE IF EXISTS lesson_resource__delete;

CREATE PROCEDURE lesson_resource__delete (
 IN p_resource_id INT,
 IN p_auth_user INT)
BEGIN
  DELETE FROM sow_resource WHERE id = p_resource_id AND published IN (32,64);
END;
//

DELIMITER ;DELIMITER //

DROP PROCEDURE IF EXISTS keyword__delete_unpublished;

CREATE PROCEDURE keyword__delete_unpublished (
 IN p_scheme_of_work_id INT,
 IN p_auth_user INT)
BEGIN
    DELETE FROM sow_key_word
    WHERE scheme_of_work_id = p_scheme_of_work_id 
            AND published IN (32,64) 
            AND p_auth_user IN 
                    (SELECT auth_user_id 
                    FROM sow_teacher 
                    WHERE scheme_of_work_id = p_scheme_of_work_id);

END;
//

DELIMITER ;DELIMITER //

DROP PROCEDURE IF EXISTS department__get_options;

CREATE PROCEDURE department__get_options (
 IN p_auth_user INT)
BEGIN
    SELECT 
        id, 
        name 
    FROM sow_department as dep
    INNER JOIN sow_department__has__teacher as dep_teach
		ON dep_teach.department_id = dep.id
    WHERE dep_teach.created_by = p_auth_user;
END;
//

DELIMITER ;
DELIMITER //

DROP PROCEDURE IF EXISTS department__get_all;

CREATE PROCEDURE department__get_all (
 IN p_institute_id INT,
 IN p_show_published_state INT,
 IN p_auth_user INT)
BEGIN
    SELECT 
        dep.id as id,
        dep.name as name,
        dep.institute_id as institute_id,
        dep.created as created,
        dep.created_by as created_by,
        usr.first_name as created_by_name,
        dep.published as published
    FROM 
        sow_department as dep
        INNER JOIN auth_user as usr ON usr.id = dep.created_by
    WHERE 
		dep.institute_id = p_institute_id 
        and (p_show_published_state % published = 0 
			or dep.created_by = p_auth_user)
    ORDER BY dep.name;
END;
//

DELIMITER ;

CALL department__get_all(2,32, 2);DELIMITER //

DROP PROCEDURE IF EXISTS institute__delete;

CREATE PROCEDURE institute__delete (
 OUT p_institute_id INT,
 IN p_auth_user INT)
BEGIN
    DELETE FROM sow_institute
    WHERE id = p_institute_id and head_id = p_auth_user;
END;
//

DELIMITER ;DELIMITER //

DROP PROCEDURE IF EXISTS topic__get_options;

CREATE PROCEDURE topic__get_options (
 IN p_topic_id INT,
 IN p_lvl INT,
 IN p_show_published_state INT,
 IN p_auth_user INT)
BEGIN
    SELECT 
        id, 
        name, 
        created, 
        created_by 
    FROM 
        sow_topic 
    WHERE 
        lvl = p_lvl and parent_id = p_topic_id
        and (p_show_published_state % published = 0
			or created_by = p_auth_user
        );
END;
//

DELIMITER ;DELIMITER //

DROP PROCEDURE IF EXISTS content__update;

CREATE PROCEDURE content__update (
 IN p_content_id INT,
 IN p_description VARCHAR(500),
 IN p_prefix VARCHAR(30),
 IN p_key_stage_id INT,
 IN p_scheme_of_work_id INT,
 IN p_published INT,
 IN p_auth_user INT)
BEGIN
    UPDATE 
        sow_content 
    SET 
        description = p_description, 
        letter = p_prefix,
        key_stage_id = p_key_stage_id,
        scheme_of_work_id = p_scheme_of_work_id,
        published = p_published,
        modified_by = p_auth_user
    WHERE
        id = p_content_id;
END;
//

DELIMITER ;DELIMITER //

DROP PROCEDURE IF EXISTS lesson_learning_objective__get_linked_pathway_objectives;

CREATE PROCEDURE lesson_learning_objective__get_linked_pathway_objectives (
 IN p_lesson_id INT,
 IN p_auth_user INT)
BEGIN
    SELECT
        lob.id as id, 
        lob.description as description, 
        solo.id as solo_id, 
        solo.name as solo_taxonomy_name, 
        solo.lvl as solo_taxonomy_level, 
        cnt.id as content_id, 
        cnt.description as content_description, 
        ks.id as key_stage_id, 
        ks.name as key_stage_name, 
        lob.key_words as key_words, 
        lob.group_name as group_name, 
        lob.created as created, 
        lob.created_by as created_by_id, 
        user.first_name as created_by_name 
    FROM sow_learning_objective as lob 
        INNER JOIN sow_lesson__has__pathway as pw ON pw.learning_objective_id = lob.id 
        LEFT JOIN sow_solo_taxonomy as solo ON solo.id = lob.solo_taxonomy_id 
        LEFT JOIN sow_content as cnt ON cnt.id = lob.content_id 
        LEFT JOIN sow_key_stage as ks ON ks.id = cnt.key_stage_id 
        LEFT JOIN auth_user as user ON user.id = lob.created_by 
   WHERE 
        pw.lesson_id = p_lesson_id 
        ORDER BY ks.name DESC, solo.lvl;
END;
//

DELIMITER ;DELIMITER //

DROP PROCEDURE IF EXISTS lesson__get_options;

CREATE PROCEDURE lesson__get_options (
 IN p_scheme_of_work_id INT,
 IN p_show_published_state INT,
 IN p_auth_user INT)
BEGIN
    SELECT 
        le.id as id, 
        le.title as title, 
        le.order_of_delivery_id as order_of_delivery_id, 
        top.id as topic_id, 
        top.name as name, 
        yr.id as year_id, 
        yr.name as year_name 
    FROM sow_lesson as le 
        INNER JOIN sow_topic as top ON top.id = le.topic_id 
        INNER JOIN sow_year as yr ON yr.id = le.year_id  
    WHERE 
        le.scheme_of_work_id = p_scheme_of_work_id
        AND (p_show_published_state % le.published = 0 
                or le.created_by = p_auth_user)
    ORDER BY le.year_id, le.order_of_delivery_id;
END;
//

DELIMITER ;

CALL lesson__get_options(11,1, 2);DELIMITER //

DROP PROCEDURE IF EXISTS department__get_number_of_schemes_of_work;

CREATE PROCEDURE department__get_number_of_schemes_of_work (
 IN p_department_id INT,
 IN p_auth_user INT)
BEGIN
    SELECT 
        count(sow.id)
    FROM 
        sow_scheme_of_work as sow
    INNER JOIN
		sow_department as dep ON dep.id = sow.department_id
    WHERE
		sow.department_id = p_department_id
        and (sow.published = 1); -- or p_auth_user IN (SELECT auth_user_id 
													-- FROM sow_teacher 
													-- WHERE auth_user_id = p_auth_user));
END;
//

DELIMITER ;

CALL department__get_number_of_schemes_of_work(5,2);DELIMITER $$
DROP PROCEDURE IF EXISTS lesson__get_all_keywords;

CREATE PROCEDURE `lesson__get_all_keywords`(
 IN p_lesson_id INT,
 IN p_show_published_state INT,
 IN p_auth_user INT)
BEGIN
      SELECT 
            kw.id as id, 
            kw.name as term, 
            kw.definition as definition,
            kw.scheme_of_work_id as scheme_of_work_id,
            kw.published as published,
            kw.created as created
      FROM sow_lesson__has__key_words as lkw 
            INNER JOIN sow_key_word kw ON kw.id = lkw.key_word_id 
      WHERE 
            lkw.lesson_id = p_lesson_id
            AND (p_show_published_state % published = 0 
                   or kw.created_by = p_auth_user)
      ORDER BY kw.name;
END$$
DELIMITER ;
DELIMITER //

DROP PROCEDURE IF EXISTS scheme_of_work__get_team_permissions;

CREATE PROCEDURE scheme_of_work__get_team_permissions (
 IN p_head_id INT,
 IN p_department_id INT,
 IN p_institute_id INT,
 IN p_is_authorised BOOLEAN,
 IN p_auth_user INT)
BEGIN
    SELECT 
        teacher_id as teacher_id,
        teacher_name as teacher_name,
		scheme_of_work_id as scheme_of_work_id,
        scheme_of_work_name as scheme_of_work_name,
        department_id as department_id,
        department_name as department_name,
        department_permission as department_permission,
		scheme_of_work_permission as scheme_of_work_permission,
        lesson_permission as lesson_permission,
		is_authorised as is_authorised -- the head of department is authorised
        , hod_id
    FROM sow_permission
	WHERE 
		hod_id = p_head_id -- get head for department
        and is_authorised = p_is_authorised -- authorised or pending
        and department_id = p_department_id
        and institute_id = p_institute_id	
    ORDER BY scheme_of_work_id, teacher_name;
END;
//

DELIMITER ;

CALL scheme_of_work__get_team_permissions(2,5,2,True,2);
CALL scheme_of_work__get_team_permissions(2,5,2,False,2);DELIMITER //

DROP PROCEDURE IF EXISTS lesson_resource__get_all;

CREATE PROCEDURE lesson_resource__get_all (
 IN p_lesson_id INT,
 IN p_resource_type_id INT,
 IN p_show_published_state INT,
 IN p_auth_user INT)
BEGIN
    SELECT 
      res.id as id, 
      res.title as title, 
      res.publisher as publisher, 
      res.type_id as type_id, 
      res_typ.name as resource_type_name, 
      res_typ.task_icon as task_icon, 
      res.md_document_name as md_document_name, 
      res.page_notes as page_notes,  
      res.url as page_uri,  
      res.lesson_id as lesson_id,  
      res.created as created,  
      res.created_by as created_by_id,  
      user.first_name as created_by_name, 
      res.published as published
    FROM sow_resource AS res
    LEFT JOIN sow_lesson AS les ON les.id = res.lesson_id
    LEFT JOIN sow_resource_type as res_typ ON res.type_id = res_typ.id  
    LEFT JOIN auth_user AS user ON user.id = res.created_by 
    WHERE res.lesson_id = p_lesson_id 
      AND (res.type_id = p_resource_type_id or p_resource_type_id = p_resource_type_id) 
      AND (p_show_published_state % res.published = 0
			or les.created_by = p_auth_user 
        );
END;
//

DELIMITER ;DELIMITER //

DROP PROCEDURE IF EXISTS lesson__get_number_of_learning_objectives;

CREATE PROCEDURE lesson__get_number_of_learning_objectives (
 IN p_lesson_id INT,
 IN p_show_published_state INT,
 IN p_auth_user INT)
BEGIN
    SELECT count(lo.id)
    FROM sow_lesson as les 
    INNER JOIN sow_learning_objective__has__lesson as lo ON lo.lesson_id = les.id 
    WHERE les.id = p_lesson_id
      AND (p_show_published_state % les.published = 0 
            or les.created_by = p_auth_user
		);
END;

//

DELIMITER ;DELIMITER //

DROP PROCEDURE IF EXISTS lesson__update;

CREATE PROCEDURE lesson__update (
 IN p_lesson_id INT,
 IN p_title VARCHAR(45),
 IN p_summary VARCHAR(100),
 IN p_order_of_delivery_id INT,
 IN p_scheme_of_work_id INT,
 IN p_content_id INT,
 IN p_topic_id INT,
 IN p_year_id INT,
 IN p_published INT,
 IN p_auth_user INT)
BEGIN
    UPDATE sow_lesson 
    SET title = p_title, 
        summary = p_summary, 
        order_of_delivery_id = p_order_of_delivery_id, 
        scheme_of_work_id = p_scheme_of_work_id, 
        content_id = p_content_id,
        topic_id = p_topic_id, 
        year_id = p_year_id, 
        published = p_published,
        modified_by = p_auth_user
    WHERE 
        id =  p_lesson_id;
END;
//

DELIMITER ;DELIMITER //

DROP PROCEDURE IF EXISTS institute__get_all;

CREATE PROCEDURE institute__get_all (
 IN p_show_published_state INT,
 IN p_auth_user INT)
BEGIN
    SELECT 
        ins.id as id,
        ins.name as name,
        ins.created as created,
        ins.created_by as created_by,
        usr.first_name as created_by_name,
        ins.published as published
    FROM 
        sow_institute as ins
        INNER JOIN auth_user as usr ON usr.id = ins.created_by
    WHERE 
	    p_show_published_state % published = 0 
        or ins.created_by = p_auth_user
    ORDER BY ins.name;
END;
//

DELIMITER ;

CALL institute__get_all(2, 1);DELIMITER //

DROP PROCEDURE IF EXISTS lesson__get_options;

CREATE PROCEDURE lesson__get_options (
 IN p_scheme_of_work_id INT,
 IN p_show_published_state INT,
 IN p_auth_user INT)
BEGIN
    SELECT 
        le.id as id, 
        le.title as title, 
        le.order_of_delivery_id as order_of_delivery_id, 
        top.id as topic_id, 
        top.name as name, 
        yr.id as year_id, 
        yr.name as year_name 
    FROM sow_lesson as le 
        INNER JOIN sow_topic as top ON top.id = le.topic_id 
        INNER JOIN sow_year as yr ON yr.id = le.year_id  
    WHERE 
        le.scheme_of_work_id = p_scheme_of_work_id
        AND (p_show_published_state % le.published = 0 
                or le.created_by = p_auth_user)
    ORDER BY le.year_id, le.order_of_delivery_id;
END;
//

DELIMITER ;

CALL lesson__get_options(11,1, 2);DELIMITER //

DROP PROCEDURE IF EXISTS institute__insert;

CREATE PROCEDURE institute__insert (
 OUT p_institute_id INT,
 IN p_name VARCHAR(100),
 IN p_teacher_id INT,
 IN p_auth_user INT,
 IN p_published INT)	
BEGIN
    INSERT INTO sow_institute
    (
        name, 
        head_id,
        created,
        created_by,
        published
    ) 
    VALUES
    (
        p_name, 
        p_teacher_id,
        NOW(),
        p_auth_user,
        p_published
    );

    SELECT LAST_INSERT_ID();
END;
//

DELIMITER ;DELIMITER //

DROP PROCEDURE IF EXISTS department__get;

CREATE PROCEDURE department__get (
 IN p_department_id INT,
 IN p_show_published_state INT,
 IN p_auth_user INT)
BEGIN
    SELECT 
        dep.id as id,
        dep.name as term,
		dep.institute_id as institute_id,
        dep.created as created,
        dep.created_by as created_by,
        usr.first_name as created_by_name,
        dep.published as published
    FROM 
        sow_department as dep
        INNER JOIN auth_user as usr ON usr.id = dep.created_by
    WHERE
        dep.id = p_department_id 
        AND (p_show_published_state % published = 0 
			 or dep.created_by = p_auth_user);
END;
//

DELIMITER ;

CALL department__get(2,1,2);DELIMITER //

DROP PROCEDURE IF EXISTS department__has__teacher__insert;

CREATE PROCEDURE department__has__teacher__insert (
 IN p_teacher_id INT,
 IN p_department_id INT,
 IN p_department_permission INT,
 IN p_scheme_of_work_permission INT,
 IN p_lesson_permission INT,
 IN p_created_by INT
)
BEGIN
  INSERT IGNORE INTO sow_department__has__teacher
    (	
		auth_user_id, 
		department_id, 
		department_permission, 
		scheme_of_work_permission, 
		lesson_permission, 
		created_by
	)
  VALUES
	(
		p_teacher_id, 
		p_department_id, 
        p_department_permission, -- IF (p_department_permission > 1, p_department_permission, department_permission), 
        p_scheme_of_work_permission, -- IF (p_scheme_of_work_permission > 1, p_scheme_of_work_permission, scheme_of_work_permission), 
        p_lesson_permission, -- IF (p_lesson_permission > 1, p_lesson_permission, lesson_permission), 
        p_created_by
	);
END;
//

DELIMITER ;DELIMITER //

DROP PROCEDURE IF EXISTS scheme_of_work__get_teacher_permissions;

CREATE PROCEDURE scheme_of_work__get_teacher_permissions (
 IN p_teacher_id INT,
 IN p_department_id INT,
 IN p_institute_id INT,
 IN p_is_authorised BIT,
 IN p_auth_user INT)
BEGIN
    SELECT 
		teacher_id as teacher_id,
		teacher_name as teacher_name,
		scheme_of_work_id as scheme_of_work_id,
        scheme_of_work_name as scheme_of_work_name,
        department_id as department_id,
        department_name as department_name,
		institute_id as institute_id,	
        institute_name as institute_name,
		scheme_of_work_permission as scheme_of_work_permission, 
        lesson_permission as lesson_permission,
        department_permission as department_permission,
		is_authorised as is_authorised
    FROM sow_permission
    WHERE department_id = p_department_id
		and institute_id = p_institute_id
        and teacher_id = p_teacher_id
        and is_authorised = p_is_authorised;
END;
//

DELIMITER ;

-- CALL scheme_of_work__get_team_permissions(2, 5, 2, True, 2);
-- CALL scheme_of_work__get_teacher_permissions(2, 5, 2, True, 2);
DELIMITER //

DROP PROCEDURE IF EXISTS scheme_of_work__get_number_of_lessons;

CREATE PROCEDURE scheme_of_work__get_number_of_lessons (
 IN p_scheme_of_work_id INT,
 IN p_show_published_state INT,
 IN p_auth_user INT)
BEGIN
    SELECT count(les.id)
    FROM sow_lesson as les 
    WHERE les.scheme_of_work_id = p_scheme_of_work_id 
      AND (p_show_published_state % les.published = 0 
            or les.created_by = p_auth_user 
	);
END;

//

DELIMITER ;DELIMITER //

DROP PROCEDURE IF EXISTS scheme_of_work__update;

CREATE PROCEDURE scheme_of_work__update (
 IN p_scheme_of_work_id INT,
 IN p_name VARCHAR(40),
 IN p_description TEXT,
 IN p_exam_board_id INT,
 IN p_key_stage_id INT,
 IN p_department_id INT,
 IN p_published INT,
 IN p_auth_user INT)
BEGIN
    UPDATE sow_scheme_of_work 
    SET 
        name = p_name,
        description = p_description, 
        exam_board_id = p_exam_board_id,
        key_stage_id = p_key_stage_id, 
        department_id = p_department_id,
        published = p_published,
        modified_by = p_auth_user
    WHERE id =  p_scheme_of_work_id 
        AND p_auth_user IN (SELECT auth_user_id 
                            FROM sow_teacher 
                            WHERE auth_user_id = p_auth_user AND scheme_of_work_id = p_scheme_of_work_id);
END;
//

DELIMITER ;

DELIMITER //

DROP PROCEDURE IF EXISTS lesson_learning_objective__update;

CREATE PROCEDURE lesson_learning_objective__update (
 IN p_learning_objective_id INT,
 IN p_lesson_id INT,
 IN p_description VARCHAR(1000),
 IN p_group_name VARCHAR(15),
 IN p_notes VARCHAR(4000),
 IN p_key_words VARCHAR(1000),
 IN p_solo_taxonomy_id INT,
 IN p_content_id INT,
 IN p_parent_id INT,
 IN p_published INT,
 IN p_auth_user INT)
BEGIN
  -- CHECK sow_teacher
    UPDATE sow_learning_objective
    SET 
        description = p_description, 
        group_name = p_group_name, 
        notes = p_notes, 
        key_words = p_key_words,
        solo_taxonomy_id = p_solo_taxonomy_id, 
        content_id = p_content_id, 
        parent_id = p_parent_id,
        modified_by = p_auth_user
    WHERE id = p_learning_objective_id;

    UPDATE sow_learning_objective__has__lesson
    SET 
        published = p_published
    WHERE learning_objective_id = p_learning_objective_id and lesson_id = p_lesson_id;
END;
//

DELIMITER ;

DELIMITER //

DROP PROCEDURE IF EXISTS lesson__delete;

CREATE PROCEDURE lesson__delete (
 IN p_lesson_id INT,
 IN p_auth_user INT)
BEGIN
    DELETE sow_lesson 
    FROM sow_lesson
    INNER JOIN sow_scheme_of_work AS sow ON sow.id = sow_lesson.scheme_of_work_id
    WHERE 
        sow_lesson.id = p_lesson_id AND sow_lesson.published IN (32,64) 
                AND p_auth_user IN 
                        (SELECT auth_user_id 
                        FROM sow_teacher 
                        WHERE scheme_of_work_id = sow_lesson.scheme_of_work_id);
END;
//

DELIMITER ;DELIMITER //

DROP PROCEDURE IF EXISTS scheme_of_work__get_latest;

CREATE PROCEDURE scheme_of_work__get_latest (
 IN p_top_n INT,
 IN p_department_id INT,
 IN p_institute_id INT,
 IN p_show_published_state INT,
 IN p_auth_user INT)
BEGIN
    SELECT DISTINCT
      sow.id as id, 
      sow.name as name, 
      sow.description as description, 
      sow.exam_board_id as 
      exam_board_id, 
      exam.name as exam_board_name, 
      sow.key_stage_id as key_stage_id, 
      kys.name as key_stage_name, 
      sow.created as created, 
      sow.created_by as created_by_id, 
      CONCAT_WS(' ', user.first_name, user.last_name) as created_by_name, 
      sow.published as published, 
      dep.id as department_id,
	  dep.name as department_name,
      ins.id as institute_id,
      ins.name as institute_name
	FROM sow_scheme_of_work as sow 
    INNER JOIN sow_department as dep ON dep.id = sow.department_id
    INNER JOIN sow_institute as ins ON ins.id = dep.institute_id
    LEFT JOIN sow_lesson as le ON le.scheme_of_work_id = sow.id 
    LEFT JOIN sow_learning_objective__has__lesson as lo_le ON lo_le.lesson_id = le.id 
    LEFT JOIN sow_exam_board as exam ON exam.id = sow.exam_board_id 
    LEFT JOIN sow_key_stage as kys ON kys.id = sow.key_stage_id  
    LEFT JOIN auth_user as user ON user.id = sow.created_by 
    WHERE dep.institute_id = p_institute_id or p_institute_id = 0 
		or dep.id = p_department_id or p_department_id = 0 
        AND 
			(p_show_published_state % sow.published = 0 
			or sow.created_by = p_auth_user
		)
    ORDER BY sow.created DESC LIMIT p_top_n;
END;
//

DELIMITER ;

#CALL scheme_of_work__get_latest(5, 2);DELIMITER //

DROP PROCEDURE IF EXISTS lesson_learning_objective__get_all;

CREATE PROCEDURE lesson_learning_objective__get_all (
 IN p_lesson_id INT,
 IN p_scheme_of_work_id INT,
 IN p_show_published_state INT,
 IN p_auth_user INT)
BEGIN
    SELECT
        lob.id as id,
        lob.description as description,
        solo.id as solo_id,
        solo.name as solo_taxonomy_name,
        solo.lvl as solo_taxonomy_level,
        cnt.id as content_id,
        cnt.description as content_description,
        sow.key_stage_id as key_stage_id,
        ks.name as key_stage_name,
        le.id as lesson_id,
        le.order_of_delivery_id as order_of_delivery, -- lesson_name,
        lob.key_words as key_words,
        lob.notes as notes,
        lob.group_name as group_name,
        le_lo.is_key_objective as is_key_objective,
        lob.created as created,
        lob.created_by as created_by_id,
        user.first_name as created_by_name,
        le_lo.published as published
    FROM sow_scheme_of_work as sow  
    INNER JOIN sow_lesson as le ON le.scheme_of_work_id = sow.id
    INNER JOIN sow_learning_objective__has__lesson as le_lo ON le_lo.lesson_id = le.id
    INNER JOIN sow_learning_objective as lob ON lob.id = le_lo.learning_objective_id
    LEFT JOIN sow_key_stage as ks ON ks.id = sow.key_stage_id
    LEFT JOIN sow_solo_taxonomy as solo ON solo.id = lob.solo_taxonomy_id
    LEFT JOIN sow_content as cnt ON cnt.id = lob.content_id
    LEFT JOIN auth_user as user ON user.id = lob.created_by
    WHERE le.id = p_lesson_id AND sow.id = p_scheme_of_work_id 
        AND (
			p_show_published_state % lob.published = 0
			or p_show_published_state % sow.published = 0
			or lob.created_by = p_auth_user or sow.created_by = p_auth_user
		)
	ORDER BY solo_taxonomy_level;
END;
//

DELIMITER ;DELIMITER //

DROP PROCEDURE IF EXISTS institute__get_context_model;

CREATE PROCEDURE institute__get_context_model (
 IN p_institute_id INT)
BEGIN
	/* return data for lightweight Context model (id, name, parent_id, created_by, published) */
    SELECT 
        ins.id as id,
        ins.name as name,
        0 as parent_id,
        ins.created_by as created_by,
        ins.published as published
    FROM 
        sow_institute as ins
    WHERE
        ins.id = p_institute_id;
END;
//

DELIMITER ;

CALL institute__get_context_model(2);DELIMITER //

DROP PROCEDURE IF EXISTS lesson__get_ks123_pathway_objective_ids;

CREATE PROCEDURE lesson__get_ks123_pathway_objective_ids (
 IN p_lesson_id INT,
 IN p_show_published_state INT,
 IN p_auth_user INT)
BEGIN
      SELECT ks123_pathway_id
      FROM sow_lesson__has__ks123_pathway as lp
      INNER JOIN sow_lesson as les on les.id = lp.lesson_id
      WHERE lp.lesson_id = p_lesson_id
      AND (p_show_published_state % les.published = 0 
            or les.created_by = p_auth_user
		);
END;

//

DELIMITER;DELIMITER //

DROP PROCEDURE IF EXISTS keyword__merge_duplicates;

CREATE PROCEDURE keyword__merge_duplicates (
 IN p_key_word_id INT,
 IN p_scheme_of_work_id INT,
 IN p_auth_user INT)
BEGIN
	DECLARE term varchar(100);
        
    SET term = (SELECT name 
				FROM sow_key_word 
				WHERE id = p_key_word_id
					and scheme_of_work_id = p_scheme_of_work_id
				LIMIT 1);                
    
    -- Create new the lesson keyword links from the keywords being deleted
    
	INSERT IGNORE INTO sow_lesson__has__key_words (key_word_id, lesson_id)
	SELECT p_key_word_id as replacement, lkw.lesson_id
    FROM sow_lesson__has__key_words as lkw 
    INNER JOIN sow_key_word as kw ON lkw.key_word_id = kw.id
	WHERE kw.name = term and kw.id != p_key_word_id and kw.scheme_of_work_id = p_scheme_of_work_id;	

	-- Mark other keywords as deleted 
	
    UPDATE sow_key_word 
	SET published = 64 -- marked for deletion
    WHERE name = term and id != p_key_word_id and scheme_of_work_id = p_scheme_of_work_id;
    
END;
//

DELIMITER ;
DELIMITER //

DROP PROCEDURE IF EXISTS lesson__get_all;

CREATE PROCEDURE lesson__get_all (
 IN p_scheme_of_work_id INT,
 IN p_show_published_state INT,
 IN p_auth_user INT)
BEGIN
    SELECT  
        le.id as id, 
        le.title as title, 
        le.order_of_delivery_id as order_of_delivery_id, 
        le.scheme_of_work_id as scheme_of_work_id, 
        sow.name as scheme_of_work_name, 
        le.content_id as content_id,
        cnt.description as content_description,
        top.id as topic_id, 
        top.name as topic_name, 
        pnt_top.id as parent_topic_id, 
        pnt_top.name as parent_topic_name, 
        sow.key_stage_id as key_stage_id, 
        yr.id as year_id, yr.name as year_name, 
        le.summary as summary, 
        le.created as created, 
        le.created_by as created_by_id, 
        user.first_name as created_by_name, 
        le.published as published 
    FROM sow_lesson as le  
    INNER JOIN sow_scheme_of_work as sow ON sow.id = le.scheme_of_work_id 
    INNER JOIN sow_year as yr ON yr.id = le.year_id 
    LEFT JOIN sow_topic as top ON top.id = le.topic_id  
    LEFT JOIN sow_topic as pnt_top ON pnt_top.id = top.parent_id  
    LEFT JOIN sow_content as cnt ON cnt.id = le.content_id
    LEFT JOIN auth_user as user ON user.id = sow.created_by  
    WHERE le.scheme_of_work_id = p_scheme_of_work_id
        AND (p_show_published_state % sow.published = 0  
             or p_show_published_state % le.published = 0
             or le.created_by = p_auth_user
             or sow.created_by = p_auth_user
		)
    ORDER BY le.year_id, le.order_of_delivery_id;
END;
//

DELIMITER ;DELIMITER //

DROP PROCEDURE IF EXISTS lesson__get;

CREATE PROCEDURE lesson__get (
 IN p_lesson_id INT,
 IN p_scheme_of_work_id INT,
 IN p_show_published_state INT,
 IN p_auth_user INT)
BEGIN
    SELECT 
        le.id as id,
        le.title as title,
        le.order_of_delivery_id as order_of_delivery_id,
        le.scheme_of_work_id as scheme_of_work_id,
        sow.name as scheme_of_work_name,
        le.content_id as content_id,
        cnt.description as content_description,
        top.id as topic_id,
        top.name as topic_name,
        pnt_top.id as parent_topic_id,
        pnt_top.name as parent_topic_name,
        sow.key_stage_id as key_stage_id,
        yr.id as year_id,
        le.summary as summary,
        le.created as created,
        le.created_by as created_by_id,
        user.first_name as created_by_name,
        le.published as published
    FROM sow_lesson as le
        INNER JOIN sow_scheme_of_work as sow ON sow.id = le.scheme_of_work_id
        INNER JOIN sow_year as yr ON yr.id = le.year_id
        INNER JOIN sow_topic as top ON top.id = le.topic_id
        LEFT JOIN sow_topic as pnt_top ON pnt_top.id = top.parent_id
        LEFT JOIN sow_content as cnt ON cnt.id = le.content_id
        LEFT JOIN auth_user as user ON user.id = sow.created_by
    WHERE le.id = p_lesson_id AND le.scheme_of_work_id = p_scheme_of_work_id 
        AND (	
				p_show_published_state % sow.published = 0 
				or p_show_published_state % le.published = 0 
                or sow.created_by = p_auth_user
                or le.created_by = p_auth_user
		);
END;
//

DELIMITER ;DELIMITER //

DROP PROCEDURE IF EXISTS scheme_of_work__has__teacher_permission__update;

CREATE PROCEDURE scheme_of_work__has__teacher_permission__update (
 IN p_scheme_of_work_id INT,
 IN p_teacher_id INT,
 IN p_department_permission INT,
 IN p_scheme_of_work_permission INT,
 IN p_lesson_permission INT, 
 IN p_auth_user INT,
 IN p_is_authorised BOOLEAN
 )
BEGIN
	-- DO NOT UPDATE ESSENTIAL USERS
	UPDATE sow_scheme_of_work__has__teacher 
	SET
		department_permission = p_department_permission,
		scheme_of_work_permission = p_scheme_of_work_permission,
		lesson_permission = p_lesson_permission,
		modified_by = p_auth_user,
        is_authorised = p_is_authorised
	WHERE
		scheme_of_work_id = p_scheme_of_work_id and
		auth_user_id = p_teacher_id;
END;
//

#CALL scheme_of_work__has__teacher_permission__update(11, 113, 1, 1, 1, 2, True);

DELIMITER ;DELIMITER //

DROP PROCEDURE IF EXISTS lesson_resource__update;

CREATE PROCEDURE lesson_resource__update (
 IN p_resource_id INT,
 IN p_title VARCHAR(300),
 IN p_publisher VARCHAR(500),
 IN p_type_id INT,
 IN p_notes text,
 IN p_url VARCHAR(2083),
 IN p_md_document_name VARCHAR(200),
 IN p_is_expired TINYINT,
 IN p_lesson_id INT,
 IN p_published INT,
 IN p_auth_user INT)
BEGIN
    UPDATE 
        sow_resource
    SET 
        title = p_title, 
        publisher = p_publisher, 
        type_id = p_type_id,
        page_notes = p_notes,
        url = p_url,
        md_document_name = p_md_document_name,
        is_expired = p_is_expired,
        lesson_id = p_lesson_id, 
        published = p_published,
        modified_by = p_auth_user
    WHERE 
        id = p_resource_id;
END;
//

DELIMITER ;DELIMITER $$

DROP PROCEDURE IF EXISTS scheme_of_work__get_all_keywords;

CREATE PROCEDURE `scheme_of_work__get_all_keywords`(
 IN p_scheme_of_work_id INT,
 IN p_show_published_state INT,
 IN p_auth_user INT)
BEGIN
      SELECT 
            kw.id as id, 
            kw.name as term, 
            kw.definition as definition, 
            kw.scheme_of_work_id as scheme_of_work_id,
            kw.published as published,
            kw.created as created
      FROM sow_key_word kw
      WHERE 
            kw.scheme_of_work_id = p_scheme_of_work_id
            AND (p_show_published_state % published = 0 
                  or kw.created_by = p_auth_user
			  )
      ORDER BY kw.name;
END$$
DELIMITER ;
DELIMITER //

DROP PROCEDURE IF EXISTS department__insert;

CREATE PROCEDURE department__insert (
    OUT p_department_id INT,
    IN p_name VARCHAR(70),
    IN p_teacher_id INT,
    IN p_institute_id INT,
    IN p_created DATETIME,
    IN p_created_by INT,
	IN p_published INT)
BEGIN
    -- CHECK sow_department
    INSERT INTO sow_department 
    (
        name, 
        head_id, 
        institute_id,
        created, 
        created_by,
        published
    )
    VALUES
    (
        p_name,
        p_teacher_id,
        p_institute_id,
        p_created,
        p_created_by,
        p_published
    );

    SELECT LAST_INSERT_ID();
END;
//

DELIMITER ;

DELIMITER //

DROP PROCEDURE IF EXISTS scheme_of_work__get_number_of_resources;

CREATE PROCEDURE scheme_of_work__get_number_of_resources (
 IN p_scheme_of_work_id INT,
 IN p_show_published_state INT,
 IN p_auth_user INT)
BEGIN
    SELECT count(lo.id)
    FROM sow_lesson as les 
    INNER JOIN sow_resource as lo ON lo.lesson_id = les.id 
    WHERE les.scheme_of_work_id = p_scheme_of_work_id 
      AND (p_show_published_state % les.published = 0
            or les.created_by = p_auth_user);
END;

//

DELIMITER ;DELIMITER //

DROP PROCEDURE IF EXISTS institute__get_context_name;

CREATE PROCEDURE institute__get_context_name (
 IN p_institute_id INT,
 IN p_auth_user_id INT)
BEGIN
    SELECT 
      ins.name as institute_name
	FROM sow_institute as ins
	WHERE ins.id = p_institute_id
    LIMIT 1;
END;
//

DELIMITER ;

CALL institute__get_context_name(2,2);DELIMITER //

DROP PROCEDURE IF EXISTS lesson_learning_objective__delete;

CREATE PROCEDURE lesson_learning_objective__delete (
 IN p_learning_objective_id INT,
 IN p_auth_user INT)
BEGIN
    DECLARE number_of_linked_lessons INT DEFAULT 0;
    
    DELETE sow_learning_objective__has__lesson
    FROM sow_learning_objective__has__lesson 
    INNER JOIN sow_lesson AS l ON l.id = sow_learning_objective__has__lesson.lesson_id
    WHERE learning_objective_id = p_learning_objective_id
        AND sow_learning_objective__has__lesson.published IN (32,64)
        -- delete only learning objectives from lesson owned by auth_user
        AND p_auth_user IN (SELECT auth_user_id 
                          FROM sow_teacher 
                          WHERE auth_user_id = p_auth_user AND scheme_of_work_id = l.scheme_of_work_id);

    SELECT count(*) 
    INTO number_of_linked_lessons
    FROM sow_learning_objective__has__lesson
    WHERE learning_objective_id = p_learning_objective_id;

    -- Delete the learning objective if it's the only one and still unpublished
    IF number_of_linked_lessons = 1 THEN
        DELETE FROM sow_learning_objective 
        WHERE id = p_learning_objective_id 
        AND published IN (32,64)
        -- delete only learning objectives from lesson owned by auth_user
        AND p_auth_user IN (SELECT auth_user_id 
                            FROM sow_teacher 
                            WHERE auth_user_id = p_auth_user AND scheme_of_work_id = l.scheme_of_work_id);
    END IF;
END;
//

DELIMITER ;

DELIMITER //

DROP PROCEDURE IF EXISTS lesson__delete_unpublished;

CREATE PROCEDURE lesson__delete_unpublished (
 IN p_scheme_of_work_id INT,
 IN p_auth_user INT)
BEGIN
    DELETE FROM sow_lesson
    WHERE scheme_of_work_id = p_scheme_of_work_id 
            AND published IN (32,64) 
            AND p_auth_user IN 
                    (SELECT auth_user_id 
                    FROM sow_teacher 
                    WHERE scheme_of_work_id = p_scheme_of_work_id);
END;
//

DELIMITER ;DELIMITER //

DROP PROCEDURE IF EXISTS teacher__get;

CREATE PROCEDURE teacher__get (
 IN p_teacher_id INT,
 IN p_department_id INT,
 IN p_institute_id INT)
BEGIN
    SELECT 
      user.id as teacher_id,
      user.first_name as teacher_name,  
      dep.id as department_id,
      dep.name as department_name,
      ins.id as institute_id,
      ins.name as institute_name,
      -- authorise based on department__has__teacher relationship,
      -- if this does not exist yet, then is_authorised is true, if 
      -- the teacher is the head of the department
      -- IFNULL(teach_dep.is_authorised, dep.head_id = p_teacher_id) as is_authorised
	  dep.head_id = p_teacher_id as is_authorised
    FROM auth_user as user    
    INNER JOIN sow_department as dep
    INNER JOIN sow_institute as ins ON ins.id = dep.institute_id
    LEFT JOIN sow_department__has__teacher as teach_dep 
		ON teach_dep.auth_user_id = user.id and teach_dep.department_id = dep.id
	WHERE user.id = p_teacher_id and dep.institute_id = p_institute_id and (teach_dep.department_id = p_department_id or dep.head_id = p_teacher_id);
    
END;
//

DELIMITER ;

CALL teacher__get(2,5,2);DELIMITER //

DROP PROCEDURE IF EXISTS scheme_of_work__has__teacher_permission__insert;

CREATE PROCEDURE scheme_of_work__has__teacher_permission__insert (
 IN p_scheme_of_work_id INT,
 IN p_teacher_id INT,
 IN p_department_permission INT,
 IN p_scheme_of_work_permission INT,
 IN p_lesson_permission INT, 
 IN p_auth_user INT,
 IN p_is_authorised BOOLEAN
 )
BEGIN
	INSERT IGNORE INTO sow_scheme_of_work__has__teacher 
	(
		scheme_of_work_id,
		auth_user_id, -- assumes the auth_user (TODO: change column name to teacher_id)
		department_permission,
		scheme_of_work_permission,
		lesson_permission,
        is_authorised,
        created_by
	)
	VALUES 
	(
		p_scheme_of_work_id,
		p_teacher_id,
		p_department_permission,
		p_scheme_of_work_permission,
		p_lesson_permission,
        p_is_authorised,
        p_auth_user
	);
END;
//

DELIMITER ;
DELIMITER //

DROP PROCEDURE IF EXISTS lesson__get_filtered;

CREATE PROCEDURE lesson__get_filtered (
 IN p_scheme_of_work_id INT,
 IN p_keyword_search VARCHAR(100),
 IN p_page INT,
 IN p_pagesize INT,
 IN p_show_published_state INT,
 IN p_auth_user INT)
BEGIN
    DECLARE offset_n_records INT DEFAULT p_page * p_pagesize;

    SELECT  
        le.id as id, 
        le.title as title, 
        le.order_of_delivery_id as order_of_delivery_id, 
        le.scheme_of_work_id as scheme_of_work_id, 
        sow.name as scheme_of_work_name, 
        le.content_id as content_id,
        cnt.description as content_description,
        top.id as topic_id, 
        top.name as topic_name, 
        pnt_top.id as parent_topic_id, 
        pnt_top.name as parent_topic_name, 
        sow.key_stage_id as key_stage_id, 
        yr.id as year_id, yr.name as year_name, 
        le.summary as summary, 
        le.created as created, 
        le.created_by as created_by_id, 
        user.first_name as created_by_name, 
        le.published as published 
    FROM sow_lesson as le  
    INNER JOIN sow_scheme_of_work as sow ON sow.id = le.scheme_of_work_id 
    INNER JOIN sow_year as yr ON yr.id = le.year_id 
    LEFT JOIN sow_topic as top ON top.id = le.topic_id  
    LEFT JOIN sow_topic as pnt_top ON pnt_top.id = top.parent_id  
    LEFT JOIN sow_content as cnt ON cnt.id = le.content_id
    LEFT JOIN auth_user as user ON user.id = sow.created_by  
    WHERE le.scheme_of_work_id = p_scheme_of_work_id
        AND (p_keyword_search = "" or le.title LIKE CONCAT('%', p_keyword_search, '%') 
                or 
                le.id IN (
                            SELECT lesson_id 
                            FROM sow_lesson__has__key_words lkw
                            INNER JOIN sow_key_word as kw ON kw.id = lkw.key_word_id
                            WHERE kw.name LIKE CONCAT('%', p_keyword_search, '%')
                        )
            )
        AND (p_show_published_state % sow.published = 0
                or sow.created_by = p_auth_user
		)
    ORDER BY le.year_id, le.order_of_delivery_id
    LIMIT p_pagesize OFFSET offset_n_records;
END;
//

DELIMITER ;DELIMITER //

DROP PROCEDURE IF EXISTS scheme_of_work__get_number_of_learning_objectives;

CREATE PROCEDURE scheme_of_work__get_number_of_learning_objectives (
 IN p_scheme_of_work_id INT,
 IN p_show_published_state INT,
 IN p_auth_user INT)
BEGIN
    SELECT count(lo.id)
    FROM sow_lesson as les 
    INNER JOIN sow_learning_objective__has__lesson as lo ON lo.lesson_id = les.id 
    WHERE les.scheme_of_work_id = p_scheme_of_work_id 
      AND (p_show_published_state % les.published = 0 
            or les.created_by = p_auth_user 
		);
END;

//

DELIMITER ;DELIMITER //

DROP PROCEDURE IF EXISTS keystage__get_options;

CREATE PROCEDURE keystage__get_options (
 IN p_show_published_state INT,
 IN p_auth_user INT)
BEGIN
    SELECT 
        id,
        name 
    FROM 
        sow_key_stage
	WHERE p_show_published_state % published = 0
		or created_by = p_auth_user;
END;
//

DELIMITER ;DELIMITER //

DROP PROCEDURE IF EXISTS lesson__get_related_topic_ids;

CREATE PROCEDURE lesson__get_related_topic_ids (
 IN p_lesson_id INT,
 IN p_parent_topic_id INT,
 IN p_show_published_state INT,
 IN p_auth_user INT)
BEGIN
      SELECT 
            top.id as id, 
            top.name as name, 
            letop.topic_id as checked, 
            (SELECT count(topic_id) 
                  FROM sow_learning_objective AS lob 
                  LEFT JOIN sow_learning_objective__has__lesson AS lole ON lole.learning_objective_id = lob.id 
                  WHERE lole.lesson_id = letop.lesson_id and lob.topic_id = top.id) as disabled 
      FROM sow_topic AS top 
            LEFT JOIN sow_lesson__has__topics AS letop 
				ON top.id = letop.topic_id and letop.lesson_id = p_lesson_id
      WHERE top.parent_id = p_parent_topic_id 
		and (p_show_published_state % top.published = 0
			or top.created_by = p_auth_user);
END;


//

DELIMITER ;DELIMITER //

DROP PROCEDURE IF EXISTS content__get_options;

CREATE PROCEDURE content__get_options (
 IN p_scheme_of_work_id INT,
 IN p_key_stage_id INT,
 IN p_show_published_state INT,
 IN p_auth_user INT)
BEGIN
    SELECT 
        cnt.id as id, 
        cnt.description as description, 
        cnt.letter as letter_prefix
    FROM sow_content as cnt 
        WHERE key_stage_id = p_key_stage_id
			AND (p_show_published_state % cnt.published = 0
				or cnt.created_by = p_auth_user
            );
END;
//

DELIMITER ;