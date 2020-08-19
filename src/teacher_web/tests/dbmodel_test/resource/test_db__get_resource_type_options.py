from unittest import TestCase, skip
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper

# create test context

from shared.models.cls_resource import ResourceModel, handle_log_info

get_resource_type_options = ResourceModel.get_resource_type_options


class test_db__get_resource_type_options(TestCase):
    
    def setUp(self):
        ' fake database context '
        self.fake_db = Mock()
        self.fake_db.cursor = MagicMock()


    def tearDown(self):
        self.fake_db.close()


    def test__should_call_execSql_with_exception(self):
        # arrange
        expected_exception = KeyError("Bang!")

        with patch.object(ExecHelper, 'select', side_effect=expected_exception):
            # act and assert

            with self.assertRaises(Exception):
                get_resource_type_options(self.fake_db, auth_user=1)


    def test__should_call_execSql_return_no_items(self):
        # arrange
        expected_result = []

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act
            
            rows = get_resource_type_options(self.fake_db, auth_user=6079)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                'resource_type__get_options', (6079,)
                , []
                , log_info=handle_log_info)

            self.assertEqual(0, len(rows))


    def test__should_call_execSql_return_single_item(self):
        # arrange
        expected_result = [
            (4345, "Markdown")
        ]

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act

            rows = get_resource_type_options(self.fake_db, auth_user=6079)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                'resource_type__get_options'
                , (6079,)
                , []
                , log_info=handle_log_info)
            
            self.assertEqual(1, len(rows))

            self.assertEqual(4345, rows[0].id)
            self.assertEqual("Markdown", rows[0].name)


    def test__should_call_execSql_return_multiple_item(self):
        # arrange
        expected_result = [
            (934, "Book"),
            (666, "Markdown"),
            (37, "Video")
        ]

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act

            rows = get_resource_type_options(self.fake_db, auth_user=6079)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                'resource_type__get_options' 
                , (6079,)
                , []
                , log_info=handle_log_info)
            
            self.assertEqual(3, len(rows))

            self.assertEqual("Book", rows[0].name)
            self.assertEqual("Video", rows[2].name)