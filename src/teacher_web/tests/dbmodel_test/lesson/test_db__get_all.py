from unittest import TestCase, skip
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.cls_lesson import LessonModel, LessonFilter,  handle_log_info 
from shared.models.cls_lesson_schedule import LessonScheduleModel
from shared.models.cls_learningobjective import LearningObjectiveModel
from shared.models.cls_resource import ResourceModel
from shared.models.enums.publlished import STATE
from tests.test_helpers.mocks import *

@patch.object(LessonModel, "get_number_of_learning_objectives", return_value=3)
@patch.object(LessonModel, "get_ks123_pathway_objective_ids", return_value=[])
@patch.object(LessonModel, "get_related_topic_ids", return_value=[{"id":56, "name":"Hardware", "checked":None, "disabled":False},{"id":57, "name":"Software", "checked":True, "disabled":False}])
@patch.object(LessonModel, "get_all_keywords", return_value={32: 'Central Processing Unit (CPU)', 17: 'Control Unit (CU)', 7: 'Registers'})
@patch.object(ResourceModel, "get_number_of_resources", return_value=6)
@patch.object(LearningObjectiveModel, "get_all", return_value=[LearningObjectiveModel(23,"Objective 1")])
@patch.object(LessonScheduleModel, "get_all", return_value=[])
@patch("shared.models.core.django_helper", return_value=fake_ctx_model())
class test_db__get_all(TestCase):


    def setUp(self):
        ' fake database context '
        self.fake_db = Mock()
        self.fake_db.cursor = MagicMock()
        
        self.search_criteria = LessonFilter("", [5, 10, 25, 50, 2])


    def tearDown(self):

        self.fake_db.close()


    def test__should_call_select__with_exception(self, mock_auth_user, 
            LessonScheduleModel_get_all,
            LearningObjectiveModel_get_all,
            ResourceModel_get_number_of_resources,
            LessonModel_get_all_keywords,
            LessonModel_get_related_topic_ids,
            LessonModel_get_ks123_pathway_objective_ids,
            LessonModel_get_number_of_learning_objectives):

        # arrange
        expected_exception = KeyError("Bang!")

        with patch.object(ExecHelper, 'select', side_effect=expected_exception):
            # act and assert

            with self.assertRaises(KeyError):
                LessonModel.get_all(self.fake_db, int(STATE.PUBLISH), mock_auth_user)


    def test__should_call_select__return_no_items(self, mock_auth_user, 
            LessonScheduleModel_get_all,
            LearningObjectiveModel_get_all,
            ResourceModel_get_number_of_resources,
            LessonModel_get_all_keywords,
            LessonModel_get_related_topic_ids,
            LessonModel_get_ks123_pathway_objective_ids,
            LessonModel_get_number_of_learning_objectives):

        # arrange
        expected_result = []

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act
            
            rows = LessonModel.get_all(self.fake_db, 5, auth_user=mock_auth_user)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                'lesson__get_all$2'
                , (5, int(STATE.PUBLISH), mock_auth_user.auth_user_id)
                , []
                , handle_log_info)
                
            self.assertEqual(0, len(rows))


    def test__should_call_select__return_single_item(self, mock_auth_user, 
            LessonScheduleModel_get_all,
            LearningObjectiveModel_get_all,
            ResourceModel_get_number_of_resources,
            LessonModel_get_all_keywords,
            LessonModel_get_related_topic_ids,
            LessonModel_get_ks123_pathway_objective_ids,
            LessonModel_get_number_of_learning_objectives):

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
            343,
            "7x",
            "ABCDEF"
        )]

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act

            actual_results = LessonModel.get_all(self.fake_db, 3, auth_user=fake_ctx_model())
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                'lesson__get_all$2'
                , (3, int(STATE.PUBLISH_INTERNAL), 6079)
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
            #self.assertEqual("", actual_results[0]["class_name"])
            #self.assertEqual("", actual_results[0]["class_code"])
            LessonModel.get_all_keywords.assert_called()        
            self.assertEqual({32: 'Central Processing Unit (CPU)', 17: 'Control Unit (CU)', 7: 'Registers'}, actual_results[0]["key_words"])

            LessonScheduleModel.get_all.assert_called()
            LearningObjectiveModel.get_all.assert_called()
            ResourceModel.get_number_of_resources.assert_called()
            LessonModel.get_related_topic_ids.assert_called()
            LessonModel.get_ks123_pathway_objective_ids.assert_called()
            LessonModel.get_number_of_learning_objectives.assert_called()


    def test__should_call_select__return_multiple_item(self, mock_auth_user, 
            LessonScheduleModel_get_all,
            LearningObjectiveModel_get_all,
            ResourceModel_get_number_of_resources,
            LessonModel_get_all_keywords,
            LessonModel_get_related_topic_ids,
            LessonModel_get_ks123_pathway_objective_ids,
            LessonModel_get_number_of_learning_objectives):

        # arrange
        expected_result = [(321, "Understanding numbering systems",1,5,"Computer Science",
            35, "Multistructural",
            2,"Binary",
            3,"Data representation",
            38,
            10,"Yr10","Understand binary representation in computer systems",
            "2020-07-16 01:04:59",1,"test_user",0,"Denary,Binary,Hexadecimal,Number Systems",
            4,"learning_objectives",23,343,
            "7x",
            "ABCDEF"
        ),
        (322, "Understanding numbering systems",1,5,"Computer Science",
            35, "Multistructural",
            2,"Denary",
            3,"Data representation",
            38,
            10,"Yr10","Understand common numbering systems",
            "2020-07-16 01:04:59",1,"test_user",0,"Denary,Binary,Hexadecimal",
            4,"learning_objectives",23,343,
            "7x",
            "ABCDEG"
        ),
        (323, "Understanding numbering systems",1,5,"Computer Science", 
            34, "Unistructural",
            2,"Hexadecimal",
            3,"Data representation",
            38,
            10,"Yr10","Understand hexadecimal representation in computer systems",
            "2020-07-16 01:04:59",1,"test_user",0,"Denary,Binary,Hexadecimal",
            4,"learning_objectives",23,343,
            "7x",
            "ABCDEH"
        )]

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act

            actual_results = LessonModel.get_all(self.fake_db, 3, auth_user=mock_auth_user)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                 'lesson__get_all$2'
                 , (3, int(STATE.PUBLISH), mock_auth_user.auth_user_id)
                 , []
                 , handle_log_info)



            LessonScheduleModel.get_all.assert_called()
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
            #self.assertEqual("", actual_results[0]["class_name"])
            #self.assertEqual("", actual_results[0]["summary"])

            
            self.assertEqual(323, actual_results[2]["id"])
            self.assertEqual("Understanding numbering systems", actual_results[2]["title"]),
            self.assertEqual(2, actual_results[2]["topic_id"]),
            self.assertEqual("Hexadecimal", actual_results[2]["topic_name"]),
            self.assertEqual(3, actual_results[2]["parent_topic_id"]),
            self.assertEqual("Data representation", actual_results[2]["parent_topic_name"]),
            self.assertEqual("Understand hexadecimal representation in computer systems", actual_results[2]["summary"])
            #self.assertEqual("", actual_results[2]["class_name"])
            #self.assertEqual("", actual_results[2]["class_code"])