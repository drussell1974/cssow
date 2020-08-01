from ._unittest import TestCase, FakeDb
import shared.models.cls_content as test_context
from unittest.mock import Mock, MagicMock, patch
from unittest import skip
from shared.models.core.db_helper import ExecHelper

get_options = test_context.ContentDataAccess.get_options


class test_db_content__get_options(TestCase):

    def setUp(self):
        ' fake database context '
        self.fake_db = Mock()
        self.fake_db.cursor = MagicMock()
        test_context.handle_log_info = MagicMock()

    def tearDown(self):
        self.fake_db.close()


    def test__should_call_execSql_with_exception(self):
        # arrange
        expected_exception = KeyError("Bang!")

        with patch.object(ExecHelper, 'execSql', side_effect=expected_exception):
            # act and assert
            with self.assertRaises(Exception):
                get_options(self.fake_db, key_stage_id=0)
            

    def test__should_call_execSql_return_no_items(self):
        # arrange
        expected_result = []

        with patch.object(ExecHelper, 'execSql', return_value=expected_result):
            # act
            
            rows = get_options(self.fake_db, key_stage_id=1)

            # assert
            ExecHelper.execSql.assert_called_with(self.fake_db,'SELECT cnt.id as id, cnt.description as description FROM sow_content as cnt WHERE key_stage_id = 1;'
            , []
            , test_context.handle_log_info)
            
            self.assertEqual(0, len(rows))


    def test__should_call_execSql_return_single_item(self):
        # arrange
        expected_result = [(17, "Mauris augue est, malesuada eget libero nec.")]

        with patch.object(ExecHelper, 'execSql', return_value=expected_result):
            # act
            
            rows = get_options(self.fake_db, key_stage_id=2)
            
            # assert
            ExecHelper.execSql.assert_called_with(self.fake_db,'SELECT cnt.id as id, cnt.description as description FROM sow_content as cnt WHERE key_stage_id = 2;'
            , []
            , test_context.handle_log_info)
            
            self.assertEqual(1, len(rows))
            self.assertEqual(17, rows[0].id)
            self.assertEqual("Mauris augue est, malesuada eget libero nec.", rows[0].description)
            

    def test__should_call_execSql_return_multiple_items(self):
        # arrange
        expected_result = [
            (29,"Sed turpis augue, tristique sed elit ac."),
            (645,"Ut porta arcu a commodo viverra. Sed."),
            (107,"Nulla sit amet aliquet enim, quis laoreet."),
        ]
        with patch.object(ExecHelper, 'execSql', return_value=expected_result):
            # act
            
            rows = get_options(self.fake_db, key_stage_id=3)
            
            # assert
            ExecHelper.execSql.assert_called_with(self.fake_db,'SELECT cnt.id as id, cnt.description as description FROM sow_content as cnt WHERE key_stage_id = 3;'
            , []
            , test_context.handle_log_info)
            
            self.assertEqual(3, len(rows))

            self.assertEqual(29, rows[0].id)
            self.assertEqual("Sed turpis augue, tristique sed elit ac.", rows[0].description)

            self.assertEqual(107, rows[2].id)
            self.assertEqual("Nulla sit amet aliquet enim, quis laoreet.", rows[2].description)
