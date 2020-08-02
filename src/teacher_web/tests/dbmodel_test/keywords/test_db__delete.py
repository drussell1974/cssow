from unittest import TestCase
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.cls_keyword import KeywordModel as Model, KeywordDataAccess, handle_log_info


delete = KeywordDataAccess.delete

class test_db__delete(TestCase):

    def setUp(self):
        ' fake database context '
        self.fake_db = Mock()
        self.fake_db.cursor = MagicMock()
        

    def tearDown(self):
        pass


    def test_should_raise_exception(self):
        # arrange
        expected_exception = KeyError("Bang!")

        model = Model(0, term="Morbi", definition="sit amet mauris ut ante porttitor interdum.")

        with patch.object(ExecHelper, 'execCRUDSql', side_effect=expected_exception):
            
            # act and assert
            with self.assertRaises(KeyError):
                # act 
                delete(self.fake_db, model.id)


    def test_should_call_execCRUDSql(self):
        # arrange
        model = Model(797, term="Morbi", definition="sit amet mauris ut ante porttitor interdum.")
        
        expected_result = 1

        with patch.object(ExecHelper, 'execCRUDSql', return_value=expected_result):
            # act

            actual_result = delete(self.fake_db, model.id)
            
            # assert

            ExecHelper.execCRUDSql.assert_called_with(self.fake_db, 
             "DELETE FROM sow_key_word WHERE id = '797'"
             , log_info=handle_log_info)
            
            self.assertEqual(expected_result, actual_result)