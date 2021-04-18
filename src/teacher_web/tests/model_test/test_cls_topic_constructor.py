from unittest import TestCase
from shared.models.cls_topic import TopicModel


class test_cls_topic_constructor(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass


    def test_constructor_default(self):

        # self.test
        self.test = TopicModel(0, "", department_id=13)

        # assert
        self.assertEqual(0, self.test.id)
        self.assertEqual("", self.test.name)
        self.assertEqual(1, self.test.lvl)
        self.assertEqual(13, self.test.department_id)
        self.assertFalse(self.test.is_valid)
        self.assertTrue(self.test.is_new())


    def test_constructor_set_valid_values(self):

        # self.test
        self.test = TopicModel(1, "Algorithms", department_id=13)

        self.test.validate()

        # assert
        self.assertEqual(1, self.test.id)
        self.assertEqual("Algorithms", self.test.name)
        self.assertEqual(13, self.test.department_id)

        self.assertTrue(self.test.is_valid)
        self.assertFalse(self.test.is_new())
