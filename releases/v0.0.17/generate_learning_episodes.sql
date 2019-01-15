DELIMITER $$
CREATE PROCEDURE `generate_learning_episodes`(IN sow_id INT)
BEGIN
	DECLARE delivery INT;
	DECLARE topic INT;
	DECLARE episode_id INT;
	SET delivery := 1;
	SET topic := 7;
	
	WHILE topic < 74 DO
		
		INSERT INTO sow_learning_episode (order_of_delivery_id, scheme_of_work_id, topic_id, created, created_by) VALUES (delivery, sow_id, topic, '2019-01-15 08:32', 1);
		
		SET episode_id := LAST_INSERT_ID();
	
		INSERT INTO sow_learning_objective__has__learning_episode (learning_objective_id, learning_episode_id)
		SELECT  id , episode_id FROM sow_learning_objective WHERE topic_id = topic AND created = '2018-11-02 05:33:00';
        
		SET delivery = delivery + 1;
		SET topic = topic + 1;
		
	END WHILE;
END$$
DELIMITER ;
