from unittest import TestCase
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.cls_lesson import LessonModel, handle_log_info 
from tests.test_helpers.mocks import *

# TODO: #329 - remove global references
get_related_topic_ids = LessonModel.get_related_topic_ids

@patch("shared.models.core.django_helper", return_value=fake_ctx_model())
class test_db__get_related_topics(TestCase):

    def setUp(self):
        ' create fake database context '
        self.fake_db = Mock()
        self.fake_db.connect()


    def tearDown(self):
        self.fake_db.close()


    def test__should_call_select__with_exception(self, mock_ctx):
        # arrange
        expected_exception = KeyError("Bang!")

        with patch.object(ExecHelper, 'select', side_effect=expected_exception):
            
            # act and assert
            with self.assertRaises(Exception):
                get_related_topic_ids(self.fake_db, 0, 1)


    def test__should_call_select__return_no_items(self, mock_ctx):
        # arrange
        expected_result = []

        with patch.object(ExecHelper, "select", return_value=expected_result):
            # act

            rows = get_related_topic_ids(self.fake_db, 0, 2, mock_ctx)

            # assert
            ExecHelper.select.assert_called_with(self.fake_db, 
                'lesson__get_related_topic_ids'
                , (0, 2, mock_ctx.auth_user_id)
                , []
                , handle_log_info)
            self.assertEqual(0, len(rows))


    def test__should_call_select__return_single_item(self, mock_ctx):
        # arrange
        expected_result = [(2,"Image","x",13)]

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            
            # act
            rows = get_related_topic_ids(self.fake_db, 0, 3, mock_ctx)

            # assert
            ExecHelper.select.assert_called_with(self.fake_db, 
                'lesson__get_related_topic_ids'
                , (0, 3, mock_ctx.auth_user_id)
                , []
                , handle_log_info)

            self.assertEqual(1, len(rows), "number of rows not as expected")
            ' first item '
            self.assertEqual(2, rows[0]["id"], "first item not as expected")
            self.assertEqual("Image", rows[0]["name"])


    def test__should_call_select__return_multiple_items(self, mock_ctx):
        # arrange
        expected_result = [(58,"Binary","x",24),(2,"Image","x",13),(64,"Sound","x",17)]

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            
            # act
            rows = get_related_topic_ids(self.fake_db, 0, 3, mock_ctx)

            # assert
            ExecHelper.select.assert_called_with(self.fake_db, 
                'lesson__get_related_topic_ids'
                , (0, 3, mock_ctx.auth_user_id)
                , []
                , handle_log_info)

            self.assertEqual(3, len(rows), "number of rows not as expected")
            ' first item '
            self.assertEqual(58, rows[0]["id"], "first item not as expected")
            self.assertEqual("Binary", rows[0]["name"])
            ' last item'
            self.assertEqual(64, rows[2]["id"], "last item not as expected")
            self.assertEqual("Sound", rows[2]["name"])
