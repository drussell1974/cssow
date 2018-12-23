
from unittest import TestCase

import sys
sys.path.insert(0, '../')

from cls_learningepisode import LearningEpisodeModel
from learningepisode_testcase import LearningEpisode_TestCase

class test_LearningEpisode__get_ui_sub_heading(LearningEpisode_TestCase):

    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_with_scheme_of_work_name(self):
        # set up
        test = self._construct_valid_object()
        test.scheme_of_work_name = "GCSE Computer Science"
        # test
        val = test.get_ui_sub_heading()

        # assert
        self.assertEqual("Learning Episode for GCSE Computer Science", val)


class test_LearningEpisode__get_ui_title(LearningEpisode_TestCase):

    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_with__order_of_delivery_only(self):
        # set up
        test = self._construct_valid_object()

        # test
        val = test.get_ui_title()

        # assert
        self.assertEqual("Week 2", val)

    def test_with_order_of_delivery__and__topic_name(self):
        # set up
        test = self._construct_valid_object()
        test.topic_name = "Algorithms"
        # test
        val = test.get_ui_title()

        # assert
        self.assertEqual("Week 2 - Algorithms", val)

    def test_with_order_of_delivery__and__topic_name__and__parent_topic_name(self):
        # set up
        test = self._construct_valid_object()
        test.topic_name = "Algorithms"
        test.parent_topic_name = "Program structures"
        # test
        val = test.get_ui_title()

        # assert
        self.assertEqual("Week 2 - Program structures : Algorithms", val)
