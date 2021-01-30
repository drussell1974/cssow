from unittest import TestCase, skip
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.cls_teacher_permission import TeacherPermissionModel as Model, handle_log_info
from shared.models.cls_schemeofwork import SchemeOfWorkModel
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

            with self.assertRaises(KeyError):
                Model.get_model(self.fake_db, SchemeOfWorkModel(99, name="Computer Sciemce"), teacher_id=7099, auth_user=99)

    
    def test__should_call__select__return_no_permissions(self):
        # arrange
        expected_result = [(int(SCHEMEOFWORK.NONE), int(LESSON.NONE), int(DEPARTMENT.NONE), "James Joyce")]

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act
            
            model = Model.get_model(self.fake_db, SchemeOfWorkModel(99, name="Ulysses"), teacher_id=6059, auth_user=999)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                "scheme_of_work__get_teacher_permissions"
                , (99, 6059, 999)
                , []
                , handle_log_info)
                
            self.assertEqual("James Joyce", model.teacher_name)
            self.assertEqual(6059, model.teacher_id)
            self.assertEqual(99, model.scheme_of_work.id)
            self.assertEqual("Ulysses", model.scheme_of_work.name)
            self.assertEqual(SCHEMEOFWORK.NONE, int(model.scheme_of_work_permission))
            self.assertEqual(LESSON.NONE, model.lesson_permission)
            self.assertEqual(DEPARTMENT.NONE, model.department_permission)
            

    def test__should_call__select__return_has_permission_to_view(self):
        # arrange
        expected_result = [(int(SCHEMEOFWORK.EDITOR), int(LESSON.VIEWER), int(DEPARTMENT.NONE), "Frank Herbert")]

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            
            # act
            
            model = Model.get_model(self.fake_db, SchemeOfWorkModel(14, name="Dune"), teacher_id=6079, auth_user=99)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                "scheme_of_work__get_teacher_permissions"
                , (14, 6079, 99)
                , []
                , handle_log_info)
            
            self.assertEqual("Frank Herbert", model.teacher_name)
            self.assertEqual(6079, model.teacher_id)
            self.assertEqual(14, model.scheme_of_work.id)
            self.assertEqual("Dune", model.scheme_of_work.name)
            self.assertEqual(SCHEMEOFWORK.EDITOR, model.scheme_of_work_permission)
            self.assertEqual(LESSON.VIEWER, model.lesson_permission)
            self.assertEqual(DEPARTMENT.NONE, model.department_permission)
