#from ._unittest import TestCase, FakeDb
from unittest import TestCase, skip
from unittest.mock import Mock, MagicMock, patch
from unittest import skip
from shared.models.core.db_helper import ExecHelper
from shared.models.cls_learningobjective import LearningObjectiveModel as Model, handle_log_info
from tests.test_helpers.mocks import *

@patch("shared.models.core.django_helper", return_value=fake_ctx_model())
class test_db_learning_objective__get_pathway_objectives(TestCase):
    
    def setUp(self):
        ' fake database context '
        self.fake_db = Mock()
        self.fake_db.cursor = MagicMock()
        handle_log_info = MagicMock()


    def tearDown(self):
        self.fake_db.close()


    def test__should_call_select__with_exception(self, mock_auth_user):
        # arrange
        expected_exception = KeyError("Bang!")

        with patch.object(ExecHelper, 'select', side_effect=expected_exception):
            
            # act and assert
            with self.assertRaises(Exception):
                Model.get_all_pathway_objectives(self.fake_db, key_stage_id = 0, key_words="test1,test2")


    def test__should_call_select__return_no_items(self, mock_auth_user):
        # arrange
        expected_result = []

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act
            test_keywords = ","
            result = Model.get_all_pathway_objectives(self.fake_db, key_stage_id = 0, key_words=test_keywords, auth_user = mock_auth_user)

            # assert
            ExecHelper.select.assert_called_with(self.fake_db,
                'lesson_learning_objective__get_all_pathway_objectives'
                , (0, mock_auth_user.id)
                , []
                , handle_log_info)

            self.assertEqual(0, len(result))


    def test__should_call_select__return_single_item(self, mock_auth_user):
        # arrange
        expected_result = [(1,"understand how to pass this test", 2, "describe, identify", 3, 4,"content here",5,"KS4","mouse,keyboard","Group 1","Dave",6,"today", "abc", "abstraction")]

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act
            
            test_keywords = "algorithm,keyboard"
            result = Model.get_all_pathway_objectives(self.fake_db, key_stage_id = 5, key_words=test_keywords, auth_user = mock_auth_user)

            # assert
            ExecHelper.select.assert_called_with(self.fake_db,
               'lesson_learning_objective__get_all_pathway_objectives'
               , (5, mock_auth_user.id)
               , []
               , handle_log_info)

            self.assertEqual(1, len(result))
            ' first item '
            self.assertEqual(1, result[0]["id"], "first item not as expected")
            self.assertEqual("understand how to pass this test", result[0]["description"])


    def test__should_call_select__return_multiple_items(self, mock_auth_user):
        # arrange
        
        test_keywords = "algorithm,abstract,abstraction"
        
        expected_result = [
            (1,"Give the names of different components for a PC", 2, "describe, identify", 3, 4,"content here",5,"KS4","mouse,algorithm,keyboard","Group 1","Dave",6,"today", "abc", "abstraction"),
            (7,"Describe the purpose of the CPU", 8, "explain, justify", 9, 10,"provide some detail",10,"KS4","abstraction,CPU,RAM","Group 1","Dave",11,"yesterday", "algorithm", "abstraction"),
            (12,"Explain the difference between RISC and CISC and justify reason for using them", 13,"explain,justify", 14, 15,"include higher level questions",16,"KS4","RISC,CISC,abstract","Group 1","Dave",1,"yesterday", "algorithm", "abstraction")
            ]

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act
            result = Model.get_all_pathway_objectives(self.fake_db, key_stage_id = 5, key_words=test_keywords, auth_user = mock_auth_user)

            # assert
            ExecHelper.select.assert_called_with(self.fake_db,
                'lesson_learning_objective__get_all_pathway_objectives'
                , (5, mock_auth_user.id)
                , []
                , handle_log_info)
                
            self.assertEqual(3, len(result))
            ' first item '
            self.assertEqual(1, result[0]["id"], "first item not as expected")
            self.assertEqual("Give the names of different components for a PC", result[0]["description"])
            ' last item '
            self.assertEqual(12, result[2]["id"], "first item not as expected")
            self.assertEqual("Explain the difference between RISC and CISC and justify reason for using them", result[2]["description"])
