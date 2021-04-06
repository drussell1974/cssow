from datetime import datetime, timedelta
from unittest import TestCase
from unittest.mock import patch
from shared.models.cls_lesson_schedule import LessonScheduleModel
from tests.test_helpers.mocks import fake_ctx_model

class test_cls_lesson_schedule__display_date(TestCase):

    def setUp(self):
        with patch("shared.models.core.django_helper", return_value=fake_ctx_model()) as mock_auth_user:    
            self.test = LessonScheduleModel(1, start_date=None, class_name="7x", class_code="", lesson_id = 34, scheme_of_work_id = 12, auth_user=mock_auth_user)


    def test_display_date__when_none(self):

        # arrange 
        self.test.start_date = None

        # assert
        self.assertEqual("", self.test.display_date)


    def test_display_date__when_today(self):

        # arrange 
        self.test.start_date = datetime.now()

        # assert
        self.assertTrue(self.test.is_today)
        self.assertEqual("Today", self.test.display_date)


    def test_display_date__when_past(self):

        # arrange 
        self.test.start_date = datetime(year=2019, month=3, day=31, hour=14, minute=0, second=0)
        # assert
        self.assertFalse(self.test.is_today)
        self.assertEqual("Sunday, 31st March 2019", self.test.display_date)


    def test_display_date__when_other_than_today__future(self):

        # arrange 
        self.test.start_date = datetime(year=2121, month=3, day=31, hour=14, minute=0, second=0)
        # assert
        self.assertFalse(self.test.is_today)
        self.assertEqual("Monday, 31st March 2121", self.test.display_date)


class test_cls_lesson_schedule__input_date(TestCase):

    def setUp(self):
        with patch("shared.models.core.django_helper", return_value=fake_ctx_model()) as mock_auth_user:    
            self.test = LessonScheduleModel(1, start_date=None, class_name="7x", class_code="", lesson_id = 34, scheme_of_work_id = 12, auth_user=mock_auth_user)


    def test_input_date__when_none(self):

        # arrange 
        self.test.start_date = None

        # assert
        self.assertEqual("", self.test.input_date)


    def test_input_date__when_past(self):

        # arrange 
        self.test.start_date = datetime(year=2019, month=9, day=30, hour=11, minute=56, second=2)
        # assert
        self.assertFalse(self.test.is_today)
        self.assertEqual("2019-09-30T11:56:02", self.test.input_date)


    def test_input_date__when_other_than_today__future(self):

        # arrange 
        self.test.start_date = datetime(year=2121, month=3, day=15, hour=14, minute=0, second=0)
        # assert
        self.assertFalse(self.test.is_today)
        self.assertEqual("2121-03-15T14:00:00", self.test.input_date)
