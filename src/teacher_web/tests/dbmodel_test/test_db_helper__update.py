from unittest.mock import Mock, MagicMock, patch
from unittest import TestCase, skip
from shared.models.core.db_helper import ExecHelper


class test_db_helper__update(TestCase):
    
    def setUp(self):
        self.handle_log_info__mock = MagicMock()
        pass 

    def tearDown(self):
        pass


    def test__should_handle_exception(self):
        
        expected_exception = KeyError("Bang!")

        # arrange
        fake_db = Mock()
        fake_db.cursor = MagicMock()
        fake_db.cursor.callproc = Mock(side_effect = expected_exception)
        
        # act and assert

        execHelper = ExecHelper()

        with self.assertRaises(Exception):
            execHelper.update(self.fake_db, "a_fake_stored_procedure_will_update_data_and_return_row_count", (1, "A", 2, "B", 3, "C"), self.handle_log_info__mock)


    def test__should_return_zero_row_count(self):
        
        # arrange

        cur = MagicMock()
        cur.callproc = Mock()
        cur.rowcount = 0

        fake_db = Mock()
        fake_db.autocommit = False
        fake_db.cursor = MagicMock(return_value = cur)

        # act      

        execHelper = ExecHelper()
        execHelper.begin(fake_db)

        result = execHelper.update(fake_db, "a_fake_stored_procedure_will_update_data_and_return_row_count", ("var1","var2","var3"))

        # assert

        cur.callproc.assert_called_with('a_fake_stored_procedure_will_update_data_and_return_row_count', ('var1', 'var2', 'var3'))

        self.assertEqual(0, result)


    def test__should_return_single_row_count(self):
        
        # arrange

        cur = MagicMock()
        cur.callproc = Mock()
        cur.rowcount = 1

        fake_db = Mock()
        fake_db.cursor = MagicMock(return_value = cur)

        # act      

        execHelper = ExecHelper()
        execHelper.begin(fake_db)

        result = execHelper.update(fake_db, "a_fake_stored_procedure_will_update_data_and_return_row_count", ("var1","var2","var3"))

        # assert

        cur.callproc.assert_called_with('a_fake_stored_procedure_will_update_data_and_return_row_count', ('var1', 'var2', 'var3'))

        self.assertEqual(1, result)


    def test__should_return_multipe_row_count(self):
        
        # arrange

        cur = MagicMock()
        cur.callproc = Mock()
        cur.rowcount = 5

        fake_db = Mock()
        fake_db.cursor = MagicMock(return_value = cur)

        # act      

        execHelper = ExecHelper()
        execHelper.begin

        result = execHelper.update(fake_db, "a_fake_stored_procedure_will_update_data_and_return_row_count", ("var1","var2","var3"))

        # assert

        cur.callproc.assert_called_with('a_fake_stored_procedure_will_update_data_and_return_row_count', ('var1', 'var2', 'var3'))

        self.assertEqual(5, result)

        

