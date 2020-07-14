from unittest import TestCase
from shared.models.cls_keyword import KeywordModel


class test_cls_reference_note_constructor(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass


    def test_constructor_default(self):

        # self.test
        self.test = KeywordModel(0, "", "")

        # assert
        self.assertEqual(0, self.test.id)
        self.assertEqual("", self.test.term, "term should be ''")
        self.assertEqual("", self.test.definition, "definition should be ''")
        self.assertTrue(self.test.is_new())


    def test_constructor_set_valid_values(self):

        # self.test
        self.test = KeywordModel(1, "Algorithm", "A list of instructions")

        self.test.validate()

        # assert
        self.assertEqual(1, self.test.id)
        self.assertEqual("Algorithm", self.test.term, "term should be ''")
        self.assertEqual("A list of instructions", self.test.definition, "definition should be ''")
        self.assertTrue(self.test.is_valid)
        self.assertFalse(self.test.is_new())
