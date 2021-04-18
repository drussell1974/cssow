from unittest import TestCase
from shared.models.cls_topic import TopicModel
from tests.test_helpers.mocks import *

@patch("shared.models.core.django_helper", return_value=fake_ctx_model())
class test_cls_topic_constructor(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass


    def test_constructor_default(self, mock_auth_user):

        # self.test
        self.test = TopicModel(0, "", auth_ctx=mock_auth_user)

        # assert
        self.assertEqual(0, self.test.id)
        self.assertEqual("", self.test.name)
        self.assertEqual(1, self.test.lvl)
        self.assertEqual(mock_auth_user.department_id, self.test.department_id)
        self.assertFalse(self.test.is_valid)
        self.assertTrue(self.test.is_new())


    def test_constructor_set_valid_values(self, mock_auth_user):

        # self.test
        self.test = TopicModel(1, "Algorithms", auth_ctx=mock_auth_user)

        self.test.validate()

        # assert
        self.assertEqual(1, self.test.id)
        self.assertEqual("Algorithms", self.test.name)
        self.assertEqual(mock_auth_user.department_id, self.test.department_id)

        self.assertTrue(self.test.is_valid)
        self.assertFalse(self.test.is_new())
