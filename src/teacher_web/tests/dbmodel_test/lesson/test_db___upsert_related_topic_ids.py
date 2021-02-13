from unittest import TestCase
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.cls_lesson import LessonDataAccess, LessonModel, handle_log_info 
from tests.test_helpers.mocks import *

@patch("shared.models.core.django_helper", return_value=fake_ctx_model())
class test_db___upsert_related_topic_ids(TestCase):


    def setUp(self):
        ' fake database context '
        self.fake_db = Mock()
        self.fake_db.cursor = MagicMock()
        

    def tearDown(self):
        pass


    def test_should_raise_exception(self, mock_auth_user):
        # arrange
        expected_exception = KeyError("Bang!")

        model = LessonModel(0, "")

        with patch.object(ExecHelper, 'insert', side_effect=expected_exception):
            
            # act and assert
            with self.assertRaises(Exception):
                # act 
                LessonDataAccess._upsert_related_topic_ids(self.fake_db, model, auth_user_id=99)


    
    def test_should_call__reinsert__related_topic_ids(self, mock_auth_user):
         # arrange
        model = LessonModel(10, "")
        model.related_topic_ids = ["201","202"]
        expected_result = []

        with patch.object(ExecHelper, 'insert', return_value=expected_result):
            # act

            actual_result = LessonDataAccess._upsert_related_topic_ids(self.fake_db, model, [], auth_user_id=99)
            
            # assert

            ExecHelper.insert.assert_called_with(self.fake_db, 
              'lesson__insert_related_topic'
              , (10, '202', 99)
              , handle_log_info)

        self.assertEqual(actual_result, expected_result)
    