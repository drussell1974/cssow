import sys
sys.path.append('../../schemeofwork/modules')
from cls_reference import ReferenceModel

from unittest import TestCase

class test_cls_reference__clean_up(TestCase):

    def setUp(self):
        self.test = ReferenceModel(1, reference_type_id = 6, reference_type_name = "Website", title = "", publisher = "", year_published = 2016, scheme_of_work_id = 0)


    def test_title__trim_whitespace(self):

        self.test.title = " x "

        # test
        self.test._clean_up()

        # assert
        self.assertEqual("x", self.test.title)


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
