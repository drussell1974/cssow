from unittest import TestCase, skip
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper

# create test context

from shared.models.cls_resource import ResourceModel, handle_log_info

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


    def test__should_call__select__with_exception(self, mock_auth_user):
        # arrange
        expected_exception = KeyError("Bang!")

        with patch.object(ExecHelper, 'select', side_effect=expected_exception):
            # act and assert

            with self.assertRaises(Exception):
                ResourceModel.get_resource_type_options(self.fake_db, auth_user=1)


    def test__should_call__select__return_no_items(self, mock_auth_user):
        # arrange
        expected_result = []

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act
            
            rows = ResourceModel.get_resource_type_options(self.fake_db, auth_user=mock_auth_user)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                'resource_type__get_options', (mock_auth_user.id,)
                , []
                , handle_log_info)

            self.assertEqual(0, len(rows))


    def test__should_call__select__return_single_item(self, mock_auth_user):
        # arrange
        expected_result = [
            (4345, "Markdown")
        ]

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act

            rows = ResourceModel.get_resource_type_options(self.fake_db, auth_user=mock_auth_user)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                'resource_type__get_options'
                , (mock_auth_user.id,)
                , []
                , handle_log_info)
            
            self.assertEqual(1, len(rows))

            self.assertEqual(4345, rows[0].id)
            self.assertEqual("Markdown", rows[0].name)


    def test__should_call__select__return_multiple_item(self, mock_auth_user):
        # arrange
        expected_result = [
            (934, "Book"),
            (666, "Markdown"),
            (37, "Video")
        ]

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act

            rows = ResourceModel.get_resource_type_options(self.fake_db, auth_user=mock_auth_user)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                'resource_type__get_options' 
                , (mock_auth_user.id,)
                , []
                , handle_log_info)
            
            self.assertEqual(3, len(rows))

            self.assertEqual("Book", rows[0].name)
            self.assertEqual("Video", rows[2].name)