INSERT INTO `django_content_type` (`app_label`, `model`) VALUES ('cssow', 'teacherpermissionmodel');
SET content_type_id = last_insert_id();
INSERT INTO `auth_permission` (`name`, `content_type_id`, `codename`) VALUES ('Can Manage Team Permissions', content_type_id, 'can_manage_team_permissions');
INSERT INTO `auth_permission` (`name`, `content_type_id`, `codename`) VALUES ('Can Request Team Permissions', content_type_id, 'can_request_team_permissions');

