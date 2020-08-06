from unittest import TestCase
from shared.models.cls_lesson import LessonModel


class test_cls_lesson__from_json(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass


    def test__from_json__when_valid(self):

        # arrange
        self.test = LessonModel()

        # act
        self.test.from_json('{"id": 220,"title": "Types of CPU architecture","summary": "","order_of_delivery_id": 3,"scheme_of_work_id": 11,"topic_id": 1,"year_id": 12,"key_stage_id": 5,"published": 1}')

        # assert
        
        self.assertEqual(220, self.test.id)
        self.assertEqual("Types of CPU architecture", self.test.title)
        self.assertTrue(self.test.is_valid)
        self.assertFalse(self.test.is_new())


    def test__from_json__when_invalid_values(self):

        # arrange
        self.test = LessonModel()

        # act
        self.test.from_json('{"id": 220,"title": "","summary": "abcd","order_of_delivery_id": 3,"scheme_of_work_id": 11,"topic_id": 1,"year_id": 12,"key_stage_id": 5,"published": 1}')

        # assert
        self.assertFalse(self.test.is_valid)
        self.assertEqual({"title": "required"}, self.test.validation_errors)