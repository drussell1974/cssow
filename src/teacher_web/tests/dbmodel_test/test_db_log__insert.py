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

        with patch.object(ExecHelper, 'execCRUDSql', side_effect=expected_exception):
            
            # act and assert
            with self.assertRaises(Exception):
                # act 

                log = test_context.Log()
                log.is_enabled = True
                # assert

                log.write(self.fake_db, "something happened")


    def test_should_call_insert_with_new_id__when_logging_is_enabled_True(self):
         # arrange
        expected_result = None
    
        log = test_context.Log()
        log.is_enabled = True
        
        with patch.object(ExecHelper, 'execCRUDSql', return_value=expected_result):
            # act
        
            log.write(self.fake_db, "something happened")
            
            # assert
            
            ExecHelper.execCRUDSql.assert_called()
            # time is different to just assert_called
            #ExecHelper.execCRUDSql.assert_called(RT INTO sow_logging (details, created) VALUES ('something happened', '2020-07-15 03:20:54.902667');")

    def test_should_call_insert_with_new_id__when_logging_is_enabled__false(self):
         # arrange
        expected_result = None
    
        log = test_context.Log()
        log.is_enabled = False
        
        with patch.object(ExecHelper, 'execCRUDSql', return_value=expected_result):
            # act
        
            log.write(self.fake_db, "something happened")
            
            # assert
            
            ExecHelper.execCRUDSql.assert_not_called()
   

    def test_should_call_insert_with_new_id__when_logging_is_enabled__default(self):
         # arrange
        expected_result = None
    
        log = test_context.Log()
        
        #########################
        # DO NOT set is_enabled #
        #########################
        #log.is_enabled = False
        
        with patch.object(ExecHelper, 'execCRUDSql', return_value=expected_result):
            # act
        
            log.write(self.fake_db, "something happened")
            
            # assert
            
            ExecHelper.execCRUDSql.assert_not_called()
   