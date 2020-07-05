from tests.model_test._unittest import TestCase
from shared.models.cls_reference import ReferenceModel


class test_cls_reference_constructor(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass


    def test_constructor_default(self):

        # self.test
        self.test = ReferenceModel(0, reference_type_id = 0, reference_type_name = "Website", title="Title here!", year_published = 2019, publisher="Penguin", scheme_of_work_id = 0)

        # assert
        self.assertEqual(0, self.test.id)
        self.assertEqual("Title here!", self.test.title, "title should be ''")
        self.assertEqual("Penguin", self.test.publisher, "publisher should be ''")
        self.assertEqual("", self.test.authors, "authors should be ''")
        self.assertEqual("", self.test.uri, "uri should be ''")
        self.assertEqual(0, self.test.scheme_of_work_id, "scheme_of_work_id should be 0")


    def test_constructor_set_valid_values(self):

        # setup

        self.test = ReferenceModel(1,
                                 reference_type_id=6,
                                 reference_type_name = "Website",
                                 title="Title here",
                                 publisher="Penguin",
                                 year_published = 2019,
                                 authors="Russell, D.;Russell, A.;",
                                 uri="http://jazzthecat.co.uk",
                                 scheme_of_work_id = 1)

        # self.test
        self.test.validate()

        # assert
        self.assertEqual(6, self.test.reference_type_id)
        self.assertEqual("Website", self.test.reference_type_name)
        self.assertEqual("Title here", self.test.title)
        self.assertEqual("Penguin", self.test.publisher)
        self.assertEqual("Russell, D.\;Russell, A.\;", self.test.authors)
        self.assertEqual("http://jazzthecat.co.uk", self.test.uri)
        self.assertEqual(1, self.test.scheme_of_work_id)
        self.assertTrue(self.test.is_valid)
