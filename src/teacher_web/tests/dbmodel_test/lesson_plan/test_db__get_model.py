from unittest import TestCase, skip
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper

from shared.models.cls_lessonplan import LessonPlanDataAccess, handle_log_info

# test context

get_model = LessonPlanDataAccess.get_model

@skip("Deprecated. No longer used.")
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
                get_model(self.fake_db, 99, lesson_id=653, auth_user=99)


    def test__should_call_execSql_return_no_items(self):
        # arrange
        expected_result = []

        with patch.object(ExecHelper, 'execSql', return_value=expected_result):
            # act

            actual_results = get_model(self.fake_db, 99, lesson_id=89, auth_user=99)
            
            # assert

            ExecHelper.execSql.assert_called_with(self.fake_db,
                "SELECT pln.id as id, pln.title as title, pln.description as description, pln.duration_minutes as duration, pln.task_icon,  pln.order_of_delivery_id FROM sow_lesson_plan as pln INNER JOIN sow_lesson as le ON le.id = pln.lesson_id WHERE pln.id = 99 AND le.id = 89;"
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

            actual_results = get_model(self.fake_db, 23, lesson_id=22, auth_user=99)

            # assert

            ExecHelper.execSql.assert_called_with(self.fake_db,
                "SELECT pln.id as id, pln.title as title, pln.description as description, pln.duration_minutes as duration, pln.task_icon,  pln.order_of_delivery_id FROM sow_lesson_plan as pln INNER JOIN sow_lesson as le ON le.id = pln.lesson_id WHERE pln.id = 23 AND le.id = 22;"
                , []
                , log_info=handle_log_info)
        

            self.assertEqual(23, actual_results.id)
            self.assertEqual("Starter Activity", actual_results.title),
            self.assertEqual("Sort the shapes", actual_results.description),
            self.assertEqual(5, actual_results.duration)
            self.assertEqual("fa-timer", actual_results.task_icon)
            





