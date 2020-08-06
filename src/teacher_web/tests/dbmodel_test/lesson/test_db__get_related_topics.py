from unittest import TestCase
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.cls_lesson import LessonModel, handle_log_info 

get_related_topic_ids = LessonModel.get_related_topic_ids


class test_db__get_related_topics(TestCase):

    def setUp(self):
        ' create fake database context '
        self.fake_db = Mock()
        self.fake_db.connect()


    def tearDown(self):
        self.fake_db.close()


    def test__should_call_execSql_with_exception(self):
        # arrange
        expected_exception = KeyError("Bang!")

        with patch.object(ExecHelper, 'execSql', side_effect=expected_exception):
            
            # act and assert
            with self.assertRaises(Exception):
                get_related_topic_ids(self.fake_db, 0, 1)


    def test__should_call_execSql_return_no_items(self):
        # arrange
        expected_result = []

        with patch.object(ExecHelper, "execSql", return_value=expected_result):
            # act

            rows = get_related_topic_ids(self.fake_db, 0, 2)

            # assert
            ExecHelper.execSql.assert_called_with(self.fake_db, 
                ' SELECT top.id as id, top.name as name, letop.topic_id as checked, (SELECT count(topic_id) FROM sow_learning_objective AS lob LEFT JOIN sow_learning_objective__has__lesson AS lole ON lole.learning_objective_id = lob.id WHERE lole.lesson_id = letop.lesson_id and lob.topic_id = top.id) as disabled FROM sow_topic AS top LEFT JOIN sow_lesson__has__topics AS letop ON top.id = letop.topic_id and letop.lesson_id = 0 WHERE top.parent_id = 2;'
                , []
                , handle_log_info)
            self.assertEqual(0, len(rows))


    def test__should_call_execSql_return_single_item(self):
        # arrange
        expected_result = [(2,"Image","x",13)]

        with patch.object(ExecHelper, 'execSql', return_value=expected_result):
            
            # act
            rows = get_related_topic_ids(self.fake_db, 0, 3)

            # assert
            ExecHelper.execSql.assert_called_with(self.fake_db, 
                ' SELECT top.id as id, top.name as name, letop.topic_id as checked, (SELECT count(topic_id) FROM sow_learning_objective AS lob LEFT JOIN sow_learning_objective__has__lesson AS lole ON lole.learning_objective_id = lob.id WHERE lole.lesson_id = letop.lesson_id and lob.topic_id = top.id) as disabled FROM sow_topic AS top LEFT JOIN sow_lesson__has__topics AS letop ON top.id = letop.topic_id and letop.lesson_id = 0 WHERE top.parent_id = 3;'
            , []
            , handle_log_info)

            self.assertEqual(1, len(rows), "number of rows not as expected")
            ' first item '
            self.assertEqual(2, rows[0]["id"], "first item not as expected")
            self.assertEqual("Image", rows[0]["name"])


    def test__should_call_execSql_return_multiple_items(self):
        # arrange
        expected_result = [(58,"Binary","x",24),(2,"Image","x",13),(64,"Sound","x",17)]

        with patch.object(ExecHelper, 'execSql', return_value=expected_result):
            
            # act
            rows = get_related_topic_ids(self.fake_db, 0, 3)
            # assert
            ExecHelper.execSql.assert_called_with(self.fake_db, 
                ' SELECT top.id as id, top.name as name, letop.topic_id as checked, (SELECT count(topic_id) FROM sow_learning_objective AS lob LEFT JOIN sow_learning_objective__has__lesson AS lole ON lole.learning_objective_id = lob.id WHERE lole.lesson_id = letop.lesson_id and lob.topic_id = top.id) as disabled FROM sow_topic AS top LEFT JOIN sow_lesson__has__topics AS letop ON top.id = letop.topic_id and letop.lesson_id = 0 WHERE top.parent_id = 3;'
                , []
                , handle_log_info)

            self.assertEqual(3, len(rows), "number of rows not as expected")
            ' first item '
            self.assertEqual(58, rows[0]["id"], "first item not as expected")
            self.assertEqual("Binary", rows[0]["name"])
            ' last item'
            self.assertEqual(64, rows[2]["id"], "last item not as expected")
            self.assertEqual("Sound", rows[2]["name"])
