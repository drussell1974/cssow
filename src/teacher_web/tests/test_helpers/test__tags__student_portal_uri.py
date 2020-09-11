from unittest import TestCase
from shared.models.utils.tags import student_uri

class test__tags__student_portal_uri(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_should_return_base_uri(self):
        # arrange
        # act
        actual = student_uri()
        # assert
        self.assertEqual("http://localhost:3001", actual)


    def test_should_return_scheme_of_work_uri(self):
        # arrange
        # act
        actual = student_uri(11)
        # assert
        self.assertEqual("http://localhost:3001/course/11", actual)


    def test_should_return_lesson_uri(self):
        # arrange
        # act
        actual = student_uri(11, 220)
        # assert
        self.assertEqual("http://localhost:3001/course/11/lesson/220", actual)
