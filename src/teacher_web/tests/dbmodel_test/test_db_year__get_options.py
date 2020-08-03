from unittest import TestCase
from shared.models.cls_year import YearModel as Model
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper

class test_YearDataAccess__get_options(TestCase):

    def setUp(self):
        ' fake database context '
        self.fake_db = Mock()
        self.fake_db.cursor = MagicMock()


    def tearDown(self):
        self.fake_db.close()


    def test__should_call_execSql_with_exception(self):

        # arrange
        expected_result = Exception('Bang')
        
        with patch.object(ExecHelper, "execSql", side_effect=expected_result):
            # act and assert
            with self.assertRaises(Exception):
                Model.get_options(self.fake_db, key_stage_id = 4)
            

    def test__should_call_execSql_no_items(self):
        # arrange
        expected_result = []

        with patch.object(ExecHelper, "execSql", return_value=expected_result):
                
            # act
            
            rows = Model.get_options(self.fake_db, key_stage_id = 1)
            
            # assert

            ExecHelper.execSql.assert_called_with(self.fake_db, "SELECT id, name FROM sow_year WHERE key_stage_id = 1;", [])
            self.assertEqual(0, len(rows))


    def test__should_call_execSql_single_items(self):
        # arrange
        expected_result = [(1,"Yr4")]
        
        with patch.object(ExecHelper, "execSql", return_value=expected_result):
            
            # act

            rows = Model.get_options(self.fake_db, key_stage_id = 2)
            
            # assert

            ExecHelper.execSql.assert_called_with(self.fake_db, "SELECT id, name FROM sow_year WHERE key_stage_id = 2;", [])
            self.assertEqual(1, len(rows))
            self.assertEqual("Yr4", rows[0].name, "First item not as expected")
            

    def test__should_call_execSql_multiple_items(self):
        # arrange
        expected_result = [(1,"Yr7"), (2, "Yr8"), (3, "Yr9")]
        
        with patch.object(ExecHelper, "execSql", return_value=expected_result):
            # act
            rows = Model.get_options(self.fake_db, key_stage_id = 3)
            
            # assert

            ExecHelper.execSql.assert_called_with(self.fake_db, 'SELECT id, name FROM sow_year WHERE key_stage_id = 3;', [])
            self.assertEqual(3, len(rows))
            self.assertEqual("Yr7", rows[0].name, "First item not as expected")
            self.assertEqual("Yr9", rows[len(rows)-1].name, "Last item not as expected")

