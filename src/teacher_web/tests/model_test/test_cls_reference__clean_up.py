from unittest import TestCase, skip
from shared.models.cls_reference import ReferenceModel

from unittest import TestCase

@skip("Deprecated. No longer used")
class test_cls_reference__clean_up(TestCase):

    def setUp(self):
        self.test = ReferenceModel(1, reference_type_id = 6, reference_type_name = "Website", title = "", publisher = "", year_published = 2016, scheme_of_work_id = 0)


    def test_title__trim_whitespace(self):

        self.test.title = " x "

        # test
        self.test._clean_up()

        # assert
        self.assertEqual("x", self.test.title)


    def test_title__escape_sqlterminator(self):

        self.test.title = "x;"

        # test
        self.test._clean_up()

        # assert
        self.assertEqual("x\;", self.test.title)


    def test_title__escape_quote(self):

        self.test.title = "'x'"

        # test
        self.test._clean_up()

        # assert
        self.assertEqual('"x"', self.test.title)



    def test_authors__trim_whitespace(self):

        self.test.authors = " x "

        # test
        self.test._clean_up()

        # assert
        self.assertEqual("x", self.test.authors)


    def test_publisher__trim_whitespace(self):

        self.test.publisher = " x "

        # test
        self.test._clean_up()

        # assert
        self.assertEqual("x", self.test.publisher)


    def test_publisher__escape_sqlterminator(self):

        self.test.publisher = "x;"

        # test
        self.test._clean_up()

        # assert
        self.assertEqual("x\;", self.test.publisher)


    def test_publisher__escape_quote(self):

        self.test.publisher = "'x'"

        # test
        self.test._clean_up()

        # assert
        self.assertEqual('"x"', self.test.publisher)
