from _unittest import TestCase
from learningepisode_testcase import LearningEpisode_TestCase

class test_LearningEpisodeModel__clean_up___scheme_of_work_name(LearningEpisode_TestCase):

    def setUp(self):
        self.test = self._construct_valid_object()


    def test__trim_whitespace(self):
        test = self._construct_valid_object()

        test.scheme_of_work_name = " x "

        # test
        test._clean_up()

        # assert
        self.assertEqual(test.scheme_of_work_name, "x")


    def test__escape_sqlterminator(self):

        self.test.scheme_of_work_name = "x;"

        # test
        self.test._clean_up()

        # assert
        self.assertEqual("x\;", self.test.scheme_of_work_name)


    def test__escape_quote(self):

        self.test.scheme_of_work_name = "'x'"

        # test
        self.test._clean_up()

        # assert
        self.assertEqual('"x"', self.test.scheme_of_work_name)


class test_LearningEpisodeModel_clean_up__key_stage_name(LearningEpisode_TestCase):

    def setUp(self):
        self.test = self._construct_valid_object()

    def test__trim_whitespace(self):
        test = self._construct_valid_object()

        test.key_stage_name = " x "

        # test
        test._clean_up()

        # assert
        self.assertEqual(test.key_stage_name, "x")


    def test__escape_sqlterminator(self):

        self.test.key_stage_name = "x;"

        # test
        self.test._clean_up()

        # assert
        self.assertEqual("x\;", self.test.key_stage_name)


    def test__escape_quote(self):

        self.test.key_stage_name = "'x'"

        # test
        self.test._clean_up()

        # assert
        self.assertEqual('"x"', self.test.key_stage_name)



class test_LearningEpisodeModel_clean_up__pathway_objective_ids(LearningEpisode_TestCase):

    def setUp(self):
        self.test = self._construct_valid_object()

    def test__trim_whitespace(self):
        test = self._construct_valid_object()

        test.pathway_objective_ids = [" x "]

        # test
        test._clean_up()

        # assert
        self.assertEqual(["x"], test.pathway_objective_ids)


    def test__multiple_items(self):
        test = self._construct_valid_object()

        test.pathway_objective_ids = [" x", " y", "z "]

        # test
        test._clean_up()

        # assert
        self.assertEqual(["x","y","z"], test.pathway_objective_ids)


    def test__remove_duplicates(self):
        test = self._construct_valid_object()

        test.pathway_objective_ids = ["x", "y", "z", "y"]

        # test
        test._clean_up()

        # assert
        self.assertEqual(["x", "y", "z"], test.pathway_objective_ids)


    def test__escape_sqlterminator(self):

        self.test.pathway_objective_ids = ["x;", "y", "z", "y"]

        # test
        self.test._clean_up()

        # assert
        self.assertEqual(["x\;", "y", "z"], self.test.pathway_objective_ids)


    def test__escape_quote(self):

        self.test.pathway_objective_ids = ["x", "'y'", "z", "y"]

        # test
        self.test._clean_up()

        # assert
        self.assertEqual(["x", '"y"', "z", "y"], self.test.pathway_objective_ids)


class test_LearningEpisodeModel_clean_up__keywords(LearningEpisode_TestCase):

    def setUp(self):
        self.test = self._construct_valid_object()

    def test__trim_whitespace(self):
        test = self._construct_valid_object()

        test.key_words = " x "

        # test
        test._clean_up()

        # assert
        self.assertEqual("x", test.key_words)


    def test__multiple_items(self):
        test = self._construct_valid_object()

        test.key_words = "w x, y, z "

        # test
        test._clean_up()

        # assert
        self.assertEqual("w x,y,z", test.key_words)


    def test__escape_sqlterminator(self):

        self.test.key_words = "x;"

        # test
        self.test._clean_up()

        # assert
        self.assertEqual("x\;", self.test.key_words)


    def test__escape_quote(self):

        self.test.key_words = "'x'"

        # test
        self.test._clean_up()

        # assert
        self.assertEqual('"x"', self.test.key_words)
