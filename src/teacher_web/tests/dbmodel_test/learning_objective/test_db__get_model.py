from unittest import TestCase, skip
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper

import shared.models.cls_learningobjective as test_context

# test context

get_model = test_context.LearningObjectiveModel.get_model
handle_log_info = test_context.handle_log_info


class test_db__get_model(TestCase):
    

    def setUp(self):
        ' fake database context '
        self.fake_db = Mock()
        self.fake_db.cursor = MagicMock()


    def tearDown(self):
        self.fake_db.close()


    def test__should_call_select__with_exception(self):
        # arrange
        expected_exception = KeyError("Bang!")

        with patch.object(ExecHelper, 'select', side_effect=expected_exception):
            # act and assert

            with self.assertRaises(Exception):
                actual_result = get_model(self.fake_db, 4)


    def test__should_call_select__return_no_items(self):
        # arrange
        expected_result = []

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act
            
            actual_results = get_model(self.fake_db, 99, lesson_id=34, scheme_of_work_id=34, auth_user=6079)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                "lesson_learning_objective__get"
                , (99,6079)
                , []
                , handle_log_info)

            self.assertEqual(0, actual_results.id)
            self.assertFalse(actual_results.is_from_db)


    def test__should_call_select__return_single_item(self):
        # arrange
        expected_result = [(
            321,"Understanding numbering systems",
            3,"Unistructural", 4, 12,
            "State the different numbering systems", 45,
            3, "KS3",
            "Binary,Denary,Hexadecimal", "Revise the names three different numbering systems",
            "Theory", "2020-07-17 02:12:34", 1, "test_user", 1
        )]
        
        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act

            actual_results = get_model(self.fake_db, 321, lesson_id=77, scheme_of_work_id=89, auth_user=6079)

            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                "lesson_learning_objective__get"
                , (321,6079)
                , []
                , handle_log_info)
            

            self.assertEqual(321, actual_results.id)
            self.assertEqual("Understanding numbering systems", actual_results.description)
            self.assertEqual("Unistructural", actual_results.solo_taxonomy_name)
            self.assertEqual("State the different numbering systems", actual_results.content_description)
            self.assertEqual("Binary,Denary,Hexadecimal", actual_results.key_words)
            self.assertEqual("Revise the names three different numbering systems", actual_results.notes)
            self.assertTrue(actual_results.is_from_db)


