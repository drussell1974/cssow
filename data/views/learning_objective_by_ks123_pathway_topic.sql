CREATE 
    ALGORITHM = UNDEFINED 
    DEFINER = `root`@`localhost` 
    SQL SECURITY DEFINER
VIEW `cssow`.`learning_objectives_by_ks123_pathway_topic` AS
    SELECT 
        `lo`.`id` AS `learning_objective_id`,
        `lo`.`description` AS `learning_objective_description`,
        `cssow`.`solo_taxonomy`.`level` AS `solo_level`,
        `lo`.`topic_id` AS `topic_id`,
        `cssow`.`topic`.`name` AS `topic_name`,
        `parent_topic`.`id` AS `parent_topic_id`,
        `parent_topic`.`name` AS `parent_topic_name`,
        `path`.`id` AS `path_objective_id`,
        `path`.`objective` AS `path_objective_description`,
        `cssow`.`year`.`id` AS `year_id`,
        `cssow`.`year`.`name` AS `year_name`
    FROM
        (((((`cssow`.`learning_objective` `lo`
        JOIN `cssow`.`topic` ON ((`lo`.`topic_id` = `cssow`.`topic`.`id`)))
        JOIN `cssow`.`topic` `parent_topic` ON ((`cssow`.`topic`.`parent_id` = `parent_topic`.`id`)))
        JOIN `cssow`.`ks123_pathway` `path` ON ((`parent_topic`.`id` = `path`.`topic_id`)))
        JOIN `cssow`.`year` ON ((`path`.`year_id` = `cssow`.`year`.`id`)))
        JOIN `cssow`.`solo_taxonomy` ON ((`lo`.`solo_taxonomy_id` = `cssow`.`solo_taxonomy`.`id`)))