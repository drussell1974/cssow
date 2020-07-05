from unittest import TestCase

from datetime import datetime
from cssow.models.cls_learningobjective import LearningObjectiveModel


class LearningObjective_TestCase(TestCase):

    current_date_for_test = ""

    """ Shared functions """
    def setUp(self):
        self.current_date_for_test = datetime.today()

    def _construct_valid_object(self):#
        """ Create a valid Object """
        # set up
        test = LearningObjectiveModel(1,
                                      description = "lo test description",
                                      scheme_of_work_name = "GCSE Computer Science",
                                      solo_taxonomy_id = 1,
                                      solo_taxonomy_name = "Unistructural",
                                      solo_taxonomy_level = "B",
                                      #topic_id = 2,
                                      #topic_name = "Algorithms",
                                      parent_topic_id = 3,
                                      parent_topic_name = "Programming",
                                      content_id = 4,
                                      content_description = "Understanding Havard Architecture",
                                      #exam_board_id = 5,
                                      #exam_board_name = "AQA",
                                      lesson_id = 6,
                                      lesson_name = "Lesson 30",
                                      key_stage_id = 7,
                                      key_stage_name = "KS7",
                                      parent_id = 99,
                                      created = self.current_date_for_test,
                                      created_by_id = 8,
                                      created_by_name = "Dave Russell",
                                      published=1)


        # test
        test.validate()

        # assert
        self.assertEqual(test.description, "lo test description", "--- setup --- description failed")
        self.assertEqual(test.scheme_of_work_name, "GCSE Computer Science", "--- setup --- scheme_of_work_name failed")
        self.assertEqual(test.solo_taxonomy_id, 1, "--- setup --- solo_taxonomy_id failed")
        self.assertEqual(test.solo_taxonomy_name, "Unistructural", "--- setup --- solo_taxonomy_name failed")
        self.assertEqual(test.solo_taxonomy_level, "B", "--- setup --- solo_taxonomy_level failed")
        #self.assertEqual(test.topic_id, 2, "--- setup --- topic_id failed")
        #self.assertEqual(test.topic_name, "Algorithms", "--- setup --- topic_name failed")
        self.assertEqual(test.parent_topic_id, 3, "--- setup --- parent_topic_id failed")
        self.assertEqual(test.parent_topic_name,"Programming", "--- setup --- parent_topic_name failed")
        self.assertEqual(test.content_id, 4, "--- setup --- content_id failed")
        self.assertEqual(test.content_description, "Understanding Havard Architecture", "--- setup --- content_name failed")
        #self.assertEqual(test.exam_board_id, 5, "--- setup --- exam_board_id failed")
        #self.assertEqual(test.exam_board_name, "AQA", "--- setup --- exam_board_name failed")
        self.assertEqual(test.lesson_id, 6, "--- setup --- lesson_id failed")
        self.assertEqual(test.lesson_name, "Lesson 30", "--- setup --- lesson_name  failed")
        self.assertEqual(test.key_stage_id, 7, "--- setup --- key_stage_id failed")
        self.assertEqual(test.key_stage_name, "KS7", "--- setup --- key_stage_name failed")
        self.assertEqual(test.parent_id, 99, "--- setup --- parent_id failed")
        self.assertEqual(test.created, self.current_date_for_test, "--- setup --- created failed")
        self.assertEqual(test.created_by_id, 8, "--- setup --- created_by_id failed")
        self.assertEqual(test.created_by_name, "Dave Russell", "--- setup --- created_by_name failed")

        return test
