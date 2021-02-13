from unittest import TestCase, skip
from unittest.mock import Mock, MagicMock, patch
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
                Model.get_linked_pathway_objectives(self.fake_db, lesson_id = 0)


    def test__should_call_select__return_no_items(self, mock_auth_user):
        # arrange
        expected_result = []

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act
            test_keywords = "algorithms,abstract"
            result = Model.get_linked_pathway_objectives(self.fake_db, lesson_id = 72, auth_user = mock_auth_user)

            # assert
            ExecHelper.select.assert_called_with(self.fake_db,
                'lesson_learning_objective__get_linked_pathway_objectives'
                , (72, mock_auth_user.id)
                , []
                , handle_log_info)

            self.assertEqual(0, len(result))


    def test__should_call_select__return_single_item(self, mock_auth_user):
        # arrange    
        expected_result = [(1, "a", 2, "b", 3, 4, "c" ,5 , "d" ,"e" ,"f" ,"g" ,6 ,"h")]

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            
            # test
            test_keywords = "algorithms,abstract"
            rows = Model.get_linked_pathway_objectives(self.fake_db, lesson_id = 72, auth_user = mock_auth_user)

            # assert
            ExecHelper.select.assert_called_with(self.fake_db, 
                'lesson_learning_objective__get_linked_pathway_objectives'
                , (72, mock_auth_user.id)
                , []
                , handle_log_info)

            self.assertEqual(1, len(rows), "number of linked pathways should 1")
            ' first item '
            self.assertEqual(1, rows[0].id, "first item not as expected")
            self.assertEqual("a", rows[0].description)
         

    def test__should_call_select__return_mutliple_items(self, mock_auth_user):
        # arrange
        expected_result = [(1, "a", 2, "b", 3, 4, "c" ,5 , "d" ,"e" ,"f" ,"g" ,6 ,"h"),
                       (7, "aa", 8, "ab", 9, 10, "ac" ,11 , "ad" ,"ae" ,"af" ,"ag" ,12 ,"ah"),
                        (13, "ba", 14, "bb", 15, 16, "bc" ,17 , "bd" ,"be" ,"bf" ,"bg" ,18 ,"bh")]

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            
            # act
            test_keywords = "algorithms,abstract"
            result = Model.get_linked_pathway_objectives(self.fake_db, lesson_id = 72, auth_user = mock_auth_user)

            # assert
            ExecHelper.select.assert_called_with(self.fake_db,
                'lesson_learning_objective__get_linked_pathway_objectives'
                , (72, mock_auth_user.id)
                , []
                , handle_log_info)

            self.assertEqual(3, len(result), "number of linked pathways should 3")
            ' first item '
            self.assertEqual(1, result[0].id, "first item not as expected")
            self.assertEqual("a", result[0].description)


            self.assertEqual(13, result[2].id, "last item not as expected")
            self.assertEqual("ba", result[2].description)