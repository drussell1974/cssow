ALTER PROCEDURE `generate_learning_episodes`(IN sow_id INT)
BEGIN
	DECLARE delivery INT;
	DECLARE topic_id INT;

	SET sow_id := 12;
	SET delivery := 1;
	SET topic_id := 7;

	WHILE topic_id < 74 DO

		INSERT INTO sow_learning_episode (order_of_delivery_id, scheme_of_work_id, topic_id, created, created_by) VALUES (delivery, sow_id, topic_id, '2019-01-05 15:08', 1);
		
		SET delivery = delivery + 1;
		SET topic_id = topic_id + 1;
		
	END WHILE;
        
    # TODO: create sow_learning_objective__has__learning_episode
    
	# ensure learning episode is parent
    
	UPDATE sow_learning_episode 
	INNER JOIN sow_topic ON sow_topic.id = sow_learning_episode.topic_id
	SET sow_learning_episode.topic_id = sow_topic.parent_id 
	WHERE sow_learning_episode.scheme_of_work_id = sow_id AND sow_learning_episode.topic_id >= 7;
END