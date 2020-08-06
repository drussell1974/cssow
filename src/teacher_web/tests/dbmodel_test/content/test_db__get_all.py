from unittest import TestCase, skip
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper

from shared.models.cls_content import ContentModel, handle_log_info

get_all = ContentModel.get_all

class test_db__get_all(TestCase):


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
                get_all(self.fake_db)


    def test__should_call_execSql_return_no_items(self):
        # arrange
        expected_result = []

        with patch.object(ExecHelper, 'execSql', return_value=expected_result):
            # act
            
            rows = get_all(self.fake_db, key_stage_id=7, auth_user=99)
            
            # assert

            ExecHelper.execSql.assert_called_with(self.fake_db,
                "SELECT id as id, description as description, letter as letter_prefix, published as published FROM sow_content WHERE key_stage_id = 7 AND (published = 1 or created_by = 99) ORDER BY letter ASC;"
                , []
                , log_info=handle_log_info)
                
            self.assertEqual(0, len(rows))


    def test__should_call_execSql_return_single_item(self):
        # arrange
        expected_result = [
            (702, "purus lacus, ut volutpat nibh euismod.", "A",0)
            ]

        with patch.object(ExecHelper, 'execSql', return_value=expected_result):
            # act

            actual_results = get_all(self.fake_db, key_stage_id=5, auth_user=99)
            
            # assert

            ExecHelper.execSql.assert_called_with(self.fake_db,
                "SELECT id as id, description as description, letter as letter_prefix, published as published FROM sow_content WHERE key_stage_id = 5 AND (published = 1 or created_by = 99) ORDER BY letter ASC;"
                , []
                , log_info=handle_log_info)
                

            self.assertEqual(1, len(actual_results))

            self.assertEqual(702, actual_results[0].id)
            self.assertEqual("purus lacus, ut volutpat nibh euismod.", actual_results[0].description)
            self.assertEqual("A", actual_results[0].letter_prefix),


    def test__should_call_execSql_return_multiple_item(self):
        # arrange
        expected_result = [
            (1021, "nec arcu nec dolor vehicula ornare non.", "X", 0),
            (1022, "purus lacus, ut volutpat nibh euismod.", "Y", 0),
            (1023, "rutrum lorem a arcu ultrices, id mollis", "Z", 0)
        ]

        with patch.object(ExecHelper, 'execSql', return_value=expected_result):
            # act

            actual_results = get_all(self.fake_db, key_stage_id=5, auth_user=99)
            
            # assert

            ExecHelper.execSql.assert_called_with(self.fake_db,
                "SELECT id as id, description as description, letter as letter_prefix, published as published FROM sow_content WHERE key_stage_id = 5 AND (published = 1 or created_by = 99) ORDER BY letter ASC;"
                 , []
                 , log_info=handle_log_info)

            self.assertEqual(3, len(actual_results))

            self.assertEqual(1021, actual_results[0].id)
            self.assertEqual("X", actual_results[0].letter_prefix),
            self.assertEqual("nec arcu nec dolor vehicula ornare non.", actual_results[0].description)
            

            self.assertEqual(1023, actual_results[2].id)
            self.assertEqual("Z", actual_results[2].letter_prefix),
            self.assertEqual("rutrum lorem a arcu ultrices, id mollis", actual_results[2].description)
