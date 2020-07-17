from unittest import TestCase
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper

from shared.models.cls_schemeofwork import get_key_stage_id_only


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
                get_key_stage_id_only(self.fake_db, 101)


    def test__should_call_execSql_return_no_items(self):
        # arrange
        expected_result = []

        with patch.object(ExecHelper, 'execSql', return_value=expected_result):
            # act
            
            actual_result = get_key_stage_id_only(self.fake_db, 99)
            
            # assert

            ExecHelper.execSql.assert_called_with(self.fake_db,
                "SELECT   sow.key_stage_id as key_stage_id  FROM sow_scheme_of_work as sow  LEFT JOIN auth_user as user ON user.id = sow.created_by  WHERE sow.id = 99;"
                , [])
            self.assertEqual(0, actual_result)


    def test__should_call_execSql_return_single_item(self):
        # arrange
        expected_result = [[3]]

        with patch.object(ExecHelper, 'execSql', return_value=expected_result):
            # act

            actual_result = get_key_stage_id_only(self.fake_db, 6)
            
            # assert

            ExecHelper.execSql.assert_called_with(self.fake_db,
                "SELECT   sow.key_stage_id as key_stage_id  FROM sow_scheme_of_work as sow  LEFT JOIN auth_user as user ON user.id = sow.created_by  WHERE sow.id = 6;"
            , [])
            self.assertEqual(3, actual_result)



