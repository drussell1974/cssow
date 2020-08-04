from unittest import TestCase, skip
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper

from shared.models.cls_lesson import LessonModel, handle_log_info
get_options = LessonModel.get_options


class test_db__get_options(TestCase):
    
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
                get_options(self.fake_db, 21, auth_user=1)


    def test__should_call_execSql_return_no_items(self):
        # arrange
        expected_result = []

        with patch.object(ExecHelper, 'execSql', return_value=expected_result):
            # act
            
            rows = get_options(self.fake_db, 21, auth_user=1)
            
            # assert

            ExecHelper.execSql.assert_called_with(self.fake_db,
                'SELECT le.id as id, le.title as title, le.order_of_delivery_id as order_of_delivery_id, top.id as topic_id, top.name as name, yr.id as year_id, yr.name as year_name FROM sow_lesson as le INNER JOIN sow_topic as top ON top.id = le.topic_id INNER JOIN sow_year as yr ON yr.id = le.year_id  WHERE le.scheme_of_work_id = 21 AND (le.published = 1 OR le.created_by = 1) ORDER BY le.year_id, le.order_of_delivery_id;'
                , [])
            self.assertEqual(0, len(rows))


    def test__should_call_execSql_return_single_item(self):
        # arrange
        expected_result = [(87, "Praesent tempus facilisis pharetra. Pellentesque.", 1, 92, "Garden Peas", 10,"Yr10")]

        with patch.object(ExecHelper, 'execSql', return_value=expected_result):
            # act

            rows = get_options(self.fake_db, 12, auth_user=1)
            
            # assert

            ExecHelper.execSql.assert_called_with(self.fake_db,
                "SELECT le.id as id, le.title as title, le.order_of_delivery_id as order_of_delivery_id, top.id as topic_id, top.name as name, yr.id as year_id, yr.name as year_name FROM sow_lesson as le INNER JOIN sow_topic as top ON top.id = le.topic_id INNER JOIN sow_year as yr ON yr.id = le.year_id  WHERE le.scheme_of_work_id = 12 AND (le.published = 1 OR le.created_by = 1) ORDER BY le.year_id, le.order_of_delivery_id;"
                , [])

            self.assertEqual(1, len(rows))

            self.assertEqual(87, rows[0].id)
            self.assertEqual("Praesent tempus facilisis pharetra. Pellentesque.", rows[0].title)
            self.assertEqual(1, rows[0].order_of_delivery_id)
            self.assertEqual("Garden Peas", rows[0].topic_name)
            self.assertEqual("Yr10", rows[0].year_name)



    def test__should_call_execSql_return_multiple_item(self):
        # arrange
        expected_result = [
            (834, "Vivamus sodales enim cursus ex.", 1, 95, "Runner Beans", 10,"Yr7"),
            (835, "Praesent tempus facilisis pharetra. Pellentesque.", 2, 96, "Mushrooms", 10,"Yr8"),
            (836, "Praesent vulputate, tortor et accumsan.", 3, 97, "Radish", 10,"Yr9"),
        ]


        with patch.object(ExecHelper, 'execSql', return_value=expected_result):
            # act

            rows = get_options(self.fake_db, 21, auth_user=1)
            
            # assert

            ExecHelper.execSql.assert_called_with(self.fake_db,
                "SELECT le.id as id, le.title as title, le.order_of_delivery_id as order_of_delivery_id, top.id as topic_id, top.name as name, yr.id as year_id, yr.name as year_name FROM sow_lesson as le INNER JOIN sow_topic as top ON top.id = le.topic_id INNER JOIN sow_year as yr ON yr.id = le.year_id  WHERE le.scheme_of_work_id = 21 AND (le.published = 1 OR le.created_by = 1) ORDER BY le.year_id, le.order_of_delivery_id;"
                , [])
            
            self.assertEqual(834, rows[0].id)
            self.assertEqual("Vivamus sodales enim cursus ex.", rows[0].title)
            self.assertEqual(1, rows[0].order_of_delivery_id)
            self.assertEqual("Runner Beans", rows[0].topic_name)
            self.assertEqual("Yr7", rows[0].year_name)

            self.assertEqual(836, rows[2].id)
            self.assertEqual("Praesent vulputate, tortor et accumsan.", rows[2].title)
            self.assertEqual(3, rows[2].order_of_delivery_id)
            self.assertEqual("Radish", rows[2].topic_name)
            self.assertEqual("Yr9", rows[2].year_name)
