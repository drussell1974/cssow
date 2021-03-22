from unittest import TestCase
from shared.models.cls_lesson_schedule import LessonScheduleModel

class test_cls_lesson_schedule__clean_up(TestCase):

    def setUp(self):
        self.test = LessonScheduleModel(1, "", lesson_id = 34, scheme_of_work_id = 12, department_id=67, institute_id=12711671276711)

    # class_code

    def test_class_code__trim_whitespace(self):

        self.test.class_code = " x "

        # test
        self.test._clean_up()

        # assert
        self.assertEqual("x", self.test.class_code)
