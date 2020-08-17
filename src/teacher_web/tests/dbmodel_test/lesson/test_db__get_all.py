from unittest import TestCase, skip
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper

from shared.models.cls_lesson import LessonModel, handle_log_info 
from shared.models.cls_learningobjective import LearningObjectiveModel
from shared.models.cls_resource import ResourceModel

get_all = LessonModel.get_all

class test_db__get_all(TestCase):


    def setUp(self):
        ' fake database context '
        self.fake_db = Mock()
        self.fake_db.cursor = MagicMock()
        
        mockLO = Mock()
        mockLO.id = 23
        mockLO.description = "Objective 1"
        LearningObjectiveModel.get_all = Mock(return_value=[
            mockLO, 
            mockLO])

        LessonModel.get_all_keywords = Mock(return_value={32: 'Central Processing Unit (CPU)', 17: 'Control Unit (CU)', 7: 'Registers'})

        ResourceModel.get_number_of_resources = Mock(return_value=6)

        LessonModel.get_related_topic_ids = Mock(return_value=[
            {"id":56, "name":"Hardware", "checked":None, "disabled":False},
            {"id":57, "name":"Software", "checked":True, "disabled":False}
        ])

        LessonModel.get_ks123_pathway_objective_ids = MagicMock()

        LessonModel.get_number_of_learning_objectives = Mock(return_value=3)


    def tearDown(self):

        LessonModel.get_ks123_pathway_objective_ids.reset_mock()
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

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act
            
            rows = get_all(self.fake_db, 5, auth_user=1)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                'lesson__get_all'
                , (5, 1)
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
            34,
            "Unistructural",
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

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act

            actual_results = get_all(self.fake_db, 3, auth_user=1)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                'lesson__get_all'
                , (3, 1)
                , []
                , log_info=handle_log_info)

            self.assertEqual(1, len(actual_results))

            self.assertEqual(321, actual_results[0]["id"])
            self.assertEqual("Understanding numbering systems", actual_results[0]["title"]),
            self.assertEqual(2, actual_results[0]["topic_id"]),
            self.assertEqual("Denary", actual_results[0]["topic_name"]),
            self.assertEqual(3, actual_results[0]["parent_topic_id"]),
            self.assertEqual("Data representation", actual_results[0]["parent_topic_name"]),
            self.assertEqual("Understand common numbering systems", actual_results[0]["summary"])
            LessonModel.get_all_keywords.assert_called()        
            self.assertEqual({32: 'Central Processing Unit (CPU)', 17: 'Control Unit (CU)', 7: 'Registers'}, actual_results[0]["key_words"])

            LearningObjectiveModel.get_all.assert_called()
            ResourceModel.get_number_of_resources.assert_called()
            LessonModel.get_related_topic_ids.assert_called()
            LessonModel.get_ks123_pathway_objective_ids.assert_called()
            LessonModel.get_number_of_learning_objectives.assert_called()


    def test__should_call_execSql_return_multiple_item(self):
        # arrange
        expected_result = [(321, "Understanding numbering systems",1,5,"Computer Science",
            35, "Multistructural",
            2,"Binary",
            3,"Data representation",
            38,
            10,"Yr10","Understand binary representation in computer systems",
            "2020-07-16 01:04:59",1,"test_user",0,"Denary,Binary,Hexadecimal,Number Systems",
            4,"learning_objectives",23,343
        ),
        (322, "Understanding numbering systems",1,5,"Computer Science",
            35, "Multistructural",
            2,"Denary",
            3,"Data representation",
            38,
            10,"Yr10","Understand common numbering systems",
            "2020-07-16 01:04:59",1,"test_user",0,"Denary,Binary,Hexadecimal",
            4,"learning_objectives",23,343
        ),
        (323, "Understanding numbering systems",1,5,"Computer Science", 
            34, "Unistructural",
            2,"Hexadecimal",
            3,"Data representation",
            38,
            10,"Yr10","Understand hexadecimal representation in computer systems",
            "2020-07-16 01:04:59",1,"test_user",0,"Denary,Binary,Hexadecimal",
            4,"learning_objectives",23,343
        )]

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act

            actual_results = get_all(self.fake_db, 3, auth_user=1)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                 'lesson__get_all'
                 , (3, 1)
                 , []
                 , log_info=handle_log_info)



            LearningObjectiveModel.get_all.assert_called()
            ResourceModel.get_number_of_resources.assert_called()
            LessonModel.get_related_topic_ids.assert_called()
            LessonModel.get_ks123_pathway_objective_ids.assert_called()
            LessonModel.get_number_of_learning_objectives.assert_called()
            
            self.assertEqual(3, len(actual_results))


            self.assertEqual(321, actual_results[0]["id"])
            self.assertEqual("Understanding numbering systems", actual_results[0]["title"]),
            self.assertEqual(2, actual_results[0]["topic_id"]),
            self.assertEqual("Binary", actual_results[0]["topic_name"]),
            self.assertEqual(3, actual_results[0]["parent_topic_id"]),
            self.assertEqual("Data representation", actual_results[0]["parent_topic_name"]),
            self.assertEqual("Understand binary representation in computer systems", actual_results[0]["summary"])

            
            self.assertEqual(323, actual_results[2]["id"])
            self.assertEqual("Understanding numbering systems", actual_results[2]["title"]),
            self.assertEqual(2, actual_results[2]["topic_id"]),
            self.assertEqual("Hexadecimal", actual_results[2]["topic_name"]),
            self.assertEqual(3, actual_results[2]["parent_topic_id"]),
            self.assertEqual("Data representation", actual_results[2]["parent_topic_name"]),
            self.assertEqual("Understand hexadecimal representation in computer systems", actual_results[2]["summary"])