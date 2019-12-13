import sys
sys.path.append('../../schemeofwork/modules')
from cls_lessonplan import LessonPlanModel

from unittest import TestCase

class test_cls_lesson_plan__clean_up(TestCase):

    def setUp(self):
        self.test = LessonPlanModel(id_=0, learning_episode_id = 0, title="", description="", task_icon = "")

    def test_title__trim_whitespace(self):

        self.test.title = " x "

        # test
        self.test._clean_up()

        # assert
        self.assertEqual("x", self.test.title)


    def test_title__escape_sqlterminator(self):

        self.test.title = "x;"

        # test
        self.test._clean_up()

        # assert
        self.assertEqual("x\;", self.test.title)


    def test_title__escape_quote(self):

        self.test.title = "'x'"

        # test
        self.test._clean_up()

        # assert
        self.assertEqual('"x"', self.test.title)


    def test_description__trim_whitespace(self):

        self.test.description = " x "

        # test
        self.test._clean_up()

        # assert
        self.assertEqual("x", self.test.description)


    def test_description__escape_sqlterminator(self):

        self.test.description = "x;"

        # test
        self.test._clean_up()

        # assert
        self.assertEqual("x\;", self.test.description)


    def test_description__escape_quote(self):

        self.test.description = "'x'"

        # test
        self.test._clean_up()

        # assert
        self.assertEqual('"x"', self.test.description)


    def test_task_icon__trim_whitespace(self):

        self.test.task_icon = " x "

        # test
        self.test._clean_up()

        # assert
        self.assertEqual("x", self.test.task_icon)


    def test_task_icon__escape_sqlterminator(self):

        self.test.task_icon = "x;"

        # test
        self.test._clean_up()

        # assert
        self.assertEqual("x\;", self.test.task_icon)


    def test_task_icon__escape_quote(self):

        self.test.task_icon = "'x'"

        # test
        self.test._clean_up()

        # assert
        self.assertEqual('"x"', self.test.task_icon)