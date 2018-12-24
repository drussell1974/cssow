from learningobjective_testcase import LearningObjective_TestCase


class test_SchemeOfWork_clean_up__topic_name(LearningObjective_TestCase):

    def test__trim_whitespace(self):
        test = self._construct_valid_object()

        test.topic_name = " x "

        # test
        test._clean_up()

        # assert
        self.assertEqual(test.topic_name, "x")


class test_SchemeOfWork_clean_up__parent_topic_name(LearningObjective_TestCase):

    def test__trim_whitespace(self):
        test = self._construct_valid_object()

        test.parent_topic_name = " x "

        # test
        test._clean_up()

        # assert
        self.assertEqual(test.parent_topic_name, "x")


class test_SchemeOfWork_clean_up__content_description(LearningObjective_TestCase):

    def test__trim_whitespace(self):
        test = self._construct_valid_object()

        test.content_description = " x "

        # test
        test._clean_up()

        # assert
        self.assertEqual(test.content_description, "x")


class test_SchemeOfWork_clean_up__exam_board_name(LearningObjective_TestCase):

    def test__trim_whitespace(self):
        test = self._construct_valid_object()

        test.exam_board_name = " x "

        # test
        test._clean_up()

        # assert
        self.assertEqual(test.exam_board_name, "x")


class test_SchemeOfWork_clean_up__learning_episode_name(LearningObjective_TestCase):

    def test__trim_whitespace(self):
        test = self._construct_valid_object()

        test.learning_episode_name = " x "

        # test
        test._clean_up()

        # assert
        self.assertEqual(test.learning_episode_name, "x")


class test_SchemeOfWork_clean_up__key_stage_name(LearningObjective_TestCase):

    def test__trim_whitespace(self):
        test = self._construct_valid_object()

        test.key_stage_name = " x "

        # test
        test._clean_up()

        # assert
        self.assertEqual(test.key_stage_name, "x")
