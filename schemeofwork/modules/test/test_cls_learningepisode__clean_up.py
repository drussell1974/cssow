from unittest import TestCase

import sys
sys.path.insert(0, '../')

from cls_learningepisode import LearningEpisodeModel
from learningepisode_testcase import LearningEpisode_TestCase

class test_LearningEpisodeModel__clean_up___scheme_of_work_name(LearningEpisode_TestCase):

    def test__trim_whitespace(self):
        test = self._construct_valid_object()

        test.scheme_of_work_name = " x "

        # test
        test._clean_up()

        # assert
        self.assertEqual(test.scheme_of_work_name, "x")


class test_LearningEpisodeModel_clean_up__key_stage_name(LearningEpisode_TestCase):

    def test__trim_whitespace(self):
        test = self._construct_valid_object()

        test.key_stage_name = " x "

        # test
        test._clean_up()

        # assert
        self.assertEqual(test.key_stage_name, "x")
