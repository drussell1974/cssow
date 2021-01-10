from unittest import TestCase, skip
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.cls_teacher_permission import TeacherPermissionModel as Model, handle_log_info
from shared.models.enums.permissions import DEPARTMENT, SCHEMEOFWORK, LESSON

class test_db__get_teacher_permission(TestCase):
    
    def setUp(self):
        ' fake database context '
        self.fake_db = Mock()
        self.fake_db.cursor = MagicMock()

    def tearDown(self):
        self.fake_db.close()


    def test__should_call__select__with_exception(self):
        # arrange
        expected_exception = KeyError("Bang!")

        with patch.object(ExecHelper, 'select', side_effect=expected_exception):
            # act and assert

            with self.assertRaises(Exception):
                SchemeOfWorkModel.has_permission(self.fake_db, 4)

    
    def test__should_call__select__return_no_permissions(self):
        # arrange
        expected_result = [(int(SCHEMEOFWORK.NONE), int(LESSON.NONE), int(DEPARTMENT.NONE))]

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act
            
            model = Model.get_model(self.fake_db, 99, 999)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                "scheme_of_work__get_teacher_permissions"
                , (99, 999)
                , []
                , handle_log_info)
                
            self.assertEqual(999, model.auth_user)
            self.assertEqual(99, model.scheme_of_work_id)
            self.assertEqual(SCHEMEOFWORK.NONE, int(model.scheme_of_work_permission))
            self.assertEqual(LESSON.NONE, model.lesson_permission)
            self.assertEqual(DEPARTMENT.NONE, model.department_permission)
            

    def test__should_call__select__return_has_permission_to_view(self):
        # arrange
        expected_result = [(int(SCHEMEOFWORK.EDIT), int(LESSON.VIEW), int(DEPARTMENT.NONE))]

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            
            # act
            
            model = Model.get_model(self.fake_db, 99, 6)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                "scheme_of_work__get_teacher_permissions"
                , (99, 6)
                , []
                , handle_log_info)
                 
            self.assertEqual(6, model.auth_user)
            self.assertEqual(99, model.scheme_of_work_id)
            self.assertEqual(SCHEMEOFWORK.EDIT, model.scheme_of_work_permission)
            self.assertEqual(LESSON.VIEW, model.lesson_permission)
            self.assertEqual(DEPARTMENT.NONE, model.department_permission)
