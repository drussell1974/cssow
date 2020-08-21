from unittest import TestCase, skip
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper

# create test context

from shared.models.cls_resource import ResourceModel, handle_log_info

get_number_of_resources = ResourceModel.get_number_of_resources

class test_db__get_resource_type_options(TestCase):
    
    def setUp(self):
        ' fake database context '
        self.fake_db = Mock()
        self.fake_db.cursor = MagicMock()


    def tearDown(self):
        self.fake_db.close()


    def test__should_call_select__with_exception(self):
        # arrange
        expected_exception = KeyError("Bang!")

        with patch.object(ExecHelper, 'select', side_effect=expected_exception):
            # act and assert

            with self.assertRaises(Exception):
                get_number_of_resources(self.fake_db, 99, auth_user=99)


    def test__should_call_select__return_no_items(self):
        # arrange
        expected_result = []

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act
            
            actual_results = get_number_of_resources(self.fake_db, 677, auth_user=6079)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                'lesson__get_number_of_resources'
                , (677,1,6079)
                , []
                , log_info=handle_log_info)

            self.assertEqual(0, actual_results)


    def test__should_call_select__return_single_item(self):
        # arrange
        expected_result = [
            (4345, "Markdown")
        ]

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act

            actual_results = get_number_of_resources(self.fake_db, 12, auth_user=6079)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                "lesson__get_number_of_resources"
                , (12,1,6079)
                , []
                , log_info=handle_log_info)
            
            self.assertEqual(1, actual_results)


    def test__should_call_select__return_multiple_item(self):
        # arrange
        expected_result = [
            (934, "Book"),
            (666, "Markdown"),
            (37, "Video")
        ]

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act

            actual_results = get_number_of_resources(self.fake_db, 22, auth_user=6079)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                "lesson__get_number_of_resources"
                , (22, 1, 6079)
                , []
                , log_info=handle_log_info)
            
            self.assertEqual(3, actual_results)
