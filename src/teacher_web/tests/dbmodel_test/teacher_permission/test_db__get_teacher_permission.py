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
        expected_exception = KeyError("Bang!")

        with patch.object(ExecHelper, 'select', side_effect=expected_exception):
            # act and assert

            with self.assertRaises(KeyError):
                Model.get_model(self.fake_db, 101, SchemeOfWorkModel(99, name="Computer Sciemce", auth_user=fake_ctx_model()), auth_user=fake_ctx_model())

    
    def test__should_call__select__return_no_permissions(self):
        # arrange
        
        fake_ctx = fake_ctx_model()

        #expected_result = [(int(SCHEMEOFWORK.NONE), int(LESSON.NONE), int(DEPARTMENT.NONE), "James Joyce", False)]
        expected_result = [(2, "Frank Herbert", 11, "A-Level Computer Science", 5, "Computer Science", 127, "Lorem Ipsum", int(SCHEMEOFWORK.EDITOR), int(LESSON.VIEWER), int(DEPARTMENT.NONE), True)]

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act
            
            model = Model.get_model(self.fake_db, 6079, SchemeOfWorkModel(99, name="Ulysses", study_duration=2, start_study_in_year=10, auth_user=fake_ctx), auth_user=fake_ctx)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                "scheme_of_work__get_teacher_permissions"
                , (6079, 67, 127671276711, True, 6079)
                , []
                , handle_log_info)
            
            #self.assertEqual(99, model.scheme_of_work_id)
            #self.assertEqual("Ulysses", model.scheme_of_work_name)
            self.assertEqual(SCHEMEOFWORK.NONE, int(model.scheme_of_work_permission))
            self.assertEqual(LESSON.NONE, model.lesson_permission)
            self.assertEqual(DEPARTMENT.NONE, model.department_permission)
            self.assertFalse(model.is_authorised)
            

    def test__should_call__select__return_has_permission_to_view(self):
        # arrange

        fake_ctx = fake_ctx_model()
        sow_id_to_get = 12323232
        #expected_result = [(int(SCHEMEOFWORK.EDITOR), int(LESSON.VIEWER), int(DEPARTMENT.NONE), "Frank Herbert", True)]
        expected_result = [(99, "Frank Herbert", sow_id_to_get, "A-Level Computer Science", 67, "Computer Science", 127671276711, "Lorem Ipsum", int(SCHEMEOFWORK.EDITOR), int(LESSON.VIEWER), int(DEPARTMENT.NONE), True)]

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            
            # act
            
            model = Model.get_model(self.fake_db, 99, scheme_of_work=SchemeOfWorkModel(sow_id_to_get, name="Dune", study_duration=2, start_study_in_year=10, auth_user=fake_ctx), auth_user=fake_ctx_model(DEPARTMENT.NONE, SCHEMEOFWORK.EDITOR, LESSON.VIEWER))
            
            # assert
            ExecHelper.select.assert_called_with(self.fake_db,
                "scheme_of_work__get_teacher_permissions"
                , (99, 67, 127671276711, True, 6079)
                , []
                , handle_log_info)
            
            #self.assertEqual(14, model.scheme_of_work_id)
            #self.assertEqual("Dune", model.scheme_of_work.name)
            self.assertEqual(SCHEMEOFWORK.EDITOR, model.scheme_of_work_permission)
            self.assertEqual(LESSON.VIEWER, model.lesson_permission)
            self.assertEqual(DEPARTMENT.NONE, model.department_permission)
            self.assertTrue(model.is_authorised)
