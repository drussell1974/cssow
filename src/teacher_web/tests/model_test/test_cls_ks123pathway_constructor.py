from unittest import TestCase
from shared.models.cls_ks123pathway import KS123PathwayModel


class test_cls_ks123pathway_constructor(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass


    def test_constructor_default(self):

        # self.test
        self.test = KS123PathwayModel(0, "", year_id=0, topic_id=1)

        # assert
        self.assertEqual(0, self.test.id)
        self.assertEqual("", self.test.objective)
        self.assertFalse(self.test.is_valid)
        self.assertTrue(self.test.is_new())


    def test_constructor_set_valid_values(self):

        # self.test
        self.test = KS123PathwayModel(1, "To be able to...", year_id=1, topic_id=1)

        self.test.validate()

        # assert
        self.assertEqual(1, self.test.id)
        self.assertEqual("To be able to...", self.test.objective)
        self.assertTrue(self.test.is_valid)
        self.assertFalse(self.test.is_new())
