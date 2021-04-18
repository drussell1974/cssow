from unittest import TestCase, skip
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.cls_topic import TopicModel, handle_log_info
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

            with self.assertRaises(Exception):
                TopicModel.get_model(self.fake_db, 4)


    def test__should_call_select__return_no_items(self, mock_auth_user):
        # arrange
        expected_result = []

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act
            
            actual_results = TopicModel.get_model(self.fake_db, topic_id=99, auth_ctx=mock_auth_user)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                'topic__get_model'
                , (99, mock_auth_user.department_id, int(STATE.PUBLISH), mock_auth_user.auth_user_id)
                , []
                , handle_log_info)

            self.assertIsNone(actual_results)


    def test__should_call_select__return_single_item(self, mock_auth_user):
        # arrange

        expected_result = [
            (321, 'Numbering systems', 1, datetime(2021, 2, 27, 15, 26), 0, 1, 0, 'Computing', 0, datetime(2021, 2, 27, 15, 26), 2)
        ]

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act

            actual_results = TopicModel.get_model(self.fake_db, topic_id=321,  auth_ctx=mock_auth_user)

            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                "topic__get_model"
                , (321, mock_auth_user.department_id, int(STATE.PUBLISH), mock_auth_user.auth_user_id)
                , []
                , handle_log_info)
            

            self.assertEqual(321, actual_results.id)
            self.assertEqual("Numbering systems", actual_results.name)
            self.assertEqual(1, actual_results.lvl)
            self.assertEqual("Computing", actual_results.parent.name)
            self.assertEqual(0, actual_results.parent.lvl)
            self.assertEqual(1, actual_results.parent.published)
            self.assertTrue(actual_results.is_from_db)
            