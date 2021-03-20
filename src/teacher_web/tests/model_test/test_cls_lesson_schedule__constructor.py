from unittest import TestCase
from shared.models.cls_lesson_schedule import LessonScheduleModel

class test_cls_lesson_schedule__constructor(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass


    def test_constructor_default(self):

        # arrange

        self.test = LessonScheduleModel(0, "", lesson_id=12, scheme_of_work_id=34)

        # assert
        self.assertEqual(0, self.test.id)
        self.assertEqual("", self.test.class_code)
        self.assertEqual(12, self.test.lesson_id)
        self.assertEqual(34, self.test.scheme_of_work_id)
        self.assertFalse(self.test.is_valid)
        self.assertTrue(self.test.is_new())


    def test_constructor_set_valid_values(self):


        # arrange

        self.test = LessonScheduleModel(0, "ABCDEF", lesson_id=12, scheme_of_work_id=34)

        # assert
        self.assertEqual(0, self.test.id)
        self.assertEqual("ABCDEF", self.test.class_code)
        self.assertEqual(12, self.test.lesson_id)
        self.assertEqual(34, self.test.scheme_of_work_id)
        self.assertFalse(self.test.is_valid)
        self.assertTrue(self.test.is_new())