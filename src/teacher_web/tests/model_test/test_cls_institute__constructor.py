from unittest import TestCase, skip
from shared.models.cls_institute import InstituteModel


@skip("not implemented")
class test_cls_institute__constructor(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass


    def test_constructor_default(self):

        # self.test
        self.test = InstituteModel(0, name="Lorem ipsum")

        # assert
        self.assertEqual(0, self.test.id)
        self.assertEqual("Lorem ipsum", self.test.name)
        self.assertFalse(self.test.is_valid)
        self.assertTrue(self.test.is_new())


    def test_constructor_set_valid_values(self):

        # setup

        self.test = InstituteModel(1, name="Sor shurem")

        # self.test
        self.test.validate()

        # assert
        self.assertEqual(1, self.test.id)
        self.assertEqual("Sor shurem", self.test.name)
        self.assertEqual({}, self.test.validation_errors)
        self.assertTrue(self.test.is_valid)
        self.assertFalse(self.test.is_new())
