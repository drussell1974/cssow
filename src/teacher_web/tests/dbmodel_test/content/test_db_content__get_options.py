#from ._unittest import TestCase, FakeDb
from shared.models.cls_content import ContentModel, handle_log_info
from unittest.mock import Mock, MagicMock, patch
from unittest import TestCase, skip
from shared.models.core.db_helper import ExecHelper
from tests.test_helpers.mocks import *


@patch("shared.models.core.django_helper", return_value=fake_ctx_model())
class test_db_content__get_options(TestCase):

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
                ContentModel.get_options(self.fake_db, key_stage_id=0)
            

    def test__should_call_select__return_no_items(self, mock_auth_user):
        # arrange
        expected_result = []

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act
            
            rows = ContentModel.get_options(self.fake_db, key_stage_id=1, auth_user=mock_auth_user)

            # assert
            ExecHelper.select.assert_called_with(self.fake_db,
            'content__get_options'
            , (0, 1, mock_auth_user.auth_user_id)
            , []
            , handle_log_info)
            
            self.assertEqual(0, len(rows))


    def test__should_call_select__return_single_item(self, mock_auth_user):
        # arrange
        expected_result = [(17, "Mauris augue est, malesuada eget libero nec.", "A")]

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act
            
            rows = ContentModel.get_options(self.fake_db, key_stage_id=2, auth_user=mock_auth_user)
            
            # assert
            ExecHelper.select.assert_called_with(self.fake_db,
            'content__get_options'
            , (0, 2, mock_auth_user.auth_user_id)
            , []
            , handle_log_info)
            
            self.assertEqual(1, len(rows))
            self.assertEqual(17, rows[0].id)
            self.assertEqual("Mauris augue est, malesuada eget libero nec.", rows[0].description)
            

    def test__should_call_select__return_multiple_items(self, mock_auth_user):
        # arrange
        expected_result = [
            (29,"Sed turpis augue, tristique sed elit ac.", "A"),
            (645,"Ut porta arcu a commodo viverra. Sed.", "B"),
            (107,"Nulla sit amet aliquet enim, quis laoreet.", "C"),
        ]
        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act
            
            rows = ContentModel.get_options(self.fake_db, key_stage_id=3, auth_user=mock_auth_user, scheme_of_work_id=563)
            
            # assert
            ExecHelper.select.assert_called_with(self.fake_db,
            'content__get_options'
            , (563, 3, mock_auth_user.auth_user_id)
            , []
            , handle_log_info)
            
            self.assertEqual(3, len(rows))

            self.assertEqual(29, rows[0].id)
            self.assertEqual("Sed turpis augue, tristique sed elit ac.", rows[0].description)

            self.assertEqual(107, rows[2].id)
            self.assertEqual("Nulla sit amet aliquet enim, quis laoreet.", rows[2].description)
