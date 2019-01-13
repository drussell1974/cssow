from unittest import TestCase
import sys
from cls_learningepisode import LearningEpisodeModel

class LearningEpisode_TestCase(TestCase):
    """ Shared functions """
    def _construct_valid_object(self):#
        """ Create a valid Object """
        # set up
        test = LearningEpisodeModel(1,
                                 order_of_delivery_id=2,
                                 scheme_of_work_id=3,
                                 topic_id=4,
                                 parent_topic_id=5,
                                 key_stage_id=6,
                                 key_words = "Lorem ipsum,sit amet,convallis",
                                 summary = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam convallis volutpat.",
                                 published=1)


        # test
        test.validate()

        # assert
        self.assertEqual(1, test.id)
        self.assertEqual(2, test.order_of_delivery_id)
        self.assertEqual(3, test.scheme_of_work_id)
        self.assertEqual(4, test.topic_id)
        self.assertEqual(5, test.parent_topic_id)
        self.assertEqual(6, test.key_stage_id)
        self.assertEqual("lorem ipsum,sit amet,convallis", test.key_words)
        self.assertEqual("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam convallis volutpat.", test.summary)
        self.assertTrue(test.is_valid)

        return test
