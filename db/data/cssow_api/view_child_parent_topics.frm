TYPE=VIEW
query=select `t`.`id` AS `id`,`t`.`name` AS `name`,`p`.`id` AS `parent_id`,`p`.`name` AS `parent_name`,`r`.`id` AS `related_topic_id`,`r`.`name` AS `related_topic_name`,`t`.`lvl` AS `lvl`,`t`.`created` AS `created`,`t`.`created_by` AS `created_by` from ((`cssow_api`.`sow_topic` `t` left join `cssow_api`.`sow_topic` `p` on(`p`.`id` = `t`.`parent_id`)) left join `cssow_api`.`sow_topic` `r` on(`p`.`id` = `r`.`parent_id`))
md5=ff4c0d0215eafdb214c20323c7f9c0ad
updatable=0
algorithm=0
definer_user=drussell1974
definer_host=%
suid=1
with_check_option=0
timestamp=2019-12-20 05:42:06
create-version=2
source=select `t`.`id` AS `id`,`t`.`name` AS `name`,`p`.`id` AS `parent_id`,`p`.`name` AS `parent_name`,`r`.`id` AS `related_topic_id`,`r`.`name` AS `related_topic_name`,`t`.`lvl` AS `lvl`,`t`.`created` AS `created`,`t`.`created_by` AS `created_by` from ((`sow_topic` `t` left join `sow_topic` `p` on((`p`.`id` = `t`.`parent_id`))) left join `sow_topic` `r` on((`p`.`id` = `r`.`parent_id`)))
client_cs_name=utf8
connection_cl_name=utf8_general_ci
view_body_utf8=select `t`.`id` AS `id`,`t`.`name` AS `name`,`p`.`id` AS `parent_id`,`p`.`name` AS `parent_name`,`r`.`id` AS `related_topic_id`,`r`.`name` AS `related_topic_name`,`t`.`lvl` AS `lvl`,`t`.`created` AS `created`,`t`.`created_by` AS `created_by` from ((`cssow_api`.`sow_topic` `t` left join `cssow_api`.`sow_topic` `p` on(`p`.`id` = `t`.`parent_id`)) left join `cssow_api`.`sow_topic` `r` on(`p`.`id` = `r`.`parent_id`))
mariadb-version=100411
