from datetime import datetime, timedelta
from unittest import TestCase, skip
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.cls_lesson_schedule import LessonScheduleModel, handle_log_info
from tests.test_helpers.mocks import *


@patch("shared.models.core.django_helper", return_value=fake_ctx_model())
class test_db__get_all(TestCase):

    def setUp(self):
        ' fake database context '
        self.fake_db = Mock()
        self.fake_db.cursor = MagicMock()


    def tearDown(self):
        self.fake_db.close()


    def test__should_call_select_with_exception(self, mock_ctx):
        # arrange
        expected_exception = KeyError("Bang!")

        with patch.object(ExecHelper, 'select', side_effect=expected_exception):
            # act and assert

            with self.assertRaises(KeyError):
                LessonScheduleModel.get_all(self.fake_db, lesson_id=34, scheme_of_work_id=11, auth_user=mock_ctx)


    def test__should_call_select_return_no_items(self, mock_ctx):
        # arrange
        expected_result = []

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act
            
            rows = LessonScheduleModel.get_all(self.fake_db, lesson_id=34, scheme_of_work_id=11, auth_user=mock_ctx)

            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                'lesson_schedule__get_all'
                , (34, mock_ctx.academic_year.start_date, mock_ctx.academic_year.end_date, 1, mock_ctx.auth_user_id)
                , []
                , handle_log_info)
                
            self.assertEqual(0, len(rows))


    def test__should_call_select_return_single_item(self, mock_ctx):
        # arrange
        expected_result = [(569, "7x", "ABCDEF", "2021-04-03 11:30:34", 6, 11, 1, 99)]

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act

            actual_results = LessonScheduleModel.get_all(self.fake_db, lesson_id=34, scheme_of_work_id=11, auth_user=mock_ctx)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                'lesson_schedule__get_all'
                , (34, mock_ctx.academic_year.start_date, mock_ctx.academic_year.end_date, 1, mock_ctx.auth_user_id)
                , []
                , handle_log_info)
                

            self.assertEqual(1, len(actual_results))

            self.assertEqual(569, actual_results[0].id)
            self.assertEqual("ABCDEF", actual_results[0].class_code)
            self.assertEqual("7x", actual_results[0].class_name)
            self.assertEqual("2021-04-03 11:30:34", actual_results[0].start_date)


    def test__should_call_select_return_multiple_item(self, mock_ctx):
        # arrange
        expected_result = [
            (569, "7x", "ABCDEX", "2021-04-03 09:00:00", 6, 11, 1, 99),
            (570, "7y", "ABCDEY", "2021-04-04 10:00:00", 6, 11, 1, 99),
            (571, "7z", "ABCDEZ", "2021-04-04 13:30:04", 6, 11, 1, 99)
            ]

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act

            actual_results = LessonScheduleModel.get_all(self.fake_db, lesson_id=34, scheme_of_work_id=11, auth_user=mock_ctx)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                'lesson_schedule__get_all'
                , (34, mock_ctx.academic_year.start_date, mock_ctx.academic_year.end_date, 1, mock_ctx.auth_user_id)
                , []
                , handle_log_info)

            self.assertEqual(3, len(actual_results))

            self.assertEqual(569, actual_results[0].id)
            self.assertEqual("ABCDEX", actual_results[0].class_code)
            self.assertEqual("7x", actual_results[0].class_name)
            self.assertEqual("2021-04-03 09:00:00", actual_results[0].start_date)
            

            self.assertEqual(571, actual_results[2].id)
            self.assertEqual("ABCDEZ", actual_results[2].class_code)
            self.assertEqual("7z", actual_results[2].class_name)
            self.assertEqual("2021-04-04 13:30:04", actual_results[2].start_date)



    def test__should_call_select_return_current_items_only(self, mock_ctx):
        # arrange
        expected_result = [
            (765569, "7x", "ABCDEX", "2121-04-03 09:00:00", 6, 11, 1, 99),
            (765570, "7y", "ABCDEY", "2121-04-04 10:00:00", 6, 11, 1, 99),
            (765571, "7z", "ABCDEZ", "2121-04-04 13:30:04", 6, 11, 1, 99)
            ]

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act

            actual_results = LessonScheduleModel.get_all(self.fake_db, lesson_id=34, scheme_of_work_id=11, auth_user=mock_ctx, show_next_days=7)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                'lesson_schedule__get_all'
                , (34, datetime.today().date(), datetime.today().date() + timedelta(7), 1, mock_ctx.auth_user_id)
                , []
                , handle_log_info)

            self.assertEqual(3, len(actual_results))

            self.assertEqual(765569, actual_results[0].id)
            self.assertEqual("ABCDEX", actual_results[0].class_code)
            self.assertEqual("7x", actual_results[0].class_name)
            self.assertEqual("2121-04-03 09:00:00", actual_results[0].start_date)
            

            self.assertEqual(765571, actual_results[2].id)
            self.assertEqual("ABCDEZ", actual_results[2].class_code)
            self.assertEqual("7z", actual_results[2].class_name)
            self.assertEqual("2121-04-04 13:30:04", actual_results[2].start_date)

