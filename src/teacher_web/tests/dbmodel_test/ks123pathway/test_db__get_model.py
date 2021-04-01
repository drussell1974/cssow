from unittest import TestCase, skip
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.cls_lesson import LessonModel
from shared.models.cls_ks123pathway import KS123PathwayModel, handle_log_info
from shared.models.cls_department import DepartmentModel
from shared.models.enums.publlished import STATE
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

            with self.assertRaises(KeyError):
                KS123PathwayModel.get_model(self.fake_db, pathway_item_id=97, auth_ctx=mock_auth_user)


    def test__should_call_select__return_no_item(self, mock_auth_user):
        # arrange
        expected_result = []

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act
            
            actual_result = KS123PathwayModel.get_model(self.fake_db, pathway_item_id=101, auth_ctx=mock_auth_user)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                'ks123_pathway__get_model'
                , (101, mock_auth_user.department_id, 1, mock_auth_user.auth_user_id) 
                , []
                , handle_log_info)
            
            self.assertIsNone(actual_result)


    def test__should_call_select__return_single_item(self, mock_auth_user):
        # arrange
        expected_result = [
            (702, "Fringilla purus lacus, ut volutpat nibh euismod.", 10, "Year 10", 2, "Algorithms", int(STATE.PUBLISH))
            ]

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act

            actual_result = KS123PathwayModel.get_model(self.fake_db, pathway_item_id=73, auth_ctx=mock_auth_user)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                'ks123_pathway__get_model'
                , (73, mock_auth_user.department_id, 1, mock_auth_user.auth_user_id) 
                , []
                , handle_log_info)
                
            self.assertEqual(702, actual_result.id)
            self.assertEqual("Fringilla purus lacus, ut volutpat nibh euismod.", actual_result.objective)
            self.assertEqual(10, actual_result.year_id)
            self.assertEqual(2, actual_result.topic_id)
