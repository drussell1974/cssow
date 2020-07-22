from unittest import TestCase
from shared.models.cls_keyword import KeywordModel


class test_cls_keyword__from_json(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass


    def test__from_json__when_valid(self):

        # arrange
        self.test = KeywordModel()

        # act
        self.test.from_json('{"id":1, "term":"Algorithm", "definition":"A list of instructions"}')

        # assert
        
        self.assertEqual(1, self.test.id)
        self.assertEqual("Algorithm", self.test.term, "term should be ''")
        self.assertEqual("A list of instructions", self.test.definition, "definition should be ''")
        self.assertTrue(self.test.is_valid)
        self.assertFalse(self.test.is_new())



    def test__from_json__when_invalid_values(self):

        # arrange
        self.test = KeywordModel()

        # act
        self.test.from_json('{"id":1, "term":"", "definition":"A list of instructions"}')

        # assert
        self.assertFalse(self.test.is_valid)
        self.assertEqual({"term": "required"}, self.test.validation_errors)