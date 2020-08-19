from unittest.mock import Mock, MagicMock, patch
from unittest import TestCase, skip
from shared.models.core.db_helper import ExecHelper


class test_db_helper__insert(TestCase):
    
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
            execHelper.insert(self.fake_db, "a_stored_procedure_that_inserts_data", (1, "A", 2, "B", 3, "C"), self.handle_log_info__mock)


    def test__should_return_an_empty_result(self):
        
        # arrange

        cur = MagicMock()
        cur.callproc = Mock()
        cur.fetchone = Mock(return_value = [])

        fake_db = Mock()
        fake_db.cursor = MagicMock(return_value = cur)

        # act      

        execHelper = ExecHelper()
        execHelper.begin(fake_db)
        
        result = execHelper.insert(fake_db, "a_fake_stored_procedure_will_insert_data", ("var1","var2","var3"))

        # assert

        cur.callproc.assert_called_with('a_fake_stored_procedure_will_insert_data', ('var1', 'var2', 'var3'))
        cur.fetchone.called_with(None)

        self.assertEqual([], result)


    def test__should_return_an_new_id_from_LAST_INSERT_ID_in_stored_proc(self):
        
        # arrange

        cur = MagicMock()
        cur.callproc = Mock()
        cur.fetchone = Mock(return_value = [(645,)])

        fake_db = Mock()
        fake_db.autocommit = True
        fake_db.cursor = MagicMock(return_value = cur)

        # act      

        execHelper = ExecHelper()
        execHelper.begin(fake_db)

        result = execHelper.insert(fake_db, "a_fake_stored_procedure_will_insert_data", ("var1","var2","var3"))

        # assert

        cur.callproc.assert_called_with('a_fake_stored_procedure_will_insert_data', ('var1', 'var2', 'var3'))
        cur.fetchone.called_with(None)

        self.assertEqual([(645,)], result)

        

