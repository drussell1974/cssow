from unittest import TestCase, skip
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.core.log import handle_log_info

import shared.models.cls_keyword as test_context 

# create test context

save_keywords_only = test_context.save_keywords_only
handle_log_info = test_context.handle_log_info

class test_db__save_keywords_only(TestCase):


    def setUp(self):
        ' fake database context '
        self.fake_db = Mock()
        self.fake_db.cursor = MagicMock()
        
    def tearDown(self):
        pass

    def test_should_raise_exception(self):
        # arrange
        keywords_to_try_and_save = "a,b,c"

        expected_exception = KeyError("Bang!")

        with patch.object(ExecHelper, 'execCRUDSql', side_effect=expected_exception):
            
            # act and assert
            with self.assertRaises(KeyError):
                # act 
                save_keywords_only(self.fake_db, keywords_to_try_and_save)


    def test_should_call_execCRUDSql(self):
         # arrange
        keywords_to_save = "a,b,c"

        expected_result = [("12")]

        with patch.object(ExecHelper, 'execCRUDSql', return_value=expected_result):
            # act

            actual_result = save_keywords_only(self.fake_db, keywords_to_save)
            
            # assert
            ExecHelper.execCRUDSql.assert_called_with(self.fake_db, 
                "INSERT INTO sow_key_word (name, definition) VALUES ('c', '');"
                , result=[]
                , log_info=handle_log_info)
        
