SET @sch_name = 'sow_academic_year';
SET @allowed_view_group = 'head of department'; -- 'head of department' or 'teacher' or 'student'
SET @allowed_edit_group = 'head of department'; -- 'head of department' or 'teacher' or 'student'

SELECT @allowed_view_group_id = id FROM auth_group WHERE name = @allowed_view_group;
SELECT @allowed_edit_group_id = id FROM auth_group WHERE name = @allowed_edit_group;

-- 1. create content
INSERT INTO `django_content_type` (app_label, model) VALUES ('cssow', @sch_name);
SET @cnt_id = LAST_INSERT_ID();
SET @sch_name = 'sow_academic_year';

-- 2. index0
-- INSERT INTO `auth_permission` (`name`, `content_type_id`, `codename`) VALUES (CONCAT('Can View ', @sch_name), 16, CONCAT('cssow.view_', @sch_name));
INSERT INTO `auth_group_permissions` (group_id, permission_id) VALUES (1, 56);

-- 3. new edit delete
INSERT INTO `auth_permission` (`name`, `content_type_id`, `codename`) VALUES (CONCAT('Can Edit ', @sch_name), 16, CONCAT('cssow.change_', @sch_name));
INSERT INTO `auth_group_permissions` (group_id, permission_id) VALUES (5, LAST_INSERT_ID());
