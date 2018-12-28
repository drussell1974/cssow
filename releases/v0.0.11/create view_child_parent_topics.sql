ALTER 
    ALGORITHM = UNDEFINED 
    DEFINER = `root`@`localhost` 
    SQL SECURITY DEFINER
VIEW `view_child_parent_topics` AS
    SELECT 
        t.id   			AS id,
        t.name			AS name,
        p.id 			AS parent_id,
        p.name 			AS parent_name,
        r.id 			AS related_topic_id,
        r.name 			AS related_topic_name,
        t.created   	AS created,
        t.created_by   	AS created_by  
    FROM
		sow_topic   as  t 
        LEFT JOIN sow_topic as p ON p.id = t.parent_id
        LEFT JOIN sow_topic as r ON p.id = r.parent_id #or t.parent_id = r.parent_id
	