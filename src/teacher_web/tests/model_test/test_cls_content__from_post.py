from unittest import TestCase
from shared.models.cls_content import ContentModel as Model


class test_cls_content__from_post(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass


    def test__should_raise_exception__when_not_a_dictionary(self):

        # arrange
        self.test = Model()

        # act

        with self.assertRaises(TypeError):
            # pass json / string
            self.test.from_post('{"id":["1"], "description":["Algorithm"], "letter_prefix":["K"]}')

        # assert
        
        self.assertEqual(0, self.test.id)
        self.assertEqual("", self.test.description)
        self.assertEqual("", self.test.letter_prefix)
        self.assertFalse(self.test.is_valid)
        self.assertEqual({}, self.test.validation_errors)



    def test__should_have_no__validition_errors__when_valid(self):

        # arrange
        self.test = Model()

        # act
        self.test.from_post({
            "id": '1', 
            "description": "Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit",
            "letter_prefix": "Y",
            "key_stage_id":"999",
            "scheme_of_work_id":"11",
            "published":"1"})

        # assert
        
        self.assertEqual(1, self.test.id)
        self.assertEqual("Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit", self.test.description)
        self.assertEqual("Y", self.test.letter_prefix)
        self.assertTrue(self.test.is_valid)
        self.assertEqual({}, self.test.validation_errors)


    def test__should_have__validation_errors__when_not_invalid(self):

        # arrange
        self.test = Model()

        # act
        self.test.from_post({"id":"1", "description":"", "letter_prefix":"X","key_stage_id":"5","scheme_of_work_id":"11","published":"1"})

        # assert
        self.assertFalse(self.test.is_valid)
        self.assertEqual({"description": "required"}, self.test.validation_errors)