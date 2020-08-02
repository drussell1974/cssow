from unittest import TestCase
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper

from shared.models.cls_schemeofwork import SchemeOfWorkDataAccess

get_schemeofwork_name_only = SchemeOfWorkDataAccess.get_schemeofwork_name_only


class test_db__get_schemeofwork_name_only(TestCase):
    
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
                get_schemeofwork_name_only(self.fake_db, 101)


    def test__should_call_execSql_return_no_items(self):
        # arrange
        expected_result = []

        with patch.object(ExecHelper, 'execSql', return_value=expected_result):
            # act
            
            actual_result = get_schemeofwork_name_only(self.fake_db, 99)
            
            # assert

            ExecHelper.execSql.assert_called_with(self.fake_db,
                "SELECT   sow.name as name  FROM sow_scheme_of_work as sow  LEFT JOIN auth_user as user ON user.id = sow.created_by  WHERE sow.id = 99;"
                , [])
            self.assertEqual("", actual_result)


    def test__should_call_execSql_return_single_item(self):
        # arrange
        expected_result = [["ipsum dolor sit amet."]]

        with patch.object(ExecHelper, 'execSql', return_value=expected_result):
            # act

            actual_result = get_schemeofwork_name_only(self.fake_db, 6)
            
            # assert

            ExecHelper.execSql.assert_called_with(self.fake_db,
                "SELECT   sow.name as name  FROM sow_scheme_of_work as sow  LEFT JOIN auth_user as user ON user.id = sow.created_by  WHERE sow.id = 6;"
            , [])
            self.assertEqual("ipsum dolor sit amet.", actual_result)



