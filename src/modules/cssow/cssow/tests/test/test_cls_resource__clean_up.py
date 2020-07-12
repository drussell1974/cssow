from tests.model_test._unittest import TestCase
from web.shared.models.cls_resource import ResourceModel

from unittest import TestCase

class test_cls_resource__clean_up(TestCase):

    def setUp(self):
        self.test = ResourceModel(1, title="", publisher="", lesson_id=999, scheme_of_work_id=99, page_uri="", page_note="")


    # title

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

    # publisher

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

    # page_uri

    def test_page_uri__trim_whitespace(self):

        self.test.page_uri = " x "

        # test
        self.test._clean_up()

        # assert
        self.assertEqual("x", self.test.page_uri)


    def test_page_uri__escape_sqlterminator(self):

        self.test.page_uri = "x;"

        # test
        self.test._clean_up()

        # assert
        self.assertEqual("x\;", self.test.page_uri)


    def test_page_uri__escape_quote(self):

        self.test.page_uri = "'x'"

        # test
        self.test._clean_up()

        # assert
        self.assertEqual('"x"', self.test.page_uri)

    # page_note

    def test_page_note__trim_whitespace(self):

        self.test.page_note = " x "

        # test
        self.test._clean_up()

        # assert
        self.assertEqual("x", self.test.page_note)


    def test_page_note__escape_sqlterminator(self):

        self.test.page_note = "x;"

        # test
        self.test._clean_up()

        # assert
        self.assertEqual("x\;", self.test.page_note)


    def test_page_note__escape_quote(self):

        self.test.page_note = "'x'"

        # test
        self.test._clean_up()

        # assert
        self.assertEqual('"x"', self.test.page_note)

    # publisher

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
        self.assertEqual('x\;', self.test.publisher)


    def test_publisher__escape_quote(self):

        self.test.publisher = "'x'"

        # test
        self.test._clean_up()

        # assert
        self.assertEqual('"x"', self.test.publisher)


    # md_document_name

    def test_md_document_name__trim_whitespace(self):

        self.test.md_document_name = " x "

        # test
        self.test._clean_up()

        # assert
        self.assertEqual("x", self.test.md_document_name)


    def test_md_document_name__escape_sqlterminator(self):

        self.test.md_document_name = "x;"

        # test
        self.test._clean_up()

        # assert
        self.assertEqual("x\;", self.test.md_document_name)


    def test_md_document_name__escape_quote(self):

        self.test.md_document_name = "'x'"

        # test
        self.test._clean_up()

        # assert
        self.assertEqual('"x"', self.test.md_document_name)
