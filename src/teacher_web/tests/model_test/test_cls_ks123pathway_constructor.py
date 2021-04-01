from unittest import TestCase
from shared.models.cls_ks123pathway import KS123PathwayModel
from tests.test_helpers.mocks import *

@patch("shared.models.core.django_helper", return_value=fake_ctx_model())
class test_cls_ks123pathway_constructor(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass


    def test_constructor_default(self, mock_auth_user):

        # self.test
        self.test = KS123PathwayModel(0, "", year_id=0, topic_id=1, ctx=mock_auth_user)

        # assert
        self.assertEqual(0, self.test.id)
        self.assertEqual("", self.test.objective)
        self.assertFalse(self.test.is_valid)
        self.assertTrue(self.test.is_new())


    def test_constructor_set_valid_values(self, mock_auth_user):

        # self.test
        self.test = KS123PathwayModel(1, "To be able to...", year_id=1, topic_id=1, ctx=mock_auth_user)

        self.test.validate()

        # assert
        self.assertEqual(1, self.test.id)
        self.assertEqual("To be able to...", self.test.objective)
        self.assertTrue(self.test.is_valid)
        self.assertFalse(self.test.is_new())
