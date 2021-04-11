from unittest import TestCase, skip
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.core.log_handlers import handle_log_info
from shared.models.cls_lesson_schedule import LessonScheduleModel as Model, handle_log_info
from tests.test_helpers.mocks import *

@patch("shared.models.core.django_helper", return_value=fake_ctx_model())
class test_db__delete(TestCase):

    def setUp(self):
        ' fake database context '
        self.fake_db = Mock()
        self.fake_db.cursor = MagicMock()

        
    def tearDown(self):
        pass


    def test_should_raise_exception(self, mock_auth_user):
        # arrange
        expected_exception = KeyError("Bang!")

        model = fake_lesson_schedule(1, title="Vivamus at porta orci. Aliquam sem sapien, tristique ac tincidunt eget", class_name="7B", class_code="ABCDFD", start_date="2021-06-09T17:20", lesson_id=15, scheme_of_work_id=115, auth_ctx=mock_auth_user)

        with patch.object(ExecHelper, 'delete', side_effect=expected_exception):
            
            # act and assert
            with self.assertRaises(KeyError):
                # act 
                Model.delete(self.fake_db, model, mock_auth_user)


    def test_should_call__delete(self, mock_auth_user):
         # arrange

        model = fake_lesson_schedule(1, title="Vivamus at porta orci. Aliquam sem sapien, tristique ac tincidunt eget", class_name="7B", class_code="ABCDFD", start_date="2021-06-09T17:20", lesson_id=15, scheme_of_work_id=115, auth_ctx=mock_auth_user)

        expected_result = [(1)]

        with patch.object(ExecHelper, 'delete', return_value=expected_result):
            # act

            actual_result = Model.delete(self.fake_db, model, mock_auth_user)
            
            # assert

            ExecHelper.delete.assert_called_with(self.fake_db, 
                'lesson_schedule__delete'
                , (1, mock_auth_user.auth_user_id)
                , handle_log_info)
            
            self.assertEqual(1, actual_result.id)
            self.assertEqual("7B", actual_result.class_name)
            self.assertEqual("ABCDFD", actual_result.class_code)