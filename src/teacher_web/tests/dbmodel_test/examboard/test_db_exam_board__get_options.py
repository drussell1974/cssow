from shared.models.cls_examboard import ExamBoardModel
from unittest.mock import Mock, MagicMock, patch
from unittest import TestCase, skip
from shared.models.core.db_helper import ExecHelper
from shared.models.core.log_handlers import handle_log_info
from shared.models.cls_department import DepartmentModel
from tests.test_helpers.mocks import fake_ctx_model

@patch("shared.models.core.django_helper", return_value=fake_ctx_model())
class test_db_exam_board__get_options(TestCase):
    
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
                ExamBoardModel.get_options(self.fake_db)


    def test__should_call_select__return_no_items(self, mock_auth_user):
        # arrange
        expected_result = []

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act
            
            rows = ExamBoardModel.get_options(self.fake_db, mock_auth_user)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                 'examboard__get_options'
                 , (mock_auth_user.auth_user_id,)
                 , []
                 , handle_log_info)
            self.assertEqual(0, len(rows))


    def test__should_call_select__return_single_item(self, mock_auth_user):
        # arrange
        expected_result = [(123, "Item 1")]

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act

            rows = ExamBoardModel.get_options(self.fake_db, mock_auth_user)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                 'examboard__get_options'
                 , (mock_auth_user.auth_user_id,)
                 , [], handle_log_info)

            self.assertEqual(1, len(rows))
            self.assertEqual(123, rows[0].id)
            self.assertEqual("Item 1", rows[0].name)


    def test__should_call_select__return_multiple_item(self, mock_auth_user):
        # arrange
        expected_result = [(1, "Item 1"),(2,"Item 2"),(3, "Item 3")]

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act

            rows = ExamBoardModel.get_options(self.fake_db, mock_auth_user)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                 'examboard__get_options'
                 , (mock_auth_user.auth_user_id,)
                 , []
                 , handle_log_info)
            
            self.assertEqual(3, len(rows))

            self.assertEqual(1, rows[0].id)
            self.assertEqual("Item 1", rows[0].name)

            self.assertEqual(3, rows[2].id)
            self.assertEqual("Item 3", rows[2].name)
