from unittest import TestCase, skip
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.cls_keyword import KeywordModel, handle_log_info
from tests.test_helpers.mocks import *

@patch("shared.models.core.django_helper", return_value=fake_ctx_model())
class test_db__get_model(TestCase):


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
                KeywordModel.get_model(self.fake_db, 4)


    def test__should_call_select__return_no_items(self, mock_auth_user):
        # arrange
        expected_result = []

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act
            
            actual_results = KeywordModel.get_model(self.fake_db, 22, 11, auth_user=mock_auth_user)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                'keyword__get'
                , (22, 11, mock_auth_user.id)
                , []
                , handle_log_info)
                
            self.assertEqual(0, actual_results.id)


    def test__should_call_select__return_single_item(self, mock_auth_user):
        # arrange
        expected_result = [
            (702, "Fringilla", "purus lacus, ut volutpat nibh euismod.", 13, 1)
        ]

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act

            actual_results = KeywordModel.get_model(self.fake_db, 702, 11, auth_user=mock_auth_user)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                "keyword__get"
                , (702, 11, mock_auth_user.id)
                , []
                , handle_log_info)
                
            self.assertEqual(702, actual_results.id)
            self.assertEqual("Fringilla", actual_results.term),
            self.assertEqual("purus lacus, ut volutpat nibh euismod.", actual_results.definition)
            self.assertEqual(13, actual_results.scheme_of_work_id)
            self.assertEqual(1, actual_results.published)
            self.assertEqual([], actual_results.belongs_to_lessons)
