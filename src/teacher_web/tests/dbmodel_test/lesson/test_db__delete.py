from unittest import TestCase
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.cls_lesson import LessonModel as Model, LessonDataAccess, handle_log_info
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

        with patch.object(ExecHelper, 'delete', side_effect=expected_exception):
            
            # act and assert
            with self.assertRaises(Exception):
                # act 
                Model.delete(self.fake_db, 99, lesson_id=456)


    def test_should_call__delete(self, mock_auth_user):
         # arrange

        with patch.object(ExecHelper, 'delete', return_value=Model(102)):
            # act

            actual_result = Model.delete(self.fake_db, mock_auth_user, lesson_id=102)
            
            # assert
            ExecHelper.delete.assert_called()

            ExecHelper.delete.assert_called_with(self.fake_db, 
                'lesson__delete'
                , (102, mock_auth_user.id)
                , handle_log_info)
            
            self.assertEqual(102, actual_result.id)