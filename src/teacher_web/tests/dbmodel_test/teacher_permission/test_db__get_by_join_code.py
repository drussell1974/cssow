from unittest import TestCase, skip
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.cls_department import DepartmentModel
from shared.models.cls_teacher_permission import TeacherPermissionModel as Model, handle_log_info
from shared.models.cls_schemeofwork import SchemeOfWorkModel
from shared.models.enums.permissions import DEPARTMENT, SCHEMEOFWORK, LESSON
from tests.test_helpers.mocks import fake_teacher_permission_model, fake_ctx_model

class test_db__get_teacher_permission(TestCase):
    
    def setUp(self):
        ' fake database context '
        self.fake_db = Mock()
        self.fake_db.cursor = MagicMock()

    def tearDown(self):
        self.fake_db.close()


    def test__should_call__select__with_exception(self):
        # arrange
        fake_ctx = fake_ctx_model()

        expected_exception = KeyError("Bang!")

        with patch.object(ExecHelper, 'select', side_effect=expected_exception):
            # act and assert

            with self.assertRaises(PermissionError):
                Model.get_by_join_code(self.fake_db, "ABCDEX", ctx=fake_ctx)

    
    def test__should_call__select__return_no_permissions(self):
        # arrange
        fake_ctx = fake_ctx_model()

        expected_result = []

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act
            
            model = Model.get_by_join_code(self.fake_db, "ABCDEF", ctx=fake_ctx)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                "scheme_of_work__get_team_permissions_by_join_code"
                , ("ABCDEF")
                , []
                , handle_log_info)
            
            self.assertIsNone(model)
            

    def test__should_call__select__return_has_permission_to_view(self):
        # arrange
        fake_ctx = fake_ctx_model()

        expected_result = [(99, "Frank Herbert", "ABCDEFGH", 12323232, "A-Level Computer Science", 67, "Computer Science", 127671276711, "Lorem Ipsum", int(DEPARTMENT.NONE), int(SCHEMEOFWORK.EDITOR), int(LESSON.VIEWER), False)]

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            
            # act
            
            model = Model.get_by_join_code(self.fake_db, "ABCDEF", ctx=fake_ctx)
            
            # assert
            ExecHelper.select.assert_called_with(self.fake_db,
                "scheme_of_work__get_team_permissions_by_join_code"
                , ("ABCDEF")
                , []
                , handle_log_info)
            
            self.assertEqual(SCHEMEOFWORK.EDITOR, model.scheme_of_work_permission)
            self.assertEqual(LESSON.VIEWER, model.lesson_permission)
            self.assertEqual(DEPARTMENT.NONE, model.department_permission)
            self.assertFalse(model.is_authorised)
