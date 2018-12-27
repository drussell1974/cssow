CREATE VIEW view_child_parent_topics AS
	SELECT top.id as id,  top.name as name, pnt_top.id as parent_id, pnt_top.name as parent_name, top.created, top.created_by 
    FROM sow_topic as top
	JOIN sow_topic as pnt_top ON pnt_top.id = top.parent_id;

