from unittest import TestCase, skip
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.cls_keystage import KeyStageModel, handle_log_info
from tests.test_helpers.mocks import *

@patch("shared.models.core.django_helper", return_value=fake_ctx_model())
class test_db__get_options(TestCase):
    
    def setUp(self):
        ' fake database context '
        self.fake_db = Mock()
        self.fake_db.cursor = MagicMock()


    def tearDown(self):
        self.fake_db.close()


    def test__should_call_select__with_exception(self, mock_ctx):
        # arrange
        expected_exception = KeyError("Bang!")

        with patch.object(ExecHelper, 'select', side_effect=expected_exception):
            # act and assert

            with self.assertRaises(Exception):
                KeyStageModel.get_options(self.fake_db)


    def test__should_call_select__return_no_items(self, mock_ctx):
        # arrange
        expected_result = []

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act
            
            rows = KeyStageModel.get_options(self.fake_db, mock_ctx)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                'keystage__get_options'
                , (mock_ctx.user_id,)
                , []
                , handle_log_info)

            self.assertEqual(0, len(rows))


    def test__should_call_select__return_single_item(self, mock_ctx):
        # arrange
        expected_result = [
            (4, "KS4")
        ]

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act

            rows = KeyStageModel.get_options(self.fake_db, mock_ctx)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                'keystage__get_options'
                , (mock_ctx.user_id,)
                , []
                , handle_log_info)
            
            self.assertEqual(1, len(rows))

            self.assertEqual(4, rows[0].id)
            self.assertEqual("KS4", rows[0].name)


    def test__should_call_select__return_multiple_item(self, mock_ctx):
        # arrange
        expected_result = [
            (3, "KS3"),
            (4, "KS4"),
            (5, "KS5")
        ]

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act

            rows = KeyStageModel.get_options(self.fake_db, mock_ctx)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                'keystage__get_options'
                , (mock_ctx.user_id,)
                , []
                , handle_log_info)
            
            self.assertEqual(3, len(rows))

            self.assertEqual(3, rows[0].id)
            self.assertEqual("KS3", rows[0].name)

            self.assertEqual(5, rows[2].id)
            self.assertEqual("KS5", rows[2].name)