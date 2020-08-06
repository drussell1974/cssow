from unittest import TestCase, skip
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper

from shared.models.cls_lessonplan import LessonPlanDataAccess, handle_log_info

get_all = LessonPlanDataAccess.get_all

@skip("Deprecated. No longer used.")
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

            with self.assertRaises(KeyError):
                get_all(self.fake_db, lesson_id=3, auth_user=99)


    def test__should_call_execSql_return_no_items(self):
        # arrange
        expected_result = []

        with patch.object(ExecHelper, 'execSql', return_value=expected_result):
            # act
            
            actual_results = get_all(self.fake_db, lesson_id=343, auth_user=99)
            
            # assert

            ExecHelper.execSql.assert_called_with(self.fake_db,
                "SELECT pln.id as id, pln.title as title, pln.description as description, pln.duration_minutes as duration, pln.task_icon,  pln.order_of_delivery_id FROM sow_lesson_plan as pln INNER JOIN sow_lesson as le ON le.id = pln.lesson_id WHERE le.id = 343 ORDER BY pln.order_of_delivery_id;"
                , []
                , log_info=handle_log_info)
                
            self.assertEqual(0, len(actual_results[0])) # data_part
            self.assertEqual(0, actual_results[1]) # duration_h
            self.assertEqual(0, actual_results[2]) # duration_m 


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
            # acts

            actual_results = get_all(self.fake_db, lesson_id=31, auth_user=99)
            
            # assert

            ExecHelper.execSql.assert_called_with(self.fake_db,
                "SELECT pln.id as id, pln.title as title, pln.description as description, pln.duration_minutes as duration, pln.task_icon,  pln.order_of_delivery_id FROM sow_lesson_plan as pln INNER JOIN sow_lesson as le ON le.id = pln.lesson_id WHERE le.id = 31 ORDER BY pln.order_of_delivery_id;"
                , []
                , log_info=handle_log_info)

            data_part= actual_results[0]
            duration_h = actual_results[1]
            duration_m = actual_results[2]

            self.assertEqual(1, len(data_part))
            self.assertEqual(0.08333333333333333, duration_h) # duration_h
            self.assertEqual(5, duration_m) # duration_m 

            self.assertEqual(23, data_part[0].id)
            self.assertEqual("Starter Activity", data_part[0].title),
            self.assertEqual("Sort the shapes", data_part[0].description),
            self.assertEqual(5, data_part[0].duration)


    def test__should_call_execSql_return_multiple_item(self):
        # arrange
        expected_result = [(
            23,                     # " pln.id as id," \
            "Starter Activity",     # " pln.title as title," \
            "Sort the shapes",      # " pln.description as description," \
            5,                      # " pln.duration_minutes as duration," \
            "fa-timer",             #" pln.task_icon, " \
            1                       #" pln.order_of_delivery_id "\
        ),
        (
            24,                     # " pln.id as id," \
            "Introduction",     # " pln.title as title," \
            "Make notes",      # " pln.description as description," \
            10,                      # " pln.duration_minutes as duration," \
            "fa-pen",             #" pln.task_icon, " \
            2                       #" pln.order_of_delivery_id "\
        ),
        (
            25,                     # " pln.id as id," \
            "Worksheet",     # " pln.title as title," \
            "Complete the questions",      # " pln.description as description," \
            15,                      # " pln.duration_minutes as duration," \
            "fa-question",             #" pln.task_icon, " \
            3                      #" pln.order_of_delivery_id "\
        )]

        with patch.object(ExecHelper, 'execSql', return_value=expected_result):
            # act

            actual_results = get_all(self.fake_db, lesson_id=87, auth_user=99)
            
            # assert

            ExecHelper.execSql.assert_called_with(self.fake_db,
                "SELECT pln.id as id, pln.title as title, pln.description as description, pln.duration_minutes as duration, pln.task_icon,  pln.order_of_delivery_id FROM sow_lesson_plan as pln INNER JOIN sow_lesson as le ON le.id = pln.lesson_id WHERE le.id = 87 ORDER BY pln.order_of_delivery_id;"
                , []
                , log_info=handle_log_info)

            self.assertEqual(3, len(actual_results))

            data_part= actual_results[0]
            duration_h = actual_results[1]
            duration_m = actual_results[2]

            self.assertEqual(3, len(data_part))

            self.assertEqual(0.5, duration_h) # duration_h
            self.assertEqual(30, duration_m) # duration_m 

            self.assertEqual(23, data_part[0].id)
            self.assertEqual("Starter Activity", data_part[0].title),
            self.assertEqual("Sort the shapes", data_part[0].description),
            self.assertEqual(5, data_part[0].duration)

            self.assertEqual(25, data_part[2].id)
            self.assertEqual("Worksheet", data_part[2].title),
            self.assertEqual("Complete the questions", data_part[2].description),
            self.assertEqual(15, data_part[2].duration)
