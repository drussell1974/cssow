from unittest import TestCase
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.cls_schemeofwork import SchemeOfWorkModel, handle_log_info
from tests.test_helpers.mocks import *

#TODO: #329 remove global reference
get_all_keywords = SchemeOfWorkModel.get_all_keywords


@patch("shared.models.core.django_helper", return_value=fake_ctx_model())
class test_db__get_all_keywords(TestCase):
    
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
                get_all_keywords(self.fake_db, 13, 6079)


    def test__should_call_select__return_no_items(self, mock_auth_user):
        # arrange
        expected_result = []

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act
            
            rows = get_all_keywords(self.fake_db, 12, mock_auth_user)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                'scheme_of_work__get_all_keywords'
                , (12, mock_auth_user.user_id)
                , []
                , handle_log_info)
            self.assertEqual(0, len(rows))


    def test__should_call_select__return_single_item(self, mock_auth_user):
        # arrange

        with patch.object(ExecHelper, 'select', return_value=[(87,"Fetch Decode Execute", "The process carried out by the CPU", 13, 1, '2020-01-24 07:26')]):
            # act

            actual_results = get_all_keywords(self.fake_db, 13, mock_auth_user)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                'scheme_of_work__get_all_keywords'
                , (13, mock_auth_user.user_id)
                , []
                , handle_log_info)

            self.assertEqual(1, len(actual_results))

            self.assertEqual(87, actual_results[0].id)
            self.assertEqual("Fetch Decode Execute", actual_results[0].term)
            self.assertEqual("The process carried out by the CPU", actual_results[0].definition)


    def test__should_call_select__return_multiple_item(self, mock_auth_user):
        # arrange

        with patch.object(ExecHelper, 'select', return_value=[
                    (1034,"DDR","", 13, 1, 2, '2020-01-24 07:27:01'),
                    (1045,"DIMM","", 13, 1, 2, '2020-01-24 07:27:02'),
                    (12,"DRAM","", 13, 1, 2, '2020-01-24 07:27:03') 
                ]
            ):
            # act

            actual_results = get_all_keywords(self.fake_db, 13, mock_auth_user)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                'scheme_of_work__get_all_keywords'
                , (13, mock_auth_user.user_id)
                , []
                , handle_log_info)
            
            self.assertEqual("DDR", actual_results[0].term)
            self.assertEqual("DRAM", actual_results[2].term)
