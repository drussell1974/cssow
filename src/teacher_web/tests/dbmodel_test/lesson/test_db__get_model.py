from unittest import TestCase, skip
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper

from shared.models.cls_lesson import LessonModel, handle_log_info
from shared.models.cls_learningobjective import LearningObjectiveModel
from shared.models.cls_resource import ResourceModel
from shared.models.cls_keyword import KeywordModel
# test context

get_model = LessonModel.get_model
#handle_log_info = shared.models.cls_lesson.handle_log_info


class test_db__get_model(TestCase):
    

    def setUp(self):
        ' fake database context '
        self.fake_db = Mock()
        self.fake_db.cursor = MagicMock()

        LessonModel.get_all_keywords = Mock(return_value=[
            KeywordModel(32, 'Central Processing Unit (CPU)', ''),
            KeywordModel(17, 'Control Unit (CU)', ''),
            KeywordModel(7, 'Registers', '')
        ])


        LearningObjectiveModel.get_all = MagicMock(return_value=[1,2,3])
        ResourceModel.get_all = MagicMock(return_value=[])
        #LessonModel.get_pathway_objective_ids = MagicMock(return_value=[])
        LessonModel.get_ks123_pathway_objective_ids = MagicMock(return_value=[])


    def tearDown(self):
        
        LearningObjectiveModel.get_all.reset_mock()
        ResourceModel.get_all.reset_mock()
        LessonModel.get_ks123_pathway_objective_ids.reset_mock()

        self.fake_db.close()


    def test__should_call_select__with_exception(self):
        # arrange
        expected_exception = KeyError("Bang!")

        with patch.object(ExecHelper, 'select', side_effect=expected_exception):
            # act and assert

            with self.assertRaises(Exception):
                get_model(self.fake_db, 4)


    def test__should_call_select__return_no_items(self):
        # arrange
        expected_result = []

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act
         
            actual_results = get_model(self.fake_db, 101, scheme_of_work_id=34, auth_user=99)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                "lesson__get"
                , (101,34,99)
                , [])


            LearningObjectiveModel.get_all.assert_not_called()
            ResourceModel.get_all.assert_not_called()
            LessonModel.get_ks123_pathway_objective_ids.assert_not_called()

            self.assertEqual(101, actual_results.id)
            self.assertEqual("", actual_results.title),
            self.assertEqual(0, actual_results.topic_id),
            self.assertEqual("", actual_results.topic_name),
            self.assertEqual(0, actual_results.parent_topic_id),
            self.assertEqual("", actual_results.parent_topic_name),
            self.assertEqual("", actual_results.summary)
            self.assertEqual([], actual_results.key_words)
            self.assertFalse(actual_results.is_from_db)
        

    def test__should_call_select__return_single_item(self):
        # arrange
        expected_result = [(
            321,"Understanding numbering systems",1,5,"Computer Science", 13, "Abstract",
            2,"Denary",3,"Data representation",38,11,"Understand common numbering systems","2020-07-16 01:04:59",
            1,"test_user",0,{32: 'Central Processing Unit (CPU)', 17: 'Control Unit (CU)', 7: 'Registers'},4,"learning_objectives",23,343
        )]
        
        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act

            actual_results = get_model(self.fake_db, 321, scheme_of_work_id=909, auth_user=6079)

            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                "lesson__get"
                , (321,909,6079)
                , [])
            
            LessonModel.get_all_keywords.assert_called_with(self.fake_db, 321, 6079)

            self.assertEqual(3, len(actual_results.key_words))
            
            LearningObjectiveModel.get_all.assert_called()
            ResourceModel.get_all.assert_called()
            LessonModel.get_ks123_pathway_objective_ids.assert_called()

            self.assertEqual(321, actual_results.id)
            self.assertEqual("Understanding numbering systems", actual_results.title),
            self.assertEqual(2, actual_results.topic_id),
            self.assertEqual("Denary", actual_results.topic_name),
            self.assertEqual(3, actual_results.parent_topic_id),
            self.assertEqual("Data representation", actual_results.parent_topic_name),
            self.assertEqual("Understand common numbering systems", actual_results.summary)

            self.assertNotIsInstance(actual_results, dict, "remove __dict__ from actual_results")
            self.assertTrue(actual_results.is_from_db)
        




