from unittest import TestCase
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.cls_schemeofwork import SchemeOfWorkModel, handle_log_info

get_all_keywords = SchemeOfWorkModel.get_all_keywords

class test_db__get_all_keywords(TestCase):
    
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
                get_all_keywords(self.fake_db, 13, 6079)


    def test__should_call_select__return_no_items(self):
        # arrange
        expected_result = []

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act
            
            rows = get_all_keywords(self.fake_db, 12, 6079)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                'scheme_of_work__get_all_keywords'
                , (12, 6079)
                , []
                , handle_log_info)
            self.assertEqual(0, len(rows))


    def test__should_call_select__return_single_item(self):
        # arrange

        with patch.object(ExecHelper, 'select', return_value=[(87,"Fetch Decode Execute", "The process carried out by the CPU", 13, 1, 0)]):
            # act

            actual_results = get_all_keywords(self.fake_db, 13, 6079)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                'scheme_of_work__get_all_keywords'
                , (13, 6079)
                , []
                , handle_log_info)

            self.assertEqual(1, len(actual_results))

            self.assertEqual(87, actual_results[0].id)
            self.assertEqual("Fetch Decode Execute", actual_results[0].term)
            self.assertEqual("The process carried out by the CPU", actual_results[0].definition)


    def test__should_call_select__return_multiple_item(self):
        # arrange

        with patch.object(ExecHelper, 'select', return_value=[(1034,"DDR","", 13, 1, 2),(1045,"DIMM","", 13, 1, 2),(12,"DRAM","", 13, 1, 2) ]):
            # act

            actual_results = get_all_keywords(self.fake_db, 13, 6079)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                'scheme_of_work__get_all_keywords'
                , (13, 6079)
                , []
                , handle_log_info)
            
            self.assertEqual("DDR", actual_results[0].term)
            self.assertEqual("DRAM", actual_results[2].term)
