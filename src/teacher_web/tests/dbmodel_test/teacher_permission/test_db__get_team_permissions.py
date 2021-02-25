from unittest import TestCase
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.cls_department import DepartmentModel
from shared.models.cls_teacher_permission import TeacherPermissionModel as Model, handle_log_info
from shared.models.enums.permissions import DEPARTMENT, SCHEMEOFWORK, LESSON
from tests.test_helpers.mocks import fake_teacher_permission_model, fake_ctx_model

@patch.object(Model, "get_model", return_value=fake_teacher_permission_model())
@patch("shared.models.cls_teacher_permission.TeacherPermissionModel", return_value=fake_teacher_permission_model())
class test_db__get_team_permissions(TestCase):

    def setUp(self):
        ' fake database context '
        self.fake_db = Mock()
        self.fake_db.cursor = MagicMock()


    def tearDown(self):
        pass

        
    def test__should_call__select__with_exception(self, TeacherModel_get_model, mock_teacher_permission_model):

        # arrange
        expected_result = Exception('Bang')
        
        with patch.object(ExecHelper, "select", side_effect=expected_result):
            # act and assert
            with self.assertRaises(Exception):
                Model.get_all(self.fake_db, key_stage_id = 4)
            

    def test__should_call__select__no_items(self, TeacherModel_get_model, mock_teacher_permission_model):
        # arrange

        fake_ctx = fake_ctx_model()

        expected_result = []

        with patch.object(ExecHelper, "select", return_value=expected_result):
                
            # act
            
            rows = Model.get_team_permissions(self.fake_db, teacher_id = 6079, auth_user=fake_ctx)
            
            # assert
            TeacherModel_get_model.assert_not_called()

            ExecHelper.select.assert_called_with(self.fake_db,
                'scheme_of_work__get_team_permissions'
                , (6079, 67, 127671276711, True, 6079)
                , []
                , handle_log_info)

            self.assertEqual(0, len(rows))


    def test__should_call__select__single_items(self, TeacherModel_get_model, mock_teacher_permission_model):
        # arrange

        fake_ctx = fake_ctx_model()

        expected_result = [
            (1, "John Doe", 67, "GCSE Computer Science", 5, "Computer Science", int(DEPARTMENT.HEAD), int(SCHEMEOFWORK.OWNER), int(LESSON.OWNER), True),
        ]
        
        with patch.object(ExecHelper, "select", return_value=expected_result):
            
            # act

            rows = Model.get_team_permissions(self.fake_db, teacher_id = 6079, auth_user=fake_ctx)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db, 
                'scheme_of_work__get_team_permissions'
                , (6079, 67, 127671276711, True, 6079)
                , []
                , handle_log_info)

            self.assertEqual(1, len(rows))
            #self.assertEqual("John Doe", rows[0].teacher_permissions[0].teacher.name, "First item not as expected")
            

    def test__should_call__select__multiple_items(self, TeacherModel_get_model, mock_teacher_permission_model):
        # arrange

        fake_ctx = fake_ctx_model()

        expected_result = [
            (1, "John Doe", 67, "GCSE Computer Science", 5, "Computer Science", int(DEPARTMENT.HEAD), int(SCHEMEOFWORK.OWNER), int(LESSON.OWNER), True),
            (2, "Jane Rogers", 68,  "Information Technology", 5, "Computer Science", int(DEPARTMENT.TEACHER), int(SCHEMEOFWORK.EDITOR), int(LESSON.EDITOR), True), 
            (3, "Bill Gates", 68,  "A-Level Computer Science", 5, "Computer Science", int(DEPARTMENT.STUDENT), int(SCHEMEOFWORK.VIEWER), int(LESSON.VIEWER), False)
        ]

        with patch.object(ExecHelper, "select", return_value=expected_result):
            # act
            rows = Model.get_team_permissions(self.fake_db, teacher_id = 6079, auth_user=fake_ctx)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db, 
                'scheme_of_work__get_team_permissions'
                , (6079, 67, 127671276711, True, 6079)
                , []
                , handle_log_info)

            self.assertEqual(2, len(rows)) # NOTE: there are two schemes of work and 3 teachers
            #self.assertEqual("John Doe", rows[0].teacher_permissions[0].teacher_id, "First item not as expected")
            #self.assertEqual("Jane Rogers", rows[len(rows)-1].teacher_permissions[0].teacher_id, "Last item not as expected")
            #self.assertEqual("Bill Gates", rows[len(rows)-1].teacher_permissions[1].teacher_id, "Last item not as expected")


    def test__should_call__select__multiple_items___show_unauthorised(self, TeacherModel_get_model, mock_teacher_permission_model):
        # arrange

        fake_ctx = fake_ctx_model()

        expected_result = [
            (1, "John Doe", 67, "GCSE Computer Science", 5, "Computer Science", int(DEPARTMENT.HEAD), int(SCHEMEOFWORK.OWNER), int(LESSON.OWNER), True),
            (2, "Jane Rogers", 68,  "Information Technology", 5, "Computer Science", int(DEPARTMENT.TEACHER), int(SCHEMEOFWORK.EDITOR), int(LESSON.EDITOR), True), 
            (3, "Bill Gates", 68,  "A-Level Computer Science", 5, "Computer Science", int(DEPARTMENT.STUDENT), int(SCHEMEOFWORK.VIEWER), int(LESSON.VIEWER), False)
        ]

        with patch.object(ExecHelper, "select", return_value=expected_result):
            # act
            rows = Model.get_team_permissions(self.fake_db, teacher_id = 6079, show_authorised=False, auth_user=fake_ctx)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db, 
                'scheme_of_work__get_team_permissions'
                , (6079, 67, 127671276711, False, 6079)
                , []
                , handle_log_info)

            self.assertEqual(2, len(rows)) # NOTE: there are two schemes of work and 3 teachers
            #self.assertEqual("John Doe", rows[0].teacher_permissions[0].teacher_id, "First item not as expected")
            #self.assertEqual("Jane Rogers", rows[len(rows)-1].teacher_permissions[0].teacher_id, "Last item not as expected")
            #self.assertEqual("Bill Gates", rows[len(rows)-1].teacher_permissions[1].teacher_id, "Last item not as expected")
