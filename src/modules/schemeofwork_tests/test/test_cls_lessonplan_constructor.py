import sys
sys.path.append('../../schemeofwork/modules/')

from unittest import TestCase

from cls_lessonplan import LessonPlanModel


class test_cls_lessonplan_constructor(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass


    def test_constructor_default(self):

        # self.test
        self.test = LessonPlanModel(0, title = "Activity 1", description="Description here!", task_icon = "", lesson_id = 0)

        # test
        self.test.validate()

        # assert
        self.assertEqual(0, self.test.id)
        self.assertEqual("Activity 1", self.test.title, "title should be ''")
        self.assertEqual("Description here!", self.test.description, "description should be ''")
        self.assertEqual(0, self.test.lesson_id, "lesson_id should be 0")

