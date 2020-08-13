from unittest import TestCase
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper

from shared.models.cls_schemeofwork import SchemeOfWorkModel as Model, handle_log_info


class test_db__get_options(TestCase):
    
    def setUp(self):
        ' fake database context '
        self.fake_db = Mock()
        self.fake_db.cursor = MagicMock()
        handle_log_info = MagicMock()

    def tearDown(self):
        self.fake_db.close()


    def test__should_call_execSql_with_exception(self):
        # arrange
        expected_exception = KeyError("Bang!")

        with patch.object(ExecHelper, 'execSql', side_effect=expected_exception):
            # act and assert

            with self.assertRaises(Exception):
                Model.get_options(self.fake_db)


    def test__should_call_execSql_return_no_items(self):
        # arrange
        expected_result = []

        with patch.object(ExecHelper, 'execSql', return_value=expected_result):
            # act
            
            rows = Model.get_options(self.fake_db, 99)
            
            # assert

            ExecHelper.execSql.assert_called_with(
                self.fake_db,
                "CALL scheme_of_work__get_options(99)"
                , [])
            self.assertEqual(0, len(rows))


    def test__should_call_execSql_return_single_item(self):
        # arrange
        expected_result = [(123, "Item 1", "Praesent tempus facilisis pharetra. Pellentesque.", 20)]

        with patch.object(ExecHelper, 'execSql', return_value=expected_result):
            # act

            rows = Model.get_options(self.fake_db, 99)
            
            # assert

            ExecHelper.execSql.assert_called_with(self.fake_db,
                "CALL scheme_of_work__get_options(99)"
                , [])
            
            self.assertEqual(1, len(rows))
            self.assertEqual(123, rows[0].id)
            self.assertEqual("Item 1", rows[0].name)
            self.assertEqual("Praesent tempus facilisis pharetra. Pellentesque.", rows[0].key_stage_name)



    def test__should_call_execSql_return_multiple_item(self):
        # arrange
        expected_result = [
            (1, "Item 1","Lorem ipsum dolor sit amet.",5),
            (2,"Item 2","Nulla porttitor quis tortor ac.",8),
            (3, "Item 3","Sed vehicula, quam nec sodales.",97)]

        with patch.object(ExecHelper, 'execSql', return_value=expected_result):
            # act

            rows = Model.get_options(self.fake_db, 99)
            
            # assert

            ExecHelper.execSql.assert_called_with(
                self.fake_db,
                "CALL scheme_of_work__get_options(99)"
                , [])

            self.assertEqual(3, len(rows))

            self.assertEqual(1, rows[0].id)
            self.assertEqual("Item 1", rows[0].name)
            self.assertEqual("Lorem ipsum dolor sit amet.", rows[0].key_stage_name)

            self.assertEqual(3, rows[2].id)
            self.assertEqual("Item 3", rows[2].name)
            self.assertEqual("Sed vehicula, quam nec sodales.", rows[2].key_stage_name)
