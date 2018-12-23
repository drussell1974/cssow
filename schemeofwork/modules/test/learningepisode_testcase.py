from unittest import TestCase
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
                                 key_stage_id=6)


        # test
        test.validate()

        # assert
        self.assertEqual(1, test.id)
        self.assertEqual(2, test.order_of_delivery_id)
        self.assertEqual(3, test.scheme_of_work_id)
        self.assertEqual(4, test.topic_id)
        self.assertEqual(5, test.parent_topic_id)
        self.assertEqual(6, test.key_stage_id)
        self.assertTrue(test.is_valid)

        return test
