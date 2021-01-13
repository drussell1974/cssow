from ._unittest import TestCase, FakeDb
from unittest import skip
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper

import shared.models.core.log as test_context


class test_db_keyword__get_options(TestCase):

    def setUp(self):
        ' fake database context '
        self.fake_db = Mock()
        self.fake_db.cursor = MagicMock()
        test_context.handle_log_info = MagicMock()


    def tearDown(self):
        pass


    def test_should_call_insert_with_exception(self):# arrange
        expected_exception = KeyError("Bang!")

        with patch.object(ExecHelper, 'insert', side_effect=expected_exception):
            
            # act and assert
            with self.assertRaises(Exception):
                # act 

                log = test_context.Log(self.fake_db, test_context.LOG_TYPE.NONE)

                # assert

                log.write("something happened")

    @skip("check logging insert strip data")
    def test_should_call_insert_with_new_id__when_logging_is_enabled_True(self):
         # arrange
        expected_result = None
    
        log = test_context.Log(self.fake_db, test_context.LOG_TYPE.Verbose)
        
        with patch.object(ExecHelper, 'insert', return_value=expected_result):
            # act
        
            log.write("something happened", "", test_context.LOG_TYPE.Verbose)
            
            # assert
            
            ExecHelper.insert.assert_called()


    def test_should_call_insert_with_new_id__when_logging_is_enabled__false(self):
         # arrange
        expected_result = None

        log = test_context.Log(self.fake_db, test_context.LOG_TYPE.NONE)


        with patch.object(ExecHelper, 'insert', return_value=expected_result):
            # act
        
            log.write("something happened", "", test_context.LOG_TYPE.Verbose, 76)
            
            # assert
            
            ExecHelper.insert.assert_not_called()
   

    def test_should_call_insert_with_new_id__when_logging_is_enabled__default(self):
         # arrange
        expected_result = None
    
        log = test_context.Log(self.fake_db)


        #########################
        # DO NOT set is_enabled #
        #########################
        #log.is_enabled = False
        
        with patch.object(ExecHelper, 'insert', return_value=expected_result):
            # act
        
            log.write("something happened", "", test_context.LOG_TYPE.Verbose, 77)
            
            # assert
            
            ExecHelper.insert.assert_not_called()
   