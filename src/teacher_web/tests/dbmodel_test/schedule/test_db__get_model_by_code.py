from unittest import TestCase, skip
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.cls_lesson_schedule import LessonScheduleModel as Model, handle_log_info
from tests.test_helpers.mocks import fake_ctx_model

@patch("shared.models.core.django_helper", return_value=fake_ctx_model())
class test_db__get_model_by_class_code(TestCase):
    
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
                Model.get_model_by_class_code(self.fake_db, class_code="FOOBAR", auth_user=mock_auth_user)


    @skip("not implemented")
    def test__should_call_select__return_no_items(self, mock_auth_user):
        # arrange
        expected_result = []

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act
            
            actual_result = Model.get_model(self.fake_db, 99, scheme_of_work_id=54, auth_user=mock_auth_user)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                'lesson_schedule__get_by_class_code$2'
                , (99, 1, mock_auth_user.auth_user_id)
                , []
                , handle_log_info)

            self.assertIsNone(actual_result)


    @skip("not implemented")
    def test__should_call_select__return_single_item(self, mock_auth_user):
        # arrange
        expected_result = [(6, "ABCDEF", "", 11, 1234, 67, 12767111276711, 1, 99)]

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act

            model = Model.get_model(self.fake_db, lesson_id=6, scheme_of_work_id=11, auth_user=mock_auth_user)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                'lesson_schedule__get_by_class_code$2'
                , (6, 1, mock_auth_user.auth_user_id)
                , []
                , handle_log_info)

            self.assertEqual(6, model.id)
            self.assertEqual("ABCDEF", model.class_code)
            self.assertEqual(11, model.scheme_of_work_id)
            self.assertEqual(1234, model.lesson_id)
            self.assertEqual(0, model.department_id)
            self.assertEqual(0, model.institute_id)
            self.assertFalse(model.is_new())
            self.assertTrue(model.is_from_db)



