import sys
sys.path.append('../../schemeofwork/modules')

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
        self.assertEqual("for GCSE Computer Science - Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam convallis volutpat.", val)


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


class test_LearningEpisode__get_list_of_key_words(LearningEpisode_TestCase):

    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_get_list_of_key_words__where_None(self):
        # setup
        test = self._construct_valid_object()

        # test
        test.key_words = None
        result = test.get_list_of_key_words()

        # assert
        self.assertEqual([], result)


    def test_get_list_of_key_words__where_Min(self):
        # setup
        test = self._construct_valid_object()

        # test
        test.key_words = "aliquet"
        result = test.get_list_of_key_words()

        # assert
        self.assertEqual(['aliquet'], result)


    def test_get_list_of_key_words__where_Max(self):
        # setup
        test = self._construct_valid_object()

        # test
        test.key_words = "Lorem ipsum, dolor, sit, amet, consectetur, adipiscing elit, Nulla, ut, nunc, quis est, ornare, tincidunt, Vivamus, aliquet elementum, ipsum vel"
        result = test.get_list_of_key_words()

        # assert
        self.assertEqual(['Lorem ipsum',
                         ' dolor',
                         ' sit',
                         ' amet',
                         ' consectetur',
                         ' adipiscing elit',
                         ' Nulla',
                         ' ut',
                         ' nunc',
                         ' quis est',
                         ' ornare',
                         ' tincidunt',
                         ' Vivamus',
                         ' aliquet elementum',
                         ' ipsum vel'], result)
