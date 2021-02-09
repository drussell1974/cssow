from unittest import TestCase, skip
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper

from shared.models.cls_lesson import LessonModel, handle_log_info
from shared.models.cls_learningobjective import LearningObjectiveModel
from shared.models.cls_resource import ResourceModel
from shared.models.cls_keyword import KeywordModel
from shared.models.cls_department import DepartmentModel
from shared.models.cls_teacher import TeacherModel

@patch("shared.models.cls_teacher.TeacherModel", return_value=TeacherModel(6079, "Dave Russell", department=DepartmentModel(67, "Computer Science")))
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


    def test__should_call_select__with_exception(self, mock_auth_user):
        # arrange
        expected_exception = KeyError("Bang!")

        with patch.object(ExecHelper, 'select', side_effect=expected_exception):
            # act and assert

            with self.assertRaises(Exception):
                LessonModel.get_model(self.fake_db, 4)


    def test__should_call_select__return_no_items(self, mock_auth_user):
        # arrange
        expected_result = []

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act
         
            actual_results = LessonModel.get_model(self.fake_db, 101, scheme_of_work_id=34, auth_user=mock_auth_user)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                "lesson__get"
                , (101,34,mock_auth_user.id)
                , []
                , handle_log_info)


            LearningObjectiveModel.get_all.assert_not_called()
            ResourceModel.get_all.assert_not_called()
            LessonModel.get_ks123_pathway_objective_ids.assert_not_called()

            self.assertIsNone(actual_results)        


    def test__should_call_select__return_single_item(self, mock_auth_user):
        # arrange
        expected_result = [(
            321,"Understanding numbering systems",1,5,"Computer Science", 13, "Abstract",
            2,"Denary",3,"Data representation",38,11,"Understand common numbering systems","2020-07-16 01:04:59",
            1,"test_user",0,{32: 'Central Processing Unit (CPU)', 17: 'Control Unit (CU)', 7: 'Registers'},4,"learning_objectives",23,343
        )]
        
        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act

            actual_results = LessonModel.get_model(self.fake_db, 321, scheme_of_work_id=909, auth_user=mock_auth_user)

            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                "lesson__get"
                , (321,909,mock_auth_user.id)
                , []
                , handle_log_info)
            
            LessonModel.get_all_keywords.assert_called_with(self.fake_db, 321, mock_auth_user)

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
        




