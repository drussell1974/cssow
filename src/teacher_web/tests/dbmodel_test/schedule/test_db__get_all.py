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
            
            mock_ctx.institute_id = 12767111276711 # explicitly set

            with self.assertRaises(KeyError):
                LessonScheduleModel.get_all(self.fake_db, lesson_id=34, scheme_of_work_id=11, auth_user=mock_ctx)


    def test__should_call_select_return_no_items(self, mock_ctx):
        # arrange
        expected_result = []

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act

            mock_ctx.institute_id = 12767111276711 # explicitly set

            rows = LessonScheduleModel.get_all(self.fake_db, lesson_id=34, scheme_of_work_id=11, auth_user=mock_ctx)

            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                'lesson_schedule__get_all$3'
                , (34, 11, mock_ctx.department_id, mock_ctx.institute_id, mock_ctx.academic_year.start_date, mock_ctx.academic_year.end_date, 1, mock_ctx.auth_user_id)
                , []
                , handle_log_info)
                
            self.assertEqual(0, len(rows))


    def test__should_call_select_return_single_item(self, mock_ctx):
        # arrange
        expected_result = [(569, "Aenean egestas erat ac turpis aliquet iaculis", "A-Level Computer Science", "7x", "ABCDEF", datetime(2020, 4, 3, 11, 30), 6, 11, 5, 2, 1, 99)]

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act

            mock_ctx.institute_id = 12767111276711 # explicitly set

            actual_results = LessonScheduleModel.get_all(self.fake_db, lesson_id=34, scheme_of_work_id=11, auth_user=mock_ctx)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                'lesson_schedule__get_all$3'
                , (34, 11, mock_ctx.department_id, mock_ctx.institute_id, mock_ctx.academic_year.start_date, mock_ctx.academic_year.end_date, 1, mock_ctx.auth_user_id)
                , []
                , handle_log_info)
                

            self.assertEqual(1, len(actual_results))

            self.assertEqual(569, actual_results[0].id)
            self.assertEqual("Aenean egestas erat ac turpis aliquet iaculis", actual_results[0].title)
            self.assertEqual("A-Level Computer Science", actual_results[0].scheme_of_work_name)
            self.assertEqual("ABCDEF", actual_results[0].class_code)
            self.assertEqual("7x", actual_results[0].class_name)
            self.assertEqual(datetime(2020, 4, 3, 11, 30), actual_results[0].start_date)
            self.assertEqual("2020-04-03T11:30", actual_results[0].start)
            self.assertEqual("2020-04-03", actual_results[0].start_date_ui_date)
            self.assertEqual("11:30", actual_results[0].start_date_ui_time)


    def test__should_call_select_return_multiple_item(self, mock_ctx):
        # arrange
        expected_result = [
            (569, "Proin sit amet elementum lectus", "A-Level Computer Science", "7x", "ABCDEX", datetime(2021, 4, 3, 9, 00), 6, 11, 5, 2, 1, 99),
            (570, "Maecenas finibus tellus", "A-Level Computer Science", "7y", "ABCDEY", datetime(2020, 4, 4, 0, 0), 6, 11, 1, 7, 2, 99),
            (571, "Vivamus at porta orci. Aliquam sem sapien, tristique ac tincidunt eget", "KS3 Computing", "7z", "ABCDEZ", datetime(2020, 4, 4, 13, 30, 4), 6, 11, 7, 2, 1, 99)
            ]

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act

            mock_ctx.institute_id = 12767111276711 # explicitly set

            actual_results = LessonScheduleModel.get_all(self.fake_db, lesson_id=34, scheme_of_work_id=11, auth_user=mock_ctx)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                'lesson_schedule__get_all$3'
                , (34, 11, mock_ctx.department_id, mock_ctx.institute_id, mock_ctx.academic_year.start_date, mock_ctx.academic_year.end_date, 1, mock_ctx.auth_user_id)
                , []
                , handle_log_info)

            self.assertEqual(3, len(actual_results))

            self.assertEqual(569, actual_results[0].id)
            self.assertEqual("Proin sit amet elementum lectus", actual_results[0].title)
            self.assertEqual("A-Level Computer Science", actual_results[0].scheme_of_work_name)
            self.assertEqual("ABCDEX", actual_results[0].class_code)
            self.assertEqual("7x", actual_results[0].class_name)
            self.assertEqual(datetime(2021, 4, 3, 9, 0), actual_results[0].start_date)
            self.assertEqual("2021-04-03T09:00", actual_results[0].start)
            self.assertEqual("2021-04-03", actual_results[0].start_date_ui_date)
            self.assertEqual("09:00", actual_results[0].start_date_ui_time)
            

            self.assertEqual(571, actual_results[2].id)
            self.assertEqual("Vivamus at porta orci. Aliquam sem sapien, tristique ac tincidunt eget", actual_results[2].title)
            self.assertEqual("KS3 Computing", actual_results[2].scheme_of_work_name)
            self.assertEqual("ABCDEZ", actual_results[2].class_code)
            self.assertEqual("7z", actual_results[2].class_name)
            self.assertEqual(datetime(2020, 4, 4, 13, 30, 4), actual_results[2].start_date)
            self.assertEqual("2020-04-04T13:30", actual_results[2].start)
            self.assertEqual("2020-04-04", actual_results[2].start_date_ui_date)
            self.assertEqual("13:30", actual_results[2].start_date_ui_time)


    def test__should_call_select_return_current_items_only(self, mock_ctx):
        # arrange
        expected_result = [
            (765569, "Vivamus at porta orci. Aliquam sem sapien, tristique ac tincidunt eget", "KS3 Computing", "7x", "ABCDEX", datetime(2021, 4, 3, 9, 0), 6, 11, 5, 2, 1, 99),
            (765570, "Proin sit amet elementum lectus","KS3 Computing", "7y", "ABCDEY", datetime(2021, 4, 4, 10, 0), 6, 11, 5, 2, 1, 99),
            (765571, "Maecenas finibus tellus","KS3 Computing", "7z", "ABCDEZ", datetime(2021, 4, 4, 13, 30, 4), 6, 11, 5, 2, 1, 99)
            ]

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act

            actual_results = LessonScheduleModel.get_all(self.fake_db, lesson_id=34, scheme_of_work_id=11, auth_user=mock_ctx, show_next_days=7)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                'lesson_schedule__get_all$3'
                , (34, 11, mock_ctx.department_id, mock_ctx.institute_id, datetime.today().date(), datetime.today().date() + timedelta(7), 1, mock_ctx.auth_user_id)
                , []
                , handle_log_info)

            self.assertEqual(3, len(actual_results))

            self.assertEqual(765569, actual_results[0].id)
            self.assertEqual("Vivamus at porta orci. Aliquam sem sapien, tristique ac tincidunt eget", actual_results[0].title)
            self.assertEqual("KS3 Computing", actual_results[0].scheme_of_work_name)
            self.assertEqual("ABCDEX", actual_results[0].class_code)
            self.assertEqual("7x", actual_results[0].class_name)
            self.assertEqual(datetime(2021, 4, 3, 9, 0), actual_results[0].start_date)
            self.assertEqual("2021-04-03T09:00", actual_results[0].start)
            self.assertEqual("2021-04-03", actual_results[0].start_date_ui_date)
            self.assertEqual("09:00", actual_results[0].start_date_ui_time)
            

            self.assertEqual(765571, actual_results[2].id)
            self.assertEqual("Maecenas finibus tellus", actual_results[2].title)
            self.assertEqual("KS3 Computing", actual_results[2].scheme_of_work_name)
            self.assertEqual("ABCDEZ", actual_results[2].class_code)
            self.assertEqual("7z", actual_results[2].class_name)
            self.assertEqual(datetime(2021, 4, 4, 13, 30, 4), actual_results[2].start_date)
            self.assertEqual("2021-04-04T13:30", actual_results[2].start)
            self.assertEqual("2021-04-04", actual_results[2].start_date_ui_date)
            self.assertEqual("13:30", actual_results[2].start_date_ui_time)
            