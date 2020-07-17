from unittest import TestCase, skip
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper

import shared.models.cls_lesson as cls_lesson 

get_all = cls_lesson.get_all
handle_log_info = cls_lesson.handle_log_info

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
                get_all(self.fake_db, 4)


    def test__should_call_execSql_return_no_items(self):
        # arrange
        expected_result = []

        with patch.object(ExecHelper, 'execSql', return_value=expected_result):
            # act
            
            rows = get_all(self.fake_db, 5, auth_user=1)
            
            # assert

            ExecHelper.execSql.assert_called_with(self.fake_db,
                "SELECT  le.id as id, le.title as title, le.order_of_delivery_id as order_of_delivery_id, le.scheme_of_work_id as scheme_of_work_id, sow.name as scheme_of_work_name, top.id as topic_id, top.name as topic_name, pnt_top.id as parent_topic_id, pnt_top.name as parent_topic_name, sow.key_stage_id as key_stage_id, yr.id as year_id, yr.name as year_name, le.summary as summary, le.created as created, le.created_by as created_by_id, CONCAT_WS(' ', user.first_name, user.last_name) as created_by_name, le.published as published FROM sow_lesson as le  INNER JOIN sow_scheme_of_work as sow ON sow.id = le.scheme_of_work_id INNER JOIN sow_year as yr ON yr.id = le.year_id LEFT JOIN sow_topic as top ON top.id = le.topic_id  LEFT JOIN sow_topic as pnt_top ON pnt_top.id = top.parent_id  LEFT JOIN auth_user as user ON user.id = sow.created_by  WHERE le.scheme_of_work_id = 5 AND (le.published = 1 OR le.created_by = 1) ORDER BY le.year_id, le.order_of_delivery_id;"
                , []
                , log_info=handle_log_info)
                
            self.assertEqual(0, len(rows))


    def test__should_call_execSql_return_single_item(self):
        # arrange
        expected_result = [(
            321, 
            "Understanding numbering systems",
            1,
            5,
            "Computer Science",
            2,
            "Denary",
            3,
            "Data representation",
            38,
            11,
            "Yr10",
            "Understand common numbering systems",
            "2020-07-16 01:04:59",
            1,
            "test_user",
            0,
            "Denary,Binary,Hexadecimal",
            4,
            "learning_objectives",
            23,
            343
        )]

        with patch.object(ExecHelper, 'execSql', return_value=expected_result):
            # act

            actual_results = get_all(self.fake_db, 3, auth_user=1)
            
            # assert

            ExecHelper.execSql.assert_called_with(self.fake_db,
                " SELECT top.id as id, top.name as name, letop.topic_id as checked, (SELECT count(topic_id) FROM sow_learning_objective AS lob LEFT JOIN sow_learning_objective__has__lesson AS lole ON lole.learning_objective_id = lob.id WHERE lole.lesson_id = letop.lesson_id and lob.topic_id = top.id) as disabled FROM sow_topic AS top LEFT JOIN sow_lesson__has__topics AS letop ON top.id = letop.topic_id and letop.lesson_id = 321 WHERE top.parent_id = 2;"
                , []
                , handle_log_info)

            self.assertEqual(1, len(actual_results))

            self.assertEqual(321, actual_results[0]["id"])
            self.assertEqual("Understanding numbering systems", actual_results[0]["title"]),
            self.assertEqual(2, actual_results[0]["topic_id"]),
            self.assertEqual("Denary", actual_results[0]["topic_name"]),
            self.assertEqual(3, actual_results[0]["parent_topic_id"]),
            self.assertEqual("Data representation", actual_results[0]["parent_topic_name"]),
            self.assertEqual("Understand common numbering systems", actual_results[0]["summary"])
            self.assertEqual({}, actual_results[0]["key_words"])


    def test__should_call_execSql_return_multiple_item(self):
        # arrange
        expected_result = [(321, "Understanding numbering systems",1,5,"Computer Science",
            2,"Binary",3,"Data representation",38,
            10,"Yr10","Understand binary representation in computer systems",
            "2020-07-16 01:04:59",1,"test_user",0,"Denary,Binary,Hexadecimal,Number Systems",
            4,"learning_objectives",23,343
        ),
        (322, "Understanding numbering systems",1,5,"Computer Science",
            2,"Denary",3,"Data representation",38,
            10,"Yr10","Understand common numbering systems",
            "2020-07-16 01:04:59",1,"test_user",0,"Denary,Binary,Hexadecimal",
            4,"learning_objectives",23,343
        ),
        (323, "Understanding numbering systems",1,5,"Computer Science",
            2,"Hexadecimal",3,"Data representation",38,
            10,"Yr10","Understand hexadecimal representation in computer systems",
            "2020-07-16 01:04:59",1,"test_user",0,"Denary,Binary,Hexadecimal",
            4,"learning_objectives",23,343
        )]

        with patch.object(ExecHelper, 'execSql', return_value=expected_result):
            # act

            actual_results = get_all(self.fake_db, 3, auth_user=1)
            
            # assert

            ExecHelper.execSql.assert_called_with(self.fake_db,
                 ' SELECT top.id as id, top.name as name, letop.topic_id as checked, (SELECT count(topic_id) FROM sow_learning_objective AS lob LEFT JOIN sow_learning_objective__has__lesson AS lole ON lole.learning_objective_id = lob.id WHERE lole.lesson_id = letop.lesson_id and lob.topic_id = top.id) as disabled FROM sow_topic AS top LEFT JOIN sow_lesson__has__topics AS letop ON top.id = letop.topic_id and letop.lesson_id = 323 WHERE top.parent_id = 2;'
                 , []
                 , handle_log_info)

            self.assertEqual(3, len(actual_results))


            self.assertEqual(321, actual_results[0]["id"])
            self.assertEqual("Understanding numbering systems", actual_results[0]["title"]),
            self.assertEqual(2, actual_results[0]["topic_id"]),
            self.assertEqual("Binary", actual_results[0]["topic_name"]),
            self.assertEqual(3, actual_results[0]["parent_topic_id"]),
            self.assertEqual("Data representation", actual_results[0]["parent_topic_name"]),
            self.assertEqual("Understand binary representation in computer systems", actual_results[0]["summary"])
            self.assertEqual({}, actual_results[0]["key_words"])

            
            self.assertEqual(323, actual_results[2]["id"])
            self.assertEqual("Understanding numbering systems", actual_results[2]["title"]),
            self.assertEqual(2, actual_results[2]["topic_id"]),
            self.assertEqual("Hexadecimal", actual_results[2]["topic_name"]),
            self.assertEqual(3, actual_results[2]["parent_topic_id"]),
            self.assertEqual("Data representation", actual_results[2]["parent_topic_name"]),
            self.assertEqual("Understand hexadecimal representation in computer systems", actual_results[2]["summary"])
            self.assertEqual({}, actual_results[2]["key_words"])