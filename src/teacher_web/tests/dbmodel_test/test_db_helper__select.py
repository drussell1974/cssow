from unittest.mock import Mock, MagicMock, patch
from unittest import TestCase, skip
from shared.models.core.db_helper import ExecHelper


class test_db_helper__select(TestCase):
    
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
            execHelper.select(self.fake_db, "a_stored_procedure_that_select_data", (1, "A", 2, "B", 3, "C"), [], self.handle_log_info__mock)


    def test__should_be_able_to_return_no_items(self):
        
        # arrange

        cur = MagicMock()
        cur.callproc = Mock()
        cur.fetchall = Mock(return_value = [])

        fake_db = Mock()
        fake_db.cursor = MagicMock(return_value = cur)

        # act      

        execHelper = ExecHelper()

        result = execHelper.select(fake_db, "a_fake_stored_procedure_will_returns_no_rows", ("var1","var2","var3"), [])

        # assert

        cur.callproc.assert_called_with('a_fake_stored_procedure_will_returns_no_rows', ('var1', 'var2', 'var3'))
        cur.fetchall.called_with(None)

        self.assertEqual([], result)


    def test__should_be_able_to_return_a_single_item(self):
        
        # arrange
        
        cur = MagicMock()
        cur.callproc = Mock()
        cur.fetchall = Mock(return_value =  [(123, "Item 1")])

        fake_db = Mock()
        fake_db.cursor = MagicMock(return_value = cur)

        # act      

        execHelper = ExecHelper()

        result = execHelper.select(fake_db, "a_fake_stored_procedure_will_returns_one_row", ("var1","var2","var3"), [], self.handle_log_info__mock)

        # assert

        cur.callproc.assert_called_with('a_fake_stored_procedure_will_returns_one_row', ('var1', 'var2', 'var3'))
        cur.fetchall.called_with(None)

        self.assertEqual(1, len(result))
        self.assertEqual(123, result[0][0])
        self.assertEqual("Item 1", result[0][1])


    def test__should_be_able_to_return_multiple_item(self):

        # arrange
        
        cur = MagicMock()
        cur.callproc = Mock()
        cur.fetchall = Mock(return_value = [(1, "Item 1"),(2,"Item 2"),(3, "Item 3")])

        fake_db = Mock()
        fake_db.cursor = MagicMock(return_value = cur)

        # act      

        execHelper = ExecHelper()

        result = execHelper.select(fake_db, "a_fake_stored_procedure_will_returns_three_rows", ("var1","var2","var3"), [])

        # assert

        cur.callproc.assert_called_with('a_fake_stored_procedure_will_returns_three_rows', ('var1', 'var2', 'var3'))
        cur.fetchall.called_with(None)

        self.assertEqual(3, len(result))
        
        self.assertEqual(1, result[0][0])
        self.assertEqual("Item 1", result[0][1])
        
        self.assertEqual(3, result[2][0])
        self.assertEqual("Item 3", result[2][1])
        
        

