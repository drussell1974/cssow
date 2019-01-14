import sys
sys.path.append('../../schemeofwork/modules')

from learningobjective_testcase import LearningObjective_TestCase


class test_LearningObjective__get_ui_sub_heading(LearningObjective_TestCase):

    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_with_scheme_of_work_name_and_learning_episode(self):
        # set up
        test = self._construct_valid_object()
        #test.scheme_of_work_name = "GCSE Computer Science"

        # test
        val = test.get_ui_sub_heading()

        # assert
        self.assertEqual("for GCSE Computer Science Week 30", val)


class test_LearningObjective__get_ui_title(LearningObjective_TestCase):

    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_with__description(self):
        # set up
        test = self._construct_valid_object()

        # test
        val = test.get_ui_title()

        # assert
        self.assertEqual("lo test description", val)




