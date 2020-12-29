from unittest import TestCase, skip
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.log import handle_log_info
from shared.models.core.db_helper import ExecHelper
from shared.models.cls_keyword import KeywordModel, KeywordDataAccess

merge_duplicates = KeywordModel.merge_duplicates


class test_db__merge_duplicates(TestCase):


    def setUp(self):
        ' fake database context '
        self.fake_db = Mock()
        self.fake_db.cursor = MagicMock()
        self.handle_log_info = MagicMock()
        
    def tearDown(self):
        pass


    def test_should_raise_exception(self):
        # arrange
        expected_exception = KeyError("Bang!")

        with patch.object(KeywordDataAccess, 'merge_duplicates', side_effect=expected_exception):
            
            # act and assert
            with self.assertRaises(Exception):
                # act 
                merge_duplicates(self.fake_db, 1, 123, 1069)


    def test_should_call_merge_duplicates(self):
        # arrange
        
        expected_result = [(1,)]
        with patch.object(KeywordModel, 'get_model', return_value=KeywordModel(12)):        
            with patch.object(ExecHelper, 'custom', return_value=expected_result):
                # act

                actual_result = merge_duplicates(self.fake_db, 12, 123, 1069)
                
                # assert
                ExecHelper.custom.assert_called_with(self.fake_db, "keyword__merge_duplicates", handle_log_info)
                KeywordModel.get_model.assert_called()
                self.assertEqual(12, actual_result.id)

