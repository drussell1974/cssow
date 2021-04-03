from unittest import TestCase
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.cls_lesson_schedule import LessonScheduleModel as Model, handle_log_info
from tests.test_helpers.mocks import fake_ctx_model

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
                Model.get_model(self.fake_db, schedule_id=101, lesson_id=93, scheme_of_work_id=54, auth_user=mock_auth_user)


    def test__should_call_select__return_no_items(self, mock_auth_user):
        # arrange
        expected_result = []

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act
            
            actual_result = Model.get_model(self.fake_db, schedule_id=987, lesson_id=99, scheme_of_work_id=54, auth_user=mock_auth_user)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                'lesson_schedule__get$2'
                , (987, 1, mock_auth_user.auth_user_id)
                , []
                , handle_log_info)

            self.assertIsNone(actual_result)


    def test__should_call_select__return_single_item(self, mock_auth_user):
        # arrange
        expected_result = [("7x", "ABCDEF", "", 6, 11, 1, 99)]

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act

            model = Model.get_model(self.fake_db, schedule_id=987, lesson_id=6, scheme_of_work_id=11, auth_user=mock_auth_user)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                'lesson_schedule__get$2'
                , (987, 1, mock_auth_user.auth_user_id)
                , []
                , handle_log_info)

            self.assertEqual(987, model.id)
            self.assertEqual("ABCDEF", model.class_code)
            self.assertEqual(11, model.scheme_of_work_id)
            self.assertEqual(6, model.lesson_id)
            self.assertEqual(99, model.created_by_id)
            self.assertFalse(model.is_new())
            self.assertTrue(model.is_from_db)



