from unittest import TestCase, skip
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper

import shared.models.cls_keyword as test_context 

get_by_terms = test_context.KeywordModel.get_by_terms
handle_log_info = test_context.handle_log_info
Model = test_context.KeywordModel

class test_db__get_by_terms(TestCase):


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
                get_by_terms(self.fake_db, 4)


    def test__should_call_select__return_no_items(self):
        # arrange
        expected_result = []

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act
            
            actual_results = get_by_terms(self.fake_db, "", True, 13, 6079)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                'keyword__get_by_term'
                , ('', 13, 6079)
                , []
                , handle_log_info)
                
            self.assertEqual(0, len(actual_results))


    def test__should_call_select___with_empty__key_words_list__and__allow_all__False(self):
        # arrange
        expected_result = []

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act

            actual_results = get_by_terms(self.fake_db, "", False, 13, 6079)
            
            # assert
            
            ExecHelper.select.assert_not_called()
                
            self.assertEqual(0, len(actual_results))


    def test__should_call_select___with_empty__key_words_list__and__allow_all__True(self):
        # arrange
        expected_result = []

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act

            actual_results = get_by_terms(self.fake_db, "", True, 13, 6079)
            
            # assert
            
            ExecHelper.select.assert_called_with(self.fake_db,
                'keyword__get_by_term'
                , ('', 13, 6079)
                , []
                , handle_log_info)
                
            self.assertEqual(0, len(actual_results))
    
    
    def test__should_call_select___with__key_words_list__and__allow_all__True__return_single_item(self):
        # arrange
        expected_result = [(702, "Fringilla", "purus lacus, ut volutpat nibh euismod.", 13)]

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act

            actual_results = get_by_terms(self.fake_db, "", True, 13, 6079)
            
            # assert
            
            ExecHelper.select.assert_called_with(self.fake_db,
                'keyword__get_by_term'
                , ('', 13, 6079)
                , []
                , handle_log_info)
                
            self.assertEqual(1, len(actual_results))

            self.assertEqual(702, actual_results[0].id)
            self.assertEqual("Fringilla", actual_results[0].term),
            self.assertEqual("purus lacus, ut volutpat nibh euismod.", actual_results[0].definition)
            self.assertEqual(13, actual_results[0].scheme_of_work_id)


    def test__should_call_select___with__key_words_list__and__allow_all__True__return_multiple_items(self):
        # arrange
        expected_result = [
            (67, "Vestibulum", "nec arcu nec dolor vehicula ornare non.", 133),
            (68, "Fringilla", "purus lacus, ut volutpat nibh euismod.", 133),
            (69, "Lorem", "rutrum a arcu ultrices, id mollis", 133)
        ]

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act

            actual_results = get_by_terms(self.fake_db, "ullamcorper, dolor, odio", True, 133, 6079)
            
            # assert
            
            ExecHelper.select.assert_called_with(self.fake_db,
                'keyword__get_by_term'
                , ("ullamcorper','dolor','odio", 133, 6079)
                , []
                , handle_log_info)
                
            self.assertEqual(3, len(actual_results))

            self.assertEqual(67, actual_results[0].id)
            self.assertEqual("Vestibulum", actual_results[0].term),
            self.assertEqual("nec arcu nec dolor vehicula ornare non.", actual_results[0].definition)
            self.assertEqual(133, actual_results[0].scheme_of_work_id)


            self.assertEqual(69, actual_results[2].id)
            self.assertEqual("Lorem", actual_results[2].term),
            self.assertEqual("rutrum a arcu ultrices, id mollis", actual_results[2].definition)
            self.assertEqual(133, actual_results[2].scheme_of_work_id)
