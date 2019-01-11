#SELECT * FROM sow_scheme_of_work WHERE name LIKE '%gcse%';
#SELECT * FROM sow_learning_episode WHERE scheme_of_work_id = 12;
#SELECT * FROM sow_topic;


DELETE FROM sow_learning_episode WHERE scheme_of_work_id = 12;

CREATE PROCEDURE create_learning_episodes ()
BEGIN
	
    DECLARE sow_id INT;
	DECLARE delivery INT;
	DECLARE topic_id INT;

	SET sow_id := 12;
	SET delivery := 0;
	SET topic_id := 6;

	WHILE topic_id < 74 DO

		INSERT INTO sow_learning_episode (order_of_delivery_id, scheme_of_work_id, topic_id, created, created_by) VALUES (delivery, sow_id, topic_id, '2019-01-05 15:08', 1);
		
		SET delivery = delivery + 1;
		SET topic_id = topic_id + 1;
		
	END;
END;

CALL create_learning_episodes();

SELECT * FROM sow_learning_episode WHERE scheme_of_work_id = 12;

