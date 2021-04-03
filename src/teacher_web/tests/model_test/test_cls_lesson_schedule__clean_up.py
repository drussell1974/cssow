from unittest import TestCase
from unittest.mock import patch
from shared.models.cls_lesson_schedule import LessonScheduleModel
from tests.test_helpers.mocks import fake_ctx_model

class test_cls_lesson_schedule__clean_up(TestCase):

    def setUp(self):
        with patch("shared.models.core.django_helper", return_value=fake_ctx_model()) as mock_auth_user:    
            self.test = LessonScheduleModel(1, start_date=None, class_name="7x", class_code="", lesson_id = 34, scheme_of_work_id = 12, auth_user=mock_auth_user)

    # class_code

    def test_class_code__trim_whitespace(self):

        self.test.class_code = " x "

        # test
        self.test._clean_up()

        # assert
        self.assertEqual("x", self.test.class_code)


    # class_name

    def test_class_name__trim_whitespace(self):

        self.test.class_name = " x "

        # test
        self.test._clean_up()

        # assert
        self.assertEqual("x", self.test.class_name)
