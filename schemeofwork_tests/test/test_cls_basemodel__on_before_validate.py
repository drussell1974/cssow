from unittest import TestCase
import sys
sys.path.append('../../schemeofwork/modules')

from basemodel import BaseModel
from datetime import datetime


class test_LearningEpisodeModel__validate___on_before_validate(TestCase):

    test = None

    def setUp(self):
        self.test = BaseModel(0, datetime.today(), 0, "", 1)

    def tearDown(self):
        pass


    def test_min__valid_extreme(self):
        # test
        self.test._on_before_validate()

        # assert
        self.assertTrue(self.test.is_valid, "is_valid should be True")
        self.assertTrue(len(self.test.validation_errors) == 0)




