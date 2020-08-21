from unittest import TestCase, skip
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper

import shared.models.cls_keyword as test_context 

get_model = test_context.KeywordModel.get_model
handle_log_info = test_context.handle_log_info
Model = test_context.KeywordModel

class test_db__get_model(TestCase):


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
                get_model(self.fake_db, 4)


    def test__should_call_execSql_return_no_items(self):
        # arrange
        expected_result = []

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act
            
            actual_results = get_model(self.fake_db, 22, auth_user=6079)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                'keyword__get'
                , (22, 6079)
                , []
                , handle_log_info)
                
            self.assertEqual(0, actual_results.id)


    def test__should_call_execSql_return_single_item(self):
        # arrange
        expected_result = [
            (702, "Fringilla", "purus lacus, ut volutpat nibh euismod.")
            ]

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act

            actual_results = get_model(self.fake_db, 702, auth_user=6079)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                "keyword__get"
                , (702, 6079)
                , []
                , handle_log_info)
                
            self.assertEqual(702, actual_results.id)
            self.assertEqual("Fringilla", actual_results.term),
            self.assertEqual("purus lacus, ut volutpat nibh euismod.", actual_results.definition)
