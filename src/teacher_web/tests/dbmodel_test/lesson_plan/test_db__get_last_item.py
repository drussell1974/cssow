from unittest import TestCase, skip
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper

import shared.models.cls_lessonplan as test_context

# test context

get_last_item = test_context.get_last_item
handle_log_info = test_context.handle_log_info

class test_db__get_model(TestCase):
    

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
                get_last_item(self.fake_db, lesson_id=653)


    def test__should_call_execSql_return_no_items(self):
        # arrange
        expected_result = []

        with patch.object(ExecHelper, 'execSql', return_value=expected_result):
            # act

            actual_results = get_last_item(self.fake_db, lesson_id=89)
            
            # assert

            ExecHelper.execSql.assert_called_with(self.fake_db,
                "SELECT pln.id as id, pln.title as title, pln.description as description, pln.duration_minutes as duration, pln.task_icon,  pln.order_of_delivery_id FROM sow_lesson_plan as pln INNER JOIN sow_lesson as le ON le.id = pln.lesson_id WHERE le.id = 89 ORDER BY pln.order_of_delivery_id DESC  LIMIT 1;"
                , []
                , log_info=handle_log_info)

            self.assertTrue(actual_results.is_new())
            

    def test__should_call_execSql_return_single_item(self):
        # arrange

        expected_result = [(
            23,                     # " pln.id as id," \
            "Starter Activity",     # " pln.title as title," \
            "Sort the shapes",      # " pln.description as description," \
            5,                      # " pln.duration_minutes as duration," \
            "fa-timer",             #" pln.task_icon, " \
            1                       #" pln.order_of_delivery_id "\
        )]
        
        with patch.object(ExecHelper, 'execSql', return_value=expected_result):
            # act

            actual_results = get_last_item(self.fake_db, lesson_id=22)

            # assert

            ExecHelper.execSql.assert_called_with(self.fake_db,
                "SELECT pln.id as id, pln.title as title, pln.description as description, pln.duration_minutes as duration, pln.task_icon,  pln.order_of_delivery_id FROM sow_lesson_plan as pln INNER JOIN sow_lesson as le ON le.id = pln.lesson_id WHERE le.id = 22 ORDER BY pln.order_of_delivery_id DESC  LIMIT 1;"
                , []
                , log_info=handle_log_info)
        

            self.assertEqual(23, actual_results.id)
            self.assertEqual("Starter Activity", actual_results.title),
            self.assertEqual("Sort the shapes", actual_results.description),
            self.assertEqual(5, actual_results.duration)
            self.assertEqual("fa-timer", actual_results.task_icon)
            





