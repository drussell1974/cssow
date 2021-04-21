from unittest import TestCase
from unittest.mock import patch
from shared.models.cls_topic import TopicModel
from tests.test_helpers.mocks import *

class test_cls_topic__clean_up(TestCase):

    def setUp(self):
        with patch("shared.models.core.django_helper", return_value=fake_ctx_model()) as mock_auth_user:
            self.test = TopicModel(1, "", auth_ctx=mock_auth_user)


    def test_name__trim_whitespace(self):

        self.test.name = " x "

        # test
        self.test._clean_up()

        # assert
        self.assertEqual("x", self.test.name)


