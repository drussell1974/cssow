from unittest import TestCase
from shared.models.cls_topic import TopicModel


class test_cls_topic__clean_up(TestCase):

    def setUp(self):
        self.test = TopicModel(1, "", department_id=13)


    def test_name__trim_whitespace(self):

        self.test.name = " x "

        # test
        self.test._clean_up()

        # assert
        self.assertEqual("x", self.test.name)


