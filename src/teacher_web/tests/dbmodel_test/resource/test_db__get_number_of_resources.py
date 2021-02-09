from unittest import TestCase, skip
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper

# create test context

from shared.models.cls_resource import ResourceModel, handle_log_info

# TODO: #329 remove global refernence
get_number_of_resources = ResourceModel.get_number_of_resources

from shared.models.cls_department import DepartmentModel
from shared.models.cls_teacher import TeacherModel

@patch("shared.models.cls_teacher.TeacherModel", return_value=TeacherModel(6079, "Dave Russell", department=DepartmentModel(67, "Computer Science")))
class test_db__get_resource_type_options(TestCase):
    
    def setUp(self):
        ' fake database context '
        self.fake_db = Mock()
        self.fake_db.cursor = MagicMock()


    def tearDown(self):
        self.fake_db.close()


    def test__should_call_scalar__with_exception(self, mock_auth_user):
        # arrange
        expected_exception = KeyError("Bang!")

        with patch.object(ExecHelper, 'scalar', side_effect=expected_exception):
            # act and assert

            with self.assertRaises(Exception):
                get_number_of_resources(self.fake_db, 99, auth_user=99)


    def test__should_call_scalar__return_no_items(self, mock_auth_user):
        # arrange
        expected_result = [0]

        with patch.object(ExecHelper, 'scalar', return_value=expected_result):
            # act
            
            actual_results = get_number_of_resources(self.fake_db, 677, auth_user=mock_auth_user)
            
            # assert

            ExecHelper.scalar.assert_called_with(self.fake_db,
                'lesson__get_number_of_resources'
                , (677,1,mock_auth_user.id)
                , []
                , handle_log_info)

            self.assertEqual(0, actual_results)


    def test__should_call_scalar__return_single_item(self, mock_auth_user):
        # arrange
        expected_result = [1]

        with patch.object(ExecHelper, 'scalar', return_value=expected_result):
            # act

            actual_results = get_number_of_resources(self.fake_db, 12, auth_user=mock_auth_user)
            
            # assert

            ExecHelper.scalar.assert_called_with(self.fake_db,
                "lesson__get_number_of_resources"
                , (12,1,mock_auth_user.id)
                , []
                , handle_log_info)
            
            self.assertEqual(1, actual_results)


    def test__should_call_scalar__return_multiple_item(self, mock_auth_user):
        # arrange
        expected_result = [3]

        with patch.object(ExecHelper, 'scalar', return_value=expected_result):
            # act

            actual_results = get_number_of_resources(self.fake_db, 22, auth_user=mock_auth_user)
            
            # assert

            ExecHelper.scalar.assert_called_with(self.fake_db,
                "lesson__get_number_of_resources"
                , (22, 1, mock_auth_user.id)
                , []
                , handle_log_info)
            
            self.assertEqual(3, actual_results)
