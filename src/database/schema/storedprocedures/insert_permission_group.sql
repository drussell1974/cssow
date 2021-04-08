INSERT INTO `django_content_type` (app_label, model) VALUES ('cssow', 'institute');
INSERT INTO `auth_permission` (`name`, `content_type_id`, `codename`) VALUES ('Can View Schedule', LAST_INSERT_ID(), 'view_schedule');
INSERT INTO `auth_group_permissions` (group_id, permission_id) VALUES (1,LAST_INSERT_ID());