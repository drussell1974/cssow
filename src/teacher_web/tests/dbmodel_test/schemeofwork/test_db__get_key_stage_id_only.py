from unittest import TestCase
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper

from shared.models.cls_schemeofwork import SchemeOfWorkModel

get_key_stage_id_only = SchemeOfWorkModel.get_key_stage_id_only


class test_db__get_key_stage_id_only(TestCase):
    
    def setUp(self):
        ' fake database context '
        self.fake_db = Mock()
        self.fake_db.cursor = MagicMock()

    def tearDown(self):
        self.fake_db.close()


    def test__should_call_execSql_with_exception(self):
        # arrange
        expected_exception = KeyError("Bang!")

        with patch.object(ExecHelper, 'execSql', side_effect=expected_exception):
            # act and assert

            with self.assertRaises(Exception):
                get_key_stage_id_only(self.fake_db, 999, 99)


    def test__should_call_execSql_return_no_items(self):
        # arrange
        expected_result = []

        with patch.object(ExecHelper, 'execSql', return_value=expected_result):
            # act
            
            actual_result = get_key_stage_id_only(self.fake_db, 101, 99)
            
            # assert

            ExecHelper.execSql.assert_called_with(self.fake_db,
                "CALL scheme_of_work__get_key_stage_id_only(101, 99)"
                , [])
            self.assertEqual(0, actual_result)


    def test__should_call_execSql_return_single_item(self):
        # arrange
        expected_result = [[3]]

        with patch.object(ExecHelper, 'execSql', return_value=expected_result):
            # act

            actual_result = get_key_stage_id_only(self.fake_db, 6, 99)
            
            # assert

            ExecHelper.execSql.assert_called_with(self.fake_db,
                "CALL scheme_of_work__get_key_stage_id_only(6, 99)"
                , [])
            self.assertEqual(3, actual_result)



