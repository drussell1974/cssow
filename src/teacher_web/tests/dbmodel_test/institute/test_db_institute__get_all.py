from unittest import TestCase, skip
from shared.models.cls_institute import InstituteModel as Model, handle_log_info
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.cls_department import DepartmentModel
from shared.models.cls_teacher import TeacherModel

@patch("shared.models.cls_teacher.TeacherModel", return_value=TeacherModel(6079, "Dave Russell", department=DepartmentModel(67, "Computer Science")))
class test_db_institute__get_all(TestCase):

    def setUp(self):
        ' fake database context '
        self.fake_db = Mock()
        self.fake_db.cursor = MagicMock()


    def tearDown(self):
        self.fake_db.close()


    def test__should_call__select__with_exception(self, mock_auth_user):

        # arrange
        expected_result = Exception('Bang')
        
        with patch.object(ExecHelper, "select", side_effect=expected_result):
            # act and assert
            with self.assertRaises(Exception):
                Model.get_all(self.fake_db, key_stage_id = 4)
            

    def test__should_call__select__no_items(self, mock_auth_user):
        # arrange
        expected_result = []

        with patch.object(ExecHelper, "select", return_value=expected_result):
                
            # act
            
            rows = Model.get_all(self.fake_db, auth_user = mock_auth_user)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                'institute__get_all'
                , (mock_auth_user.id,)
                , []
                , handle_log_info)

            self.assertEqual(0, len(rows))


    def test__should_call__select__single_items(self, mock_auth_user):
        # arrange
        expected_result = [(1,"Computer Science", "2020-07-21 17:09:34", 1, "test_user", 0)]
        
        with patch.object(ExecHelper, "select", return_value=expected_result):
            
            # act

            rows = Model.get_all(self.fake_db, auth_user = mock_auth_user)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db, 
                'institute__get_all'
                , (mock_auth_user.id,)
                , []
                , handle_log_info)

            self.assertEqual(1, len(rows))
            self.assertEqual("Computer Science", rows[0].name, "First item not as expected")
            

    def test__should_call__select__multiple_items(self, mock_auth_user):
        # arrange
        expected_result = [
            (1,"Computer Science",  "2020-07-21 17:09:34", 1, "test_user", 0),
            (2, "Business",  "2020-07-21 17:09:34", 1, "test_user", 1), 
            (3, "IT",  "2020-07-21 17:09:34", 1, "test_user", 1)]
        
        with patch.object(ExecHelper, "select", return_value=expected_result):
            # act
            rows = Model.get_all(self.fake_db, auth_user = mock_auth_user)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db, 
                'institute__get_all'
                , (mock_auth_user.id,)
                , []
                , handle_log_info)
            self.assertEqual(3, len(rows))
            self.assertEqual("Computer Science", rows[0].name, "First item not as expected")
            self.assertEqual("IT", rows[len(rows)-1].name, "Last item not as expected")

