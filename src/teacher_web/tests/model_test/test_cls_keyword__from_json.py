from unittest import TestCase
from shared.models.cls_keyword import KeywordModel


class test_cls_keyword__from_json(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass



    def test__should_raise_exception__when_not_a_string(self):

        # arrange
        self.test = KeywordModel()

        # act
        with self.assertRaises(TypeError):
            self.test.from_json({"id":1, "term":"Algorithm", "definition":"A list of instructions"})

        # assert
        
        self.assertEqual(0, self.test.id)
        self.assertEqual("", self.test.term)
        self.assertEqual("", self.test.definition)
        self.assertFalse(self.test.is_valid)
        self.assertTrue(self.test.is_new())


    def test__should_have_no__validition_errors__when_valid(self):

        # arrange
        self.test = KeywordModel()

        # act
        self.test.from_json('{"id":1, "term":"Algorithm", "definition":"A list of instructions"}', 13)

        # assert
        
        self.assertEqual(1, self.test.id)
        self.assertEqual("Algorithm", self.test.term)
        self.assertEqual("A list of instructions", self.test.definition)
        self.assertTrue(self.test.is_valid)
        self.assertFalse(self.test.is_new())



    def test__should_have__validation_errors__when_not_invalid(self):

        # arrange
        self.test = KeywordModel()

        # act
        self.test.from_json('{"id":1, "term":"", "definition":"A list of instructions"}', 13)

        # assert
        self.assertFalse(self.test.is_valid)
        self.assertEqual({"term": "required"}, self.test.validation_errors)