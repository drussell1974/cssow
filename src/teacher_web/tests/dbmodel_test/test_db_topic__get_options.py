from ._unittest import TestCase, FakeDb
import shared.models.cls_topic as db_topic
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper

class test_db_topic__get_options__level_1(TestCase):

    def setUp(self):
        ' pass function to this fake class to mock the web2py database functions '
        self.fake_db = FakeDb()
        self.fake_db.connect()
        db_topic.handle_log_info = MagicMock()


    def tearDown(self):
        self.fake_db.close()

    
    def test__should_call_execSql_with_exception(self):
        # arrange
        expected_result = Exception('Bang')
        
        with patch.object(ExecHelper, "execSql", side_effect=expected_result):
            # act and assert
            with self.assertRaises(Exception):
                db_topic.get_options(self.fake_db, lvl = 1)


    def test__should_call_execSql_return_no_items(self):
        # arrange

        expected_result = []
        
        with patch.object(ExecHelper, 'execSql', return_value=expected_result):
            # act

            rows = db_topic.get_options(self.fake_db, lvl = 2, topic_id = 1)
            
            # assert
            ExecHelper.execSql.assert_called_with(self.fake_db,'SELECT id, name, created, created_by FROM sow_topic WHERE lvl = 2 and parent_id = 1;', [], db_topic.handle_log_info)
            self.assertEqual(0, len(rows))


    def test__should_call_execSql_return_single_items(self):
        # arrange

        expected_result = [(1,"Operators","X","X")]

        with patch.object(ExecHelper, 'execSql',  return_value=expected_result):
            
            # act
            rows = db_topic.get_options(self.fake_db, lvl = 2, topic_id = 2)
            
            # assert
            ExecHelper.execSql.assert_called_with(self.fake_db, 'SELECT id, name, created, created_by FROM sow_topic WHERE lvl = 2 and parent_id = 2;', [], db_topic.handle_log_info)
            self.assertEqual(1, len(rows))
            self.assertEqual("Operators", rows[0]["name"], "First item not as expected")
        


    def test__should_call_execSql_return_multiple_items(self):
        # arrange
        
        expected_result = [(1,"Binary","X","X"),(2,"Operators","X","X"),(3,"Data compression","X","X")]

        with patch.object(ExecHelper, 'execSql',  return_value=expected_result):
            
            # act
            
            rows = db_topic.get_options(self.fake_db, lvl = 2, topic_id = 3)
            
            # assert
            ExecHelper.execSql.assert_called_with(self.fake_db, 'SELECT id, name, created, created_by FROM sow_topic WHERE lvl = 2 and parent_id = 3;', [], db_topic.handle_log_info)
            self.assertEqual(3, len(rows))
            self.assertEqual("Binary", rows[0]["name"], "First item not as expected")
            self.assertEqual("Data compression", rows[len(rows)-1]["name"], "Last item not as expected")
