from unittest import TestCase
from shared.models.cls_resource import ResourceModel


class test_cls_resource__constructor(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass


    def test_constructor_default(self):

        # self.test
        self.test = ResourceModel(0, 
            scheme_of_work_id=6,
            lesson_id=12,
            title="How to create a unit test with unitest python",
            publisher="Phaidon")

        # assert
        self.assertEqual(0, self.test.id)
        self.assertEqual(6, self.test.scheme_of_work_id, "scheme_of_work_id should be 6")
        self.assertEqual(12, self.test.lesson_id, "lesson_id should be 0")
        self.assertEqual("How to create a unit test with unitest python", self.test.title)
        self.assertEqual("Phaidon", self.test.publisher)
        
        self.assertEqual(0, self.test.type_id, "type_id should be 0")
        self.assertEqual("", self.test.type_name, "type_name should be ''")  
        self.assertEqual("", self.test.type_icon, "type_icon should be ''")  
        self.assertEqual("", self.test.page_note, "page_note should be ''")
        self.assertEqual("", self.test.page_uri, "page_uri should be ''")
        self.assertEqual("", self.test.md_document_name, "md_document_name should be ''")
        self.assertFalse(self.test.is_expired, "is_expired should be false")
        self.assertFalse(self.test.is_valid)
        self.assertTrue(self.test.is_new())


    def test_constructor_set_valid_values(self):

        # setup

        self.test = ResourceModel(1,
                                 scheme_of_work_id=6,
                                 lesson_id=12,
                                 title="Motherboards and the CPU",
                                 publisher="Sybex",
                                 type_id=3,
                                 type_name="Book",
                                 page_note="Note here!",
                                 page_uri="http://jazzthecat.co.uk",
                                 md_document_name="README.md",
                                 is_expired=True)

        # self.test
        self.test.validate()

        # assert
        self.assertEqual(1, self.test.id)
        self.assertEqual(6, self.test.scheme_of_work_id)
        self.assertEqual(12, self.test.lesson_id)
        self.assertEqual(3, self.test.type_id)
        self.assertEqual("Book", self.test.type_name)
        self.assertEqual("Note here!", self.test.page_note)
        self.assertEqual("http://jazzthecat.co.uk", self.test.page_uri)
        self.assertEqual("README.md", self.test.md_document_name)
        self.assertTrue(self.test.is_expired, "is_expired should be true")
        self.assertEqual({}, self.test.validation_errors)
        self.assertTrue(self.test.is_valid)
        self.assertFalse(self.test.is_new())
