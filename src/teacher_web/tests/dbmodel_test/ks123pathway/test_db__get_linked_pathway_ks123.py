from unittest import TestCase, skip
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper

import shared.models.cls_ks123pathway as test_context 

get_linked_pathway_ks123 = test_context.get_linked_pathway_ks123
handle_log_info = test_context.handle_log_info


class test_db__get_linked_pathway_ks123(TestCase):
    
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
                get_linked_pathway_ks123(self.fake_db, 87)


    def test__should_call_execSql_return_no_items(self):
        # arrange
        expected_result = []

        with patch.object(ExecHelper, 'execSql', return_value=expected_result):
            # act
            
            rows = get_linked_pathway_ks123(self.fake_db, 67)
            
            # assert

            ExecHelper.execSql.assert_called_with(self.fake_db,
                "SELECT pw.id as id, pw.objective as objective FROM sow_lesson__has__ks123_pathway as le_pw INNER JOIN sow_ks123_pathway AS pw ON pw.id = le_pw.ks123_pathway_id WHERE le_pw.lesson_id = 67;"
                , []
                , log_info=handle_log_info)

            self.assertEqual(0, len(rows))


    def test__should_call_execSql_return_single_item(self):
        # arrange
        expected_result = [
            [34, "Morbi sit amet mauris ut ante porttitor interdum."]
        ]

        with patch.object(ExecHelper, 'execSql', return_value=expected_result):
            # act

            rows = get_linked_pathway_ks123(self.fake_db, 236)
            
            # assert

            ExecHelper.execSql.assert_called_with(self.fake_db,
                "SELECT pw.id as id, pw.objective as objective FROM sow_lesson__has__ks123_pathway as le_pw INNER JOIN sow_ks123_pathway AS pw ON pw.id = le_pw.ks123_pathway_id WHERE le_pw.lesson_id = 236;"
                , []
                , log_info=handle_log_info)
            
            self.assertEqual(1, len(rows))

            self.assertEqual(34, rows[0][0])
            self.assertEqual("Morbi sit amet mauris ut ante porttitor interdum.", rows[0][1])


    def test__should_call_execSql_return_multiple_item(self):
        # arrange
        expected_result = [
            [356, "Morbi sit amet mauris ut ante porttitor interdum."],
            [445, "Curabitur vestibulum ipsum vitae mi iaculis, id dapibus."],
            [777, "Sed blandit fringilla dui et vehicula. Donec sagittis."]
        ]

        with patch.object(ExecHelper, 'execSql', return_value=expected_result):
            # act

            rows = get_linked_pathway_ks123(self.fake_db, 403)
            
            # assert

            ExecHelper.execSql.assert_called_with(self.fake_db,
                "SELECT pw.id as id, pw.objective as objective FROM sow_lesson__has__ks123_pathway as le_pw INNER JOIN sow_ks123_pathway AS pw ON pw.id = le_pw.ks123_pathway_id WHERE le_pw.lesson_id = 403;"
                , []
                , log_info=handle_log_info)
            
            self.assertEqual(3, len(rows))

            self.assertEqual(356, rows[0][0])
            self.assertEqual("Morbi sit amet mauris ut ante porttitor interdum.", rows[0][1])

            self.assertEqual(777, rows[2][0])
            self.assertEqual("Sed blandit fringilla dui et vehicula. Donec sagittis.", rows[2][1])
