from unittest import TestCase
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.cls_schemeofwork import SchemeOfWorkModel as Model, handle_log_info
from shared.models.cls_department import DepartmentModel
from shared.models.cls_teacher import TeacherModel

@patch("shared.models.cls_teacher.TeacherModel", return_value=TeacherModel(6079, "Dave Russell", department=DepartmentModel(67, "Computer Science")))
class test_db__get_options(TestCase):
    
    def setUp(self):
        ' fake database context '
        self.fake_db = Mock()
        self.fake_db.cursor = MagicMock()
        handle_log_info = MagicMock()

    def tearDown(self):
        self.fake_db.close()


    def test__should_call__select__with_exception(self, mock_auth_user):
        # arrange
        expected_exception = KeyError("Bang!")

        with patch.object(ExecHelper, 'select', side_effect=expected_exception):
            # act and assert

            with self.assertRaises(Exception):
                Model.get_options(self.fake_db)


    def test__should_call__select__return_no_items(self, mock_auth_user):
        # arrange
        expected_result = []

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act
            
            rows = Model.get_options(self.fake_db, mock_auth_user)
            
            # assert

            ExecHelper.select.assert_called_with(
                self.fake_db,
                "scheme_of_work__get_options"
                , (mock_auth_user.id,)
                , []
                , handle_log_info)
            self.assertEqual(0, len(rows))


    def test__should_call__select__return_single_item(self, mock_auth_user):
        # arrange
        expected_result = [(123, "Item 1", "Praesent tempus facilisis pharetra. Pellentesque.", 20)]

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act

            rows = Model.get_options(self.fake_db, mock_auth_user)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                "scheme_of_work__get_options"
                , (mock_auth_user.id,)
                , []
                , handle_log_info)
            
            self.assertEqual(1, len(rows))
            self.assertEqual(123, rows[0].id)
            self.assertEqual("Item 1", rows[0].name)
            self.assertEqual("Praesent tempus facilisis pharetra. Pellentesque.", rows[0].key_stage_name)



    def test__should_call__select__return_multiple_item(self, mock_auth_user):
        # arrange
        expected_result = [
            (1, "Item 1","Lorem ipsum dolor sit amet.",5),
            (2,"Item 2","Nulla porttitor quis tortor ac.",8),
            (3, "Item 3","Sed vehicula, quam nec sodales.",97)]

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act

            rows = Model.get_options(self.fake_db, mock_auth_user)
            
            # assert

            ExecHelper.select.assert_called_with(
                self.fake_db,
                "scheme_of_work__get_options"
                , (mock_auth_user.id,)
                , []
                , handle_log_info)

            self.assertEqual(3, len(rows))

            self.assertEqual(1, rows[0].id)
            self.assertEqual("Item 1", rows[0].name)
            self.assertEqual("Lorem ipsum dolor sit amet.", rows[0].key_stage_name)

            self.assertEqual(3, rows[2].id)
            self.assertEqual("Item 3", rows[2].name)
            self.assertEqual("Sed vehicula, quam nec sodales.", rows[2].key_stage_name)
