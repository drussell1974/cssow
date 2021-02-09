from unittest import TestCase
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.cls_department import DepartmentModel
from shared.models.cls_teacher import TeacherModel as Model, handle_log_info
from shared.models.cls_department import DepartmentModel
from shared.models.cls_teacher import TeacherModel

class test_db__get_model(TestCase):
    
    def setUp(self):
        ' fake database context '
        self.fake_db = Mock()
        self.fake_db.cursor = MagicMock()

    def tearDown(self):
        self.fake_db.close()

    @patch("shared.models.cls_teacher.TeacherModel", return_value=TeacherModel(6079, "Dave Russell", is_from_db=True, department=DepartmentModel(67, "Computer Science", is_from_db=True)))
    def test__should_call_select__with_exception(self, mock_auth_user):
        # arrange
        expected_exception = KeyError("Bang!")

        with patch.object(ExecHelper, 'select', side_effect=expected_exception):
            # act and assert

            with self.assertRaises(Exception):
                Model.get_model(self.fake_db, 54, 4)

    #NOTE: Do not use mock_auth_user
    def test__should_call_select__return_no_items(self):
        # arrange
        expected_result = []

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act
            
            actual_result = Model.get_model(self.fake_db, 999, 45)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                'teacher__get'
                , (999, 45)
                , []
                , handle_log_info)

            self.assertEqual(0, actual_result.id)
            self.assertFalse(actual_result.is_authorised)

    @patch("shared.models.cls_teacher.TeacherModel", return_value=TeacherModel(6079, "Dave Russell", is_from_db=True, department=DepartmentModel(67, "Computer Science", is_from_db=True)))
    def test__should_call_select__return_single_item(self, mock_auth_user):
        # arrange
        expected_result = [(6079, "Dave Russell", 67, "Computer Science", True)]

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act

            model = Model.get_model(self.fake_db, 6, 34)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                'teacher__get'
                , (6, 34)
                , []
                , handle_log_info)

            self.assertEqual(6079, model.id)
            self.assertEqual("Dave Russell", model.name)
            self.assertEqual(67, model.department.id)
            self.assertEqual("Computer Science", model.department.name)
            self.assertFalse(model.is_new())
            self.assertTrue(model.is_from_db)



