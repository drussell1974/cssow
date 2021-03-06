from unittest import TestCase
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.core.log_handlers import handle_log_info
from shared.models.cls_lesson_schedule import LessonScheduleModel
from shared.models.enums.publlished import STATE
from tests.test_helpers.mocks import fake_ctx_model

@patch("shared.models.core.django_helper", return_value=fake_ctx_model())
class test_db__deleteunpublished(TestCase):


    def setUp(self):
        ' fake database context '
        self.fake_db = Mock()
        self.fake_db.cursor = MagicMock()
        self.handle_log_info = MagicMock()
        
    def tearDown(self):
        pass


    def test_should_raise_exception(self, mock_auth_user):
        # arrange
        expected_exception = KeyError("Bang!")

        #LessonScheduleModel(0, title="Vivamus at porta orci. Aliquam sem sapien, tristique ac tincidunt eget", class_name="7x", class_code="ABCDEF", start_date="2021-06-09T17:20", lesson_id=12, scheme_of_work_id=34, auth_user=mock_auth_user)

        with patch.object(ExecHelper, 'delete', side_effect=expected_exception):
            
            # act and assert
            with self.assertRaises(KeyError):
                # act 
                LessonScheduleModel.delete_unpublished(self.fake_db, lesson_id=866, scheme_of_work_id=34, auth_user=mock_auth_user)


    def test_should_call__delete(self, mock_auth_user):
         # arrange

        with patch.object(ExecHelper, 'delete', return_value=(5)):
            # act

            actual_result = LessonScheduleModel.delete_unpublished(self.fake_db, lesson_id=99, scheme_of_work_id=12, auth_user=mock_auth_user)
            
            # assert
            ExecHelper.delete.assert_called_with(self.fake_db,
                'lesson_schedule__delete_unpublished'
                , (99, 12, mock_auth_user.auth_user_id)
                , handle_log_info)

            self.assertEqual(5, actual_result)
