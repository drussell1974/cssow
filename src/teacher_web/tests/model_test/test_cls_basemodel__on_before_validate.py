from datetime import datetime
from unittest import TestCase
from shared.models.core.basemodel import BaseModel


class test_LessonModel__validate___on_before_validate(TestCase):

    test = None

    def setUp(self):
        self.test = BaseModel(0, "some title", datetime.today(), 0, "", 1)

    def tearDown(self):
        pass


    def test_min__valid_extreme(self):
        # test
        self.test._on_before_validate()

        # assert
        self.assertTrue(self.test.is_valid, "is_valid should be True")
        self.assertTrue(len(self.test.validation_errors) == 0)




