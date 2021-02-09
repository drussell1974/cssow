from unittest import TestCase, skip
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.cls_lesson import LessonModel as Model, handle_log_info
from shared.models.cls_learningobjective import LearningObjectiveModel
from shared.models.cls_resource import ResourceModel
from shared.models.cls_department import DepartmentModel
from shared.models.cls_teacher import TeacherModel

@patch("shared.models.cls_teacher.TeacherModel", return_value=TeacherModel(6079, "Dave Russell", department=DepartmentModel(67, "Computer Science")))
class test_db__get_by_keyword(TestCase):


    def setUp(self):
        ' fake database context '
        self.fake_db = Mock()
        self.fake_db.cursor = MagicMock()

    def tearDown(self):
        self.fake_db.close()


    def test__should_call_select__with_exception(self, mock_auth_user):
        # arrange
        expected_exception = KeyError("Bang!")

        with patch.object(ExecHelper, 'select', side_effect=expected_exception):
            # act and assert

            with self.assertRaises(Exception):
                Model.get_by_keyword(self.fake_db, 999, 99, 6079)


    def test__should_call_select__return_no_items(self, mock_auth_user):
        # arrange
        expected_result = []

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act
            
            rows = Model.get_by_keyword(self.fake_db, 222, 13, mock_auth_user)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                'lesson__get_by_keyword'
                , (222, 13, mock_auth_user.id) 
                , []
                , handle_log_info)
                
            self.assertEqual(0, len(rows))


    def test__should_call_select__return_single_item(self, mock_auth_user):
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

            actual_results = Model.get_by_keyword(self.fake_db, 223, 13, mock_auth_user)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                'lesson__get_by_keyword'
                , (223, 13, mock_auth_user.id) 
                , []
                , handle_log_info)
                

            self.assertEqual(1, len(actual_results))

            self.assertEqual(321, actual_results[0].id)
            self.assertEqual("Understanding numbering systems", actual_results[0].title),
            self.assertEqual(2, actual_results[0].topic_id),
            self.assertEqual("Denary", actual_results[0].topic_name),
            self.assertEqual(3, actual_results[0].parent_topic_id),
            self.assertEqual("Data representation", actual_results[0].parent_topic_name),
            self.assertEqual("Understand common numbering systems", actual_results[0].summary)
            
            #Model.get_all_keywords.assert_not_called()        
            LearningObjectiveModel.get_all.assert_not_called()
            ResourceModel.get_number_of_resources.assert_not_called()
            Model.get_related_topic_ids.assert_not_called()
            Model.get_ks123_pathway_objective_ids.assert_not_called()
            Model.get_number_of_learning_objectives.assert_not_called()


    def test__should_call_select__return_multiple_item(self, mock_auth_user):
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

            actual_results = Model.get_by_keyword(self.fake_db, 224, 13, mock_auth_user)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                'lesson__get_by_keyword'
                , (224, 13, mock_auth_user.id)
                , []
                , handle_log_info)

            
            self.assertEqual(3, len(actual_results))


            self.assertEqual(321, actual_results[0].id)
            self.assertEqual("Understanding numbering systems", actual_results[0].title),
            self.assertEqual(2, actual_results[0].topic_id),
            self.assertEqual("Binary", actual_results[0].topic_name),
            self.assertEqual(3, actual_results[0].parent_topic_id),
            self.assertEqual("Data representation", actual_results[0].parent_topic_name),
            self.assertEqual("Understand binary representation in computer systems", actual_results[0].summary)

            
            self.assertEqual(323, actual_results[2].id)
            self.assertEqual("Understanding numbering systems", actual_results[2].title),
            self.assertEqual(2, actual_results[2].topic_id),
            self.assertEqual("Hexadecimal", actual_results[2].topic_name),
            self.assertEqual(3, actual_results[2].parent_topic_id),
            self.assertEqual("Data representation", actual_results[2].parent_topic_name),
            self.assertEqual("Understand hexadecimal representation in computer systems", actual_results[2].summary)

            # THESE ARE NOT CALLED BY DEFAULT unless parent_only = False

            LearningObjectiveModel.get_all.assert_not_called()
            ResourceModel.get_number_of_resources.assert_not_called()
            Model.get_related_topic_ids.assert_not_called()
            Model.get_ks123_pathway_objective_ids.assert_not_called()
            Model.get_number_of_learning_objectives.assert_not_called()


    def test__should_call_select__when_parent_only_is_false(self, mock_auth_user):
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

            actual_results = Model.get_by_keyword(self.fake_db, 223, 13, mock_auth_user, parent_only = False)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                'lesson__get_by_keyword'
                , (223, 13, mock_auth_user.id) 
                , []
                , handle_log_info)
                

            self.assertEqual(1, len(actual_results))

            self.assertEqual(321, actual_results[0].id)
            self.assertEqual("Understanding numbering systems", actual_results[0].title),
            self.assertEqual(2, actual_results[0].topic_id),
            self.assertEqual("Denary", actual_results[0].topic_name),
            self.assertEqual(3, actual_results[0].parent_topic_id),
            self.assertEqual("Data representation", actual_results[0].parent_topic_name),
            self.assertEqual("Understand common numbering systems", actual_results[0].summary)
            Model.get_all_keywords.assert_called()        
            self.assertEqual({32: 'Central Processing Unit (CPU)', 17: 'Control Unit (CU)', 7: 'Registers'}, actual_results[0].key_words)

            LearningObjectiveModel.get_all.assert_called()
            ResourceModel.get_number_of_resources.assert_called()
            Model.get_related_topic_ids.assert_called()
            Model.get_ks123_pathway_objective_ids.assert_called()
            Model.get_number_of_learning_objectives.assert_called()

